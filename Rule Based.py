#############################################
# Customer Potential Revenue Estimation with Rule-Based Classification
#############################################


#############################################
# Tasks
#############################################


#############################################
# Libraries
#############################################
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# Read the persona.csv file and show general information about the dataset.
df = pd.read_csv("datasets/persona.csv")
df.head()


def check_df(dataframe, head=5):
    print("##################### Shape #####################")
    print(dataframe.shape)
    print("##################### Types #####################")
    print(dataframe.dtypes)
    print("##################### Head #####################")
    print(dataframe.head(head))
    print("##################### Tail #####################")
    print(dataframe.tail(head))
    print("##################### NA #####################")
    print(dataframe.isnull().sum())
    print("##################### Quantiles #####################")
    print(dataframe.describe().T)


check_df(df)

# How many unique SOURCE are there? What are their frequencies?
df["SOURCE"].value_counts()
df["SOURCE"].unique()

# Task 3: How many unique PRICEs are there
df["PRICE"].nunique()

# How many sales were made from which PRICE?
df["PRICE"].value_counts()
df.groupby("PRICE").count()

#  How many sales were made from which country?
df["COUNTRY"].value_counts()
# alternatif
df.groupby("COUNTRY").agg({"SOURCE": "count"}).sort_values(by="SOURCE", ascending=False)

#  How much was earned in total from sales by country?
df.groupby("COUNTRY")["PRICE"].sum()

# alternative
df.groupby("COUNTRY"). \
    agg({"PRICE": "sum"}). \
    sort_values(by="PRICE", ascending=False)

#  What are the sales numbers according to SOURCE types?
df["SOURCE"].value_counts()

# alternative
df.groupby("SOURCE"). \
    agg({"PRICE": "count"})

#  What are the PRICE averages by country?
df.groupby("COUNTRY"). \
    agg({"PRICE": "mean"}). \
    sort_values(by="PRICE", ascending=False)

#  What are the PRICE averages by SOURCEs?
df.groupby("SOURCE") \
    .agg({"PRICE": "mean"})

# What are the PRICE averages in the COUNTRY-SOURCE breakdown?
df.groupby(["COUNTRY", "SOURCE"]). \
    agg({"PRICE": "mean"})

#############################################
# TASK 2: What are the average earnings in breakdown of COUNTRY, SOURCE, SEX, AGE?
#############################################
df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"]). \
    agg({"PRICE": "mean"})

#############################################
# TASK 3: Sort the output by PRICE.
#############################################

agg_df = df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"]) \
    .agg({"PRICE": "mean"}). \
    sort_values(by="PRICE", ascending=False)

#############################################
# TASK 4: Convert the names in the index to variable names.
#############################################
agg_df.reset_index(inplace=True)
agg_df.head()

#############################################
# TASK 5: Convert AGE variable to categorical variable and add it to agg_df.
#############################################

l = [0, 18, 23, 30, 40, 70]

agg_df["AGE_CAT"] = pd.cut(agg_df["AGE"], l, labels=['0_18', '19_23', '24_30', '31_40', '41_70'])

#############################################
# TASK 6: Identify new level based customers and add them as variables to the dataset.
#############################################

agg_df["customer_level_based"] = [i[0].upper() + "_" + i[1].upper() + "_" + i[2].upper() + "_" + i[5].upper() for i in
                                  agg_df.values]
["_".join(row).upper() for row in agg_df[["COUNTRY", "SOURCE", "SEX", "AGE"]].values.astype(str)]

agg_df.head()

agg_df = agg_df.groupby("customer_level_based"). \
    agg({"PRICE": "mean"}). \
    sort_values("PRICE", ascending=False). \
    reset_index()

# alternatıve
for index, row in agg_df.iterrows():
    agg_df["customer_level_based"] = row[0].upper() + "_" + row[1].upper() + "_" + row[2].upper() + "_" + row[5].upper()
    print(agg_df["customer_level_based"])

#############################################
# TASK 7: Segment new customers
#############################################
agg_df["SEGMENT"] = pd.qcut(agg_df["PRICE"], 4, labels=["D", "C", "B", "A"])

#############################################
# TASK 8: Classify the new customers and estimate how much income they can bring.
#############################################
# Which segment does a 33-year-old Turkish woman using ANDROID belong to and how much income is expected to earn on average?
new_user = "TUR_ANDROID_FEMALE_31_40"

agg_df[agg_df["customer_level_based"] == new_user]

# In which segment and on average how much income would a 35-year-old French woman using iOS expect to earn?

new_user1 = "FRA_IOS_FEMALE_31_40"

agg_df[agg_df["customer_level_based"] == new_user1]
