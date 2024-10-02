import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
# Assuming data.csv has columns "Location - Crop" and "Pesticide Amount"
data = pd.read_csv("C:\\Users\\labh\\Desktop\\New folder (2)\\data.csv")
plt.barh(data["Location - Crop"], data["Pesticide Amount"])
plt.xlabel("Pesticide Amount (mg/kg)")
plt.ylabel("Location - Crop")
plt.title("Pesticide Residue by Location and Crop")
plt.show()
