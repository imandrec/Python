import pandas as pd
#Ecommerce Purchases is in the same folder
ecom = pd.read_csv('Ecommerce Purchases') 
#What is the average Purchase Price?
ecom['Purchase Price'].mean()
#What were the highest and lowest purchase prices?
ecom['Purchase Price'].max()
ecom['Purchase Price'].min()
#How many people have English 'en' as their Language of choice on the website?
ecom[ecom['Language']=='en'].count()
#How many people have the job title of "Lawyer" ?
ecom[ecom['Job'] == 'Lawyer'].info()
#How many people made the purchase during the AM and how many people made the purchase during PM ?
ecom['AM or PM'].value_counts()
#What are the 5 most common Job Titles?
ecom['Job'].value_counts().head(5)
#Someone made a purchase that came from Lot: "90 WT" , what was the Purchase Price for this transaction?
ecom[ecom['Lot']=='90 WT']['Purchase Price']
#What is the email of the person with the following Credit Card Number: 4926535242672853
ecom[ecom["Credit Card"] == 4926535242672853]['Email'] 
#How many people have American Express as their Credit Card Provider *and made a purchase above $95 ?
ecom[(ecom['CC Provider']=='American Express') & (ecom['Purchase Price']>95)].count()
#How many people have a credit card that expires in 2025?
sum(ecom['CC Exp Date'].apply(lambda x: x[3:]) == '25')
#What are the top 5 most popular email providers/hosts (e.g. gmail.com, yahoo.com, etc...)
ecom['Email'].apply(lambda x: x.split('@')[1]).value_counts().head(5)
