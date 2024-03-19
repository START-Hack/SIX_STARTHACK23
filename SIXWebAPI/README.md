# SIX Web API - Introduction

SIX Web API is a web API to retrive information of financial instruments and companies. You can for instance, retrieve the price of a financial instrument or get some further description. You can even get a financial instrument price in real-time via a WebSocket connection: each time the financial instrument price changes you receive an update on the WebSocket.
SIX Web API leverages 3 technologies REST/JSON, GraphQL and WebSockects. It is accessible via the [API Portal](https://web.apiportal.six-group.com/portal/bfi/home).

You can access the API documentation and samples on [here](https://web.apiportal.six-group.com/portal/bfi/documentation).

# SIX Web API - Accounts
The Web API uses certificates for authentication. In the current folder, you will find 10 user accounts: CH52991-hackathon1, CH52991-hackathon2,... CH52991-hackathon10. We recommend you to agreed with the other teams on the account to use as each account is limited to 5 requests per second. If you go above the limit an *HTTP 429* message will be returned. An http header indicates how long you have to wait before sending the next request.

The account contains a *p12 key* that you can register in your web browser to use the [API Portal](https://web.apiportal.six-group.com/portal/bfi/home) swagger interfaces. The file *password.txt* contains the password of the p12 key. The process to register the *p12 key* is described in the [documentation, Step 2 register p12 certificate in browser](https://web.apiportal.six-group.com/portal/bfi/documentation#request-in-portal)
Most http libraries do not use a p12 key but a certificate and a private key. Therefore we also provided you a *private-key.pem* and a *signed-certificate.pem* files.

In the folder, you will also a *CSR.pem* file. This is a certificate request file. It is useless for you.

In the API documentation, you can find samples:
For **Python**
- [How to connect using Python](https://web.apiportal.six-group.com/portal/bfi/documentation#how-to-connect-using-python)
- [GraphQL request using Phython](https://web.apiportal.six-group.com/portal/bfi/documentation#graphql-request-in-python)
For **Java**
- [How to connect using Java](https://web.apiportal.six-group.com/portal/bfi/documentation#how-to-connect-using-java)
- [GraphQL request using Java](https://web.apiportal.six-group.com/portal/bfi/documentation#graphql-request-in-java)
