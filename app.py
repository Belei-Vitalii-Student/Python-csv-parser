import pandas as pd

df = pd.read_csv('GoogleApps.csv')

print("First app:", df['App'].iloc[0])
print("Last app category:", df['Category'].iloc[-1])
print("Column number:", len(df.columns))
print("Average app size:", df['Size'].mean())
print("Median app size:", df['Size'].median())

max_reviews_app = df.loc[df['Reviews'].idxmax()]
print("The application category with the largest number of reviews:", max_reviews_app['Category'])

expensive_apps = df[(df['Price'] > 20) & (df['Installs'] > 10000)]
print("Average rating for expensive apps with a lot of installs:", expensive_apps['Rating'].mean())

