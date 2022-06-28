import pandas as pd
import sys

csv = sys.argv[1]

df = pd.read_csv(csv)


number_of_orders_total = len(df.index)

quantity_per_product_avg = df.groupby('name').sum() / number_of_orders_total

quantity_per_product_avg.rename(columns = {'quantity':'quantity_avg'}, inplace = True)

most_popular_brands = df.groupby('name').agg({'brand': lambda x: x.mode().iat[0]})

quantity_per_product_avg.to_csv(r'0_output_file_name.csv', encoding='utf-8', index=True)

most_popular_brands.to_csv(r'1_output_file_name.csv', encoding='utf-8', index=True)

#print (quantity_per_product_avg)


#print (most_popular_brands)
