import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Create the data for the product categories and their quantities in different years
data = {
    'Product Category': ['Fishery and seafood products', 'Vegetable and vegetable products', 'Fruit and fruit products',
                         'Non-chocolate candy and chewing gum', 'Bakery products/dough/mix/icing', 
                         'Spices, flavors, and salts', 'Cheese and cheese products'],
    '1998-2004': [1800, 1300, 900, 700, 600, 500, 400],
    '2005-2013': [2300, 1600, 1200, 900, 800, 700, 600]
}

# Step 2: Create a DataFrame from the data
df = pd.DataFrame(data)

# Step 3: Plotting the horizontal bar chart (barh) for both years' data
df.plot(kind='barh', x='Product Category', figsize=(10, 6), color=['#1f77b4', '#ff7f0e'], width=0.7)

# Step 4: Adding a title and labels to make the chart clear
plt.title('Product Quantity Distribution (1998-2004 vs 2005-2013)')
plt.xlabel('Quantity')
plt.ylabel('Product Category')

# Step 5: Add a legend to show which colors correspond to which year range
plt.legend(title='Year Range')

# Step 6: Display the plot
plt.show()
