import numpy as np
import pandas as pd 

arr=np.arange(0,35).reshape(7,5)

df=pd.DataFrame( arr, columns="VAL1 VAL2 VAL3 VAL4 VAL5".split())
print(df)


print(df[["VAL1"]])    # return the data as a dataframe
print("\nreturn as a series\n",df["VAL1"]) # return as a series 



print(df[["VAL1"]] < 20)    # conditional statements with the boolean values

print(df[df[["VAL1"]] < 20])    # conditional statements with the actual values

# df["VAL6"] = df["VAL3"] + df["VAL2"]



# df["VAL7"]=np.arange(40, 47)
# print(df)