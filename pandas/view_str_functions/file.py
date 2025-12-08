# import pandas as pd

# # df = pd.DataFrame([
# #     [1,   2,   None, 4,   5],
# #     [6,   None, 8,   9,   10],
# #     [11,  12,  13,   None, 15],
# #     [16,  17,  18,   19,  None],
# #     [None, 22, 23,   24,  25],
# #     [26,  27, None, 29,  30],
# #     [31,  32, 33,   None, 35],
# #     [36,  None, 38, 39,  40],
# #     [41,  42, None, 44, 45],
# #     [46,  47, 48,  49,  None],
# #     [None, 52, 53, 54, 55],
# #     [56,  None, 58, 59, 60],
# #     [61,  62, 63, None, 65],
# #     [66,  67, None, 69, 70],
# #     [71, None, 73, 74, 75],
# #     [76,  77, 78, 79, None],
# #     [None, 82, 83, 84, 85],
# #     [86,  None, 88, 89, 90],
# #     [91,  92, 93, None, 95],
# #     [96,  97, 98, 99, None]
# # ], columns=["A", "B", "C", "D", "E"])

# # print(df)

# # print(df.shape) # df module shape class
# # print(df.info()) # df module info() class
# # print(df.columns) # df mpodule columns class
# # print(df.describe()) # to get all description about all columns as min, max, avg values etc..
# # print(df.head(1)) # used to get first rows from datfarame
# # print(df.tail(1)) # used to get last rows from dataframe


# # str functions data cleaning  :-- str column



# import pandas as pd

# df = pd.DataFrame([
#     ["AMZ001", "     Echo Dot 5th Gen", "Electronics", 3999, 4.4],
#     ["AMZ002", "FIRETVSTCIK    ", "Electronics", None, 4.3],
#     ["AMZ003", "Amazon Basics KEYBOARD", "    Computer Accessories", 799, None],
#     ["AMZ004", "Noise Smartwatch", "Wearables", 1499, 4.2],
#     [None, "    Boat Airdopes 141     ", "Headphones", 999, 4.1],
#     ["AMZ006", "Samsung 25W Charger", "Mobiles", None, 4.5],
#     ["AMZ007", "HP Wired Mouse", "Computer Accessories", 499, 4.0],
#     ["AMZ008", None, "Electronics", 899, 3.9],
#     ["AMZ009", "Mi Power Bank", "Mobiles", None, 4.4],
#     ["      AMZ010      ", "OnePlus Bullets Wireless", "Headphones", 1999, None],
#     [None, "             logitech Keyboard", "Computer Accessories", 1299, 4.6],
#     ["AMZ012", None, "wearables", 2499, 4.1],
#     ["AMZ013", "Amazon Tripod", "Camera Accessories", 599, None],
#     ["AMZ014", "Canon DSLR Bag", "          Camera Accessories     ", None, 4.4],
#     ["AMZ015", None, "Electronics", 2999, 4.7],
#     ["AMZ016", "Redmi Earbuds", "Headphones", 1399, None],
#     [None, "             Acer Monitor 21.5 inch", "Electronics", 7999, 4.5],
#     ["AMZ018", None, "Mobiles", 12999, 4.6],
#     ["AMZ019", "JBL Bluetooth Speaker", "Audio           ", None, 4.4],
#     ["AMZ020", "        Sandisk 64GB Pendrive", "Computer Accessories", 549, None]
# ], columns=["ProductID", "Name", "Category", "Price", "Rating"])

# # print(df)
# df["ProductID"]=df["ProductID"].str.strip().str.lower()
# df["Name"]=df["Name"].str.strip().str.lower()
# df["Category"]=df["Category"].str.strip().str.upper() # COMPUTER ACCESSORIES


# df["Category"]=df["Category"].str.replace("Computer Accessories","cmpter acsrs",case=False)

# #contains 
# print(df["Category"].str.contains("Mobiles",case=False))
# #replace
# # df["ProductID"]=df["ProductID"].str.replace("None","amz000")
# # print(df)



import pandas as pd

df = pd.DataFrame([
    [101, "Ravi Kumar", "IT", 55000, 3],
    [102, "Neha Sharma", "HR", None, 4],
    [103, "Vamsi Krishna", "Finance", 48000, None],
    [104, "Roja Reddy", "IT", 62000, 5],
    [105, None, "Marketing", 45000, 2],
    [106, "Anil Varma", "Operations", None, 6],
    [107, "Sathwik Rao", "IT", 52000, 2],
    [108, "Priya Devi", None, 47000, 3],
    [109, "Sneha Patil", "Finance", None, 4],
    [110, "Teja Kumar", "IT", 65000, None],
    [None, "Kiran Reddy", "HR", 38000, 1],
    [112, None, "Marketing", 53000, 5],
    [113, "Suresh Babu", "Operations", None, 7],
    [114, "Samatha Devi", "IT", 49000, None],
    [115, None, "Finance", 46000, 2],
    [116, "Madhu Sudhan", "HR", 58000, None],
    [None, "Varun Sai", "IT", 70000, 8],
    [118, None, "Operations", 54000, 4],
    [119, "Nikhil Raj", "Finance", None, 1],
    [120, "Bindu Latha", "Marketing", 50000, None]
], columns=["EmpID", "Name", "Department", "Salary", "Experience"])

# print(df)


# filteration / selecting methods 
# df["col"] # to select a single column 

# print(df[["Name","Salary"]])
# df[["col1","col2"]] # to slect multiple columns

# df.loc[row_label,col_label] # we can select partcilar row with particlar column
# print(df.loc[5,"Name"])
# print(df.loc[5])
# df.loc[conditions]
# df["Salary"] >=55000
print(df.loc[((df["Department"]=="IT") | (df["Department"]=="Finance") ) & (df["Salary"]>=45000)],["Name","Salary"])

# df.query[]
# df.iloc[]
# a=df.iloc[[1,4,10,19],[1,3]]
# # print(a)
# a["Name"]=a["Name"].str.lower()
# print(a)
