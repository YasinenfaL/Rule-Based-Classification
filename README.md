
# Customer Potential Revenue Estimation with Rule-Based Classification

## Business Problem
A gaming company wants to create level-based new customer personas and estimate how much potential revenue they can generate based on these new customer definitions by using some characteristics of their customers.
 For example: The company wants to estimate how much revenue an IOS user who is 25 years old and from Turkey can generate on average.


## Dataset Story


 The Persona.csv dataset contains the prices of products sold by an international gaming company and some demographic information of
 users who bought these products. The dataset consists of records generated in each sales transaction. This means that the table is not
 deduplicated. In other words, a user with certain demographic characteristics may have made multiple purchases.
 
* Price: The amount spent by the customer
* Source: The type of device the customer connected from
* Sex: Gender of the customer
* Country: The country of the customer
* Age: Age of the customer

 ### Before 
 
|   PRICE  |  SOURCE  |  SEX   | COUNTRY |  AGE |
|---------|---------|-------|---------|------|
|     39  | android | male  | bra     |   17 |
|     39  | android | male  | bra     |   17 |
|     49  | android | male  | bra     |   17 |
|     29  | android | male  | tur     |   17 |
|     49  | android | male  | tur     |   17 |


### After 

|    | customers_level_based       |    PRICE | SEGMENT |
|---:|:----------------------------|---------:|:-------|
|  0 | BRA_ANDROID_FEMALE_0_18     | 1139.80  | A       |
|  1 | BRA_ANDROID_FEMALE_19_23    | 1070.60  | A       |
|  2 | BRA_ANDROID_FEMALE_24_30    |  508.14  | A       |
|  3 | BRA_ANDROID_FEMALE_31_40    |  233.17  | C       |
|  4 | BRA_ANDROID_FEMALE_41_66    |  236.67  | C       |

