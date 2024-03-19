# ESG Data - Introduction

ESG stands for Environmental, Social and Governance. In this folder you will get 2 CSV files containing ESG data on investment funds from different countries.
The different ESG aspects of a fund or a company are assessed by *ESG Factors*. An ESG Factor is an evalution criteria. ESG factors cover diverse aspects such as the gas emission, energy consumptions, exposure to human rights issues, anti-corruptions, genders considerations and many other topics.

The 2 files **EUESGMANUFACTURER.csv** and **EUESGMANUFACTURER-LIGHT.csv** refers to data known as EET (European ESG Template) specified by the [FinDatex](https://findatex.eu/). You can find further details on the data on the FinDatex website.

The file **EUESGMANUFACTURER.csv** goes up to 600 ESG factors while **EUESGMANUFACTURER-LIGHT.csv** contains about 80 ESG factors that are relevant for the current state of the regulation. Using the light file is an option for you to reduce the scope of your analysis while focusing on the most important ESG Factors. Both files structures are identical so you can start playing with the light version and then check how your project behave with the full version.

# ESG File Format
The files **EUESGMANUFACTURER.csv** and **EUESGMANUFACTURER-LIGHT.csv** are in CSV format separated by a coma character.

The table below describes each columns. The most important columns are written in **bold**.

| Column Name | Description |
| ----------- | ----------- |
| swissValorNumber | Also named valor. This is an financial instrument identifier. You can use it to query data with the SIX Web API. But we recommend you to use the **ISIN** instead. |
| **ISIN** | An international standard to identify a financial instrument. You can use the ISIN with the Web API and also use it to find more information on the financial instrument on the WEB. |
| **ISIN_BC** | ISIN_BC is the combination of an ISIN code with a bourse code identifier. This is the code to use to retrieve prices in the SIX Web API. Check out the end points *End of Day History*, *Intraday Snapshot* and *Streaming Market Data* |
| FISN | Financial instrument short name according to ISO18774 |
| issuerSIXCompanyKey | Also named **gk**. This is a SIX company identifier that you can use in the *Entity Base* SIX Web API end point |
| LEI | LEI (Legal Entity Identifier) is company identifier same as *issuerSIXCompanyKey*. The difference is that the LEI is a standard identifier. You can also use the LEI in the SIX Web API as well |
| companyDomicile | The country where the company is domiciled |
| *companyDomicileISO* | Same as above the the location is represented in a 2 characters ISO code. You can find services on the Web to download the country flag from the ISO code |
| companyLongName | The company name |
| fundManagerSIXCompanyKey | The company identifier of the fund manager. This is a **gk** code that you can use in the SIX Web API (see issuerSIXCompanyKey for further details) |
| *fundManagerLEI* | Same as above execpt that the fund manager is identified by an **LEI** code (see LEI above for further details).
| fundManagerLongName | The fund manager name |
| ESGValidFrom | Date from which the ESG data is valid. Regarding SFDR, the data is related to the last two calendar years, so it will be valid from January first of the current year. ESG scores may be just current figures which are valid from the date of delivery. The valid from date remains the same, if the data is updated or corrected later. |
| ESGDeliveryDate | Date at which the data has been delivered by the provider. SFDR in example has to be delivered latest by 30 June of the current year. In case of an update or correction, the delivery date is updated as well. |
| **ESGActivity** | ESG Activity assigns an additional key for Taxonomy and EET data. In practice, ESGActivity and ESGClassification creates a categorization of ESG Factors. ESGActivity is the highest level in the categorization while ESGClassification is the second level |
| **ESGClassification** | see ESGActivity |
| **ESGFactor** | The ESG factor name as specified by the FinDatex |
| ESGFactorProviderId | A numerical identifier of the ESG Factor. You can use it as an index |
| **ESGFactorAmountLastYear** | Some ESG Factors are expressed using numerical value representing a quantity or a ratio. The unit is express in the field *ESGFactorAmountLastYearUnit* |
| **ESGFactorAmountLastYearUnit** | See *ESGFactorAmountLastYear* |
| **ESGClassSymbol** | When the ESG Factor is not expressed by a numerical value. The value is expressed by the ESGClassSymbol as a Yes, No or other specific values for the factor. |
| **ESGFactorDate** | When the ESG Factor is a date, then this column will be populated. Note there is not such ESG Factor in the **EUESGMANUFACTURER-LIGHT.csv** file |

Note: An ESG Factor can express a value in 4 different manners.
- The column **ESGFactorAmountLastYear** is populated for amount values, or
- The column **ESGClassSymbol** is populated to express predefined values (e.g. Yes, No, Neutral...), or
- The column **ESGFactorDate** is populated to express date values, or
- None of the above columns are populated. In such case, it means the ESG factor applies to the instrument but does not have a specific value.
