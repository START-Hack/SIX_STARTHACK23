import javax.net.ssl.KeyManagerFactory;
import javax.net.ssl.SSLContext;
import java.io.FileInputStream;
import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.security.GeneralSecurityException;
import java.security.KeyStore;

// Requires JDK 17 and no external libraries
public class SampleJavaClient {

    private static final String URL = "https://web.api.six-group.com";
    private static final String CERTIFICATE = "C:/path/to//certificate.p12";
    private static final String PASSWORD = "ask SIX";

    public static void main(String[] args) throws Exception {
        // 1. create mTLS
        SSLContext sslContext = createSslContextOrFail();

        // 2. create HTTP/2 client with mTLS setup
        HttpClient httpClient = HttpClient.newBuilder().version(HttpClient.Version.HTTP_2).sslContext(sslContext).build();

        // 3. create the request
        URI instrumentSummary = URI.create(URL + "/api/findata/v1/instruments/referenceData/instrumentSummary?ids=AAPL_67&scheme=TICKER_BC");
        HttpRequest request = HttpRequest.newBuilder()
                .uri(instrumentSummary)
                .header("api-version", "2023-01-01")
                .build();

        // 4. send the request (blocking the current thread)
        HttpResponse<String> response = httpClient.send(request, HttpResponse.BodyHandlers.ofString());

        // 5. just show the response
        System.out.println(response.body());
    }

    private static SSLContext createSslContextOrFail() throws GeneralSecurityException, IOException {
        KeyStore store = KeyStore.getInstance("PKCS12");
        store.load(new FileInputStream(CERTIFICATE), PASSWORD.toCharArray());
        KeyManagerFactory keyManagerFactory = KeyManagerFactory.getInstance("SunX509");
        keyManagerFactory.init(store, PASSWORD.toCharArray());
        SSLContext sslContext = SSLContext.getInstance("TLSv1.2");
        sslContext.init(keyManagerFactory.getKeyManagers(), null, null);
        return sslContext;
    }

}
