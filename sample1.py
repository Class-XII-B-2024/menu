
import matplotlib.pyplot as plt
import pandas as pd
#samples tested
data=pd.read_csv("C://Users//sherin//Desktop//IP project//samples.csv")
df=pd.DataFrame(data)
print(df)

#civil cases on food adulteration
import pandas as pd
import numpy as np
data=pd.read_csv("C://Users//sherin//Desktop//IP project//civil.csv")
df=pd.DataFrame(data)
df = df.replace('NA',np.nan)
print("Civil Cases on Food Adulteration:")
print(df)

#criminal cases on food adulteration
import pandas as pd
import numpy as np
data=pd.read_csv("C://Users//sherin//Desktop//IP project//criminal cases.csv")
df=pd.DataFrame(data)
df = df.replace('NA',np.nan)
print("Criminal Cases on Food Adulteration:")
print(df)
#penalites
data = {'Year': ['2020', '2021', '2022', '2023'],'No_of_samples': [69850, 77530, 91570, 88310],'Percentage_of_non_conforming_samples': [22, 23, 25, 27]}
df = pd.DataFrame(data)
print(df)
data={'No_of_Cases_Launched':[11200, 12670, 15360, 17600],'No_of_Cases_of_Conviction':[2300, 2650, 3010, 4380],'Amount_Raised_by_Penalties_Rs':[146729087, 159834617, 193459153, 239120874]}
df2 = pd.DataFrame(data)
print(df2)

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
#commonly adulterated
slices=[30,24,31,12,3]
Category=['Fruits','Vegetables','Dairy Products','Spices','Other Products']
exp=[0,0,0.2,0,0]
plt.pie(slices,labels=Category,startangle=90,explode=exp,shadow=True,autopct='%.1F%%')
plt.title('Food Adulteration Detection')
plt.legend()
plt.show()
#line
categories = ['2011-12', '2012-13', '2013-14']
values1 = [64593, 69949, 72200]
values2 = [8247, 10380, 13571]
values3 = [6845, 5840, 10235]
x = np.arange(len(categories))
plt.plot(x, values1,label='No.of Samples Examined',color='green',linestyle='dotted',marker='o')
plt.plot(x, values2,label='No.of Samples found Non-Conforming',color='purple',linestyle='dotted',marker='o')
plt.plot(x, values3,label='No.of prosecutions Launched',color='pink',linestyle='dotted',marker='o')
plt.xlabel('Years')
plt.xticks(x, categories)
plt.ylabel('Values')
plt.title('Samples Tested and Found Adulterated')
plt.legend()
plt.show()
#histogram

import matplotlib.pyplot as plt
adulterants = ['Water', 'Urea', 'Starch', 'AR', 'RF', 'Sorbitol', 'Glucose', 'C-Sugar', 'AS', 'Na-Soda', 'S&P', 'V. Oil', 'Formalin', 'H202', 'B-Acid', 'Detergent', 'H.Chlorite']
positive_percentages = [91.0, 27.0, 15.0, 9.0, 24.0, 3.0, 10.0, 31.0, 13.0, 11.0, 19.0, 19.0, 20.0, 15.0, 12.0, 4.0, 5.0]
plt.figure(figsize=(10, 6))  # Adjust figure size as needed
plt.bar(adulterants, positive_percentages,align='edge', color='skyblue',width=1,edgecolor='black')
plt.xlabel('Adulterant')
plt.ylabel('Positive (%)')
plt.title('Percentage of Adulterants used in the foods')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
#highest
import pandas as pd
# Create a Series with the data

import pandas as pd
import matplotlib.pyplot as plt

# Data for highest adulteration rates
data1 = {'Uttar Pradesh': 52.32, 'Tamil Nadu': 45.39, 'Jharkhand': 41.68}

# Data for lowest adulteration rates
data2 = {'Arunachal Pradesh': 3.78, 'Goa': 5.67, 'Uttarakhand': 4.63}

# Create a stacked bar chart directly from the data dictionaries
plt.figure(figsize=(8, 6))  # Set figure size for better visualization
plt.bar(kind='barstacked',data1.keys(), data1.values(), label='Highest Adulteration Rates', color='red')
plt.bar(kind='barstacked',data2.keys(), data2.values(), label='Lowest Adulteration Rates', color='green')
plt.xlabel('State')
plt.ylabel('Adulteration Rate (%)')
plt.title('Adulteration Rates (Highest & Lowest)')
plt.xticks(rotation=45)  # Rotate x-axis labels for readability
plt.legend(title='Data Set')  # Add legend for clarity
plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt
import pandas as pd
data = {
    'States': ["UP", "Punjab", "Tamil Nadu", "Maharashtra", "J&K"],
    'Failed samples': [8375, 3053, 2461, 1532, 992],
    'Samples tested': [19063, 11057, 7383, 9022, 3643],
    'Convictions': [3237, 22, 896, 83, 310]
    }
df = pd.DataFrame(data)
df.plot('States',kind='bar', figsize=(10, 6), color=['pink', 'purple','cyan'], width=0.7)
plt.title('Details about the samples of adulterants Statewise)')
plt.xlabel('States')
plt.ylabel('Samples')
plt.legend()
plt.show()




