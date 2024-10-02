#civil cases on food adulteration
import pandas as pd
import numpy as np
data=pd.read_csv("C://Users//sherin//Desktop//IP project//criminal cases.csv")
df=pd.DataFrame(data)
df = df.replace('NA',np.nan)
print(df)
