import numpy as np
import pandas as pd 



# # df=pd.DataFrame({ "VAL1":[2,4,6,np.nan,4,2,1],
# #                   "VAL2":[np.nan,6,7,np.nan,90,88,66],
# #                   "VAL3":["PAK","BAN","IND","AUS","USA","UK","SRI"]})
# # print(df)



# df = pd.DataFrame({
#     "Name": ["Ali", "Ubaid", "Ahmed", "Sara", "Hamza", "Ayesha"],
#     "Age": [20, 21, np.nan, 19, 22, 20],
#     "Marks": [85, 72, 90, np.nan, 65, 88],
#     "City": ["Lahore", "Karachi", "Lahore", "Islamabad", np.nan, "Lahore"]
# }, index=["A", "B", "C", "D", "E", "F"])

# # print(df[["VAL1"]])    # return the data as a dataframe
# # print("\nreturn as a series\n",df["VAL1"]) # return as a series 



# # print(df[["VAL1"]] < 20)    # conditional statements with the boolean values

# # print(df[df[["VAL1"]] < 20])    # conditional statements with the actual values

# # df["VAL6"] = df["VAL3"] + df["VAL2"]



# # df["VAL7"]=np.arange(40, 47 )
# # print(df)

# # print(df.drop(["VAL2","VAL3"],axis=1,inplace=True))  //  delete the columns from the dataframe

# # print(df.drop())  # drop the rows

# # print(df.isnull())

# # print(len(df))

# # print(df.axes)

# # print(df.index)
# # print(df.columns)


# # df["VAL4"]=np.nan
# print(df)

# # print(df.dropna())

# # print(df["VAL3"][0::3])  #create empty values between 0 and 3 , have two positions, after that he will follow that producer, mean 

# # # df["VAL3"][0::3]=np.nan                   # this also make empty 4 and 5 , 
# # df.loc[0::3, "VAL3"] = np.nan 
# # df["VAL3"]=df["VAL3"].fillna("PAK")         
# print(df)

# # print(df[["Name"]])
# # print(df[["Name","Marks"]])
# # print(df.loc["A":"D","Name":"Marks"])
# # print(df[df["Marks"] > 20][["Name","Marks"]])
# # print(df.iloc[3,1])
# # print(df["City"].fillna("Unknowm"))
# # print(df.dropna())
# # print(df.drop(["Name","City"], axis=1))


# # print(df.reset_index(drop=True,inplace=True))
# # #print(df)

# # df["New_Index"]=[12,34,12,11,1,1]

# # df.set_index("New_Index",inplace=True)
# # print(df)



#                                     MULTI-INDEXED DATAFRAME 
inner=["Class A", "Class B","Class C","Class A","Class B","Class C"]
outer=["School 1","School 1","School 1","School 2","School 2","School 2",]

zip(outer,inner)
list(zip(outer,inner))

multi_index=list(zip(outer,inner))
hier_index=pd.MultiIndex.from_tuples(multi_index)
data=np.random.randint(20,30,(6,2))

df=pd.DataFrame(data,hier_index, columns="Semester_1 semester_2".split() )
print(df)


