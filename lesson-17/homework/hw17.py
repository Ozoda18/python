import pandas as pd
data = {'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
         'Age': [25, 30, 35, 40], 
         'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']} 
df = pd.DataFrame(data)
print(df)
def to_clean(val):
    return val.lower().replace(' ','_')
print(to_clean('First_name','Age','City'))
print(data.head(3))
age=data['age']
print(age.mean())
subset=df[['Name','City']]
print(subset)
print(data.assign('Salary'='some value'))
summary=df.describe()
print(summary);

dataframe = {'Month': ['Jan', 'Feb', 'Mar', 'April'],
         'Sales': [5000, 6000, 7500, 8000], 
         'Expenses': [3000, 3500, 4000, 4500]}
df=pd.DataFrame(dataframe);

sales=dataframe['Sales']
print(sales.min())
print(sales.max());
expenses=dataframe['Expenses']
print(expenses.min())
print(expenses.max())
print(expenses.mean())
print(sales.mean());

expenses = {'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
         'January': [1200, 200, 300,150], 
         'February': [1300, 220, 3200, 160],
         'March':[1400,240,330,170],
         'April':[1500,250,350,180]}
df=pd.DataFrame(dataframe)
expenses.set_index('Category');
rent=expenses['Rent']
print(rent.min())
print(rent.max())
print(rent.mean());
utilities=expenses['Utilities']
print(utilities.min())
print(utilities.max())
print(utilities.mean())
groceries=expenses['Groceries']
print(groceries.min())
print(groceries.max())
print(groceries.mean())
entertainment=expenses['Entertainment']
print(entertainment.min())
print(entertainment.max())
print(entertainment.mean());








