import pandas as pd

customers = pd.DataFrame({
    'customer_id': [1, 2, 3, 4, 5],
    'name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Edward']
})
invoices = pd.DataFrame({
    'invoice_id': [101, 102, 103, 104, 105],
    'customer_id': [1, 2, 3, 4, 5]
})
invoice_items = pd.DataFrame({
    'invoice_id': [101, 101, 102, 103, 104],
    'product_id': [201, 202, 203, 204, 205],
    'quantity': [2, 1, 3, 1, 2],
    'unit_price': [100, 150, 200, 250, 300]
})
merged = invoice_items.merge(invoices, on='invoice_id').merge(customers, on='customer_id')

# Calculate total amount spent per item
merged['total_amount'] = merged['quantity'] * merged['unit_price']

# Group by customer and sum the total amounts
customer_spend = merged.groupby(['customer_id', 'name'])['total_amount'].sum().reset_index()

# Sort by total amount spent in descending order and get top 5 customers
top_customers = customer_spend.sort_values(by='total_amount', ascending=False).head(5)

print(top_customers);
data = {
    'customer_id': [1, 1, 1, 2, 2, 3, 3, 3],
    'album_id': [101, 101, 101, 102, 102, 103, 103, 103],
    'track_id': [1, 2, 3, 1, 2, 1, 2, 3],
    'purchase_date': ['2025-06-01', '2025-06-02', '2025-06-03', '2025-06-01', '2025-06-02', '2025-06-01', '2025-06-02', '2025-06-03']
}

purchases = pd.DataFrame(data)
total_tracks_per_album = purchases.groupby('album_id')['track_id'].nunique()
tracks_purchased_per_customer = purchases.groupby(['customer_id', 'album_id'])['track_id'].nunique()
purchase_comparison = pd.merge(tracks_purchased_per_customer, total_tracks_per_album, on='album_id', suffixes=('_purchased', '_total'))

purchase_comparison['purchase_type'] = purchase_comparison.apply(
    lambda row: 'Full Album' if row['track_id_purchased'] == row['track_id_total'] else 'Individual Tracks',
    axis=1
)
purchase_counts = purchase_comparison['purchase_type'].value_counts(normalize=True) * 100
print(purchase_counts)
