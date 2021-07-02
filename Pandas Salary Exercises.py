import pandas as pd

df = pd.read_csv('Salaries.csv')
#Average BasePay
df['BasePay'].mean()
#highest amount of OvertimePay in the dataset
df['OvertimePay'].max()
#Job title of CHRISTOPHER CHONG ?
df[df['EmployeeName']=='CHRISTOPHER CHONG']['JobTitle']
# How much does JOSEPH DRISCOLL make
df[df['EmployeeName']=='JOSEPH DRISCOLL']['TotalPayBenefits']
#What is the name of highest paid person (including benefits)?
df[df['TotalPayBenefits']== df['TotalPayBenefits'].max()]
#What is the name of lowest paid person (including benefits)?
df[df['TotalPayBenefits']== df['TotalPayBenefits'].min()]
#What was the average BasePay of all employees per year?
df.groupby('Year').mean()['BasePay']
#How many unique job titles are there?
df['JobTitle'].nunique()
#What are the top 5 most common jobs
df['JobTitle'].value_counts().head(5)
#How many Job Titles were represented by only one person in 2013? 
sum(df[df['Year']==2013]['JobTitle'].value_counts() == 1)
#How many people have the word Chief in their job title?
def chief_string(title):
    if 'chief' in title.lower():
        return True
    else:
        return False
   sum(df['JobTitle'].apply(lambda x: chief_string(x)))
