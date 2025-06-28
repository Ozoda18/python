import pandas as pd
population=pd.read_csv('population.csv')
print(population.head());
pop_sal=pd.read_csv('population_salary_analysis.csv')
print(pop_sal.head())
sales_data=pd.read_csv('sales_data.csv')
print(sales_data.head());

print((sales_data
        .groupby('Category')
         .agg(['sum','max']) 
         ));

top_sellers=(sales_data.groupby(['Category','Product'])['Quantity']
             .sum()
             .reset_index()
             .sort_values(['Category','Quantity'],ascending=[True,False])
             .groupby('Category',as_index=False)
             .first())
print(top_sellers);

sales_data['Sales']=sales_data['Quantity']*sales_data['Price']
daily_sales = sales_data.groupby('Date', as_index=False)['Sales'].sum()
max_idx = daily_sales['Sales'].idxmax()
top_day = daily_sales.loc[max_idx]
print(top_day);

cus_orders=pd.read_csv('customer_orders.csv')
print(cus_orders.head(101));

grouped=cus_orders.groupby('CustomerID')['CustomerID'].transform('size')>=20
filtered=cus_orders[grouped]
print(filtered);

cus_orders['TotalPrice'] = cus_orders['Quantity'] * cus_orders['Price']


avg_price_per_unit = cus_orders.groupby(['CustomerID', 'Product']).agg(
    avg_price=('Price', 'mean'),
    total_quantity=('Quantity', 'sum'),
    total_price=('TotalPrice', 'sum')
).reset_index()


filtered_customers = avg_price_per_unit[avg_price_per_unit['avg_price'] > 120]

print(filtered_customers);

product_summary = cus_orders.groupby('Product').agg(
    total_quantity=('Quantity', 'sum'),
    total_price=('TotalPrice', 'sum')
).reset_index()


filtered_products = product_summary[product_summary['total_quantity'] >= 5]

print(filtered_products);





