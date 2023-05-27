## Pandas

# 1. Import the Pandas and Seaborn libraries. 
import pandas as pd
import seaborn as sns

# 2. Include the “titanic” dataset from the Seaborn library to the project. 
data = sns.load_dataset("titanic")

# 3. Print the first and last 8 rows of the data frame. 
data.head(1)
data.tail(8)

# 4. Print the information about the dataset and memory usage. 
data.info()
data.memory_usage()

# 5. Print the column names of the dataset. 
data.columns

# 6. Print the index information of the dataset. 
data.info

# 7. Print the mean value of the rows which include numerical values. 
data["age"].mean()
data["fare"].mean()

# 8. Figure out how many different cities people embarked the ship. 
data["embark_town"].value_counts().count()

# 9. Find the number of males and females on the ship. 
len(data[data["sex"]=="female"])
len(data[data["sex"]=="male"])

# 10. Find the age of the youngest passenger. 
data["age"].min()

# 11. Find the age of the oldest passenger. 
data["age"].max()

# 12. Find the city that the oldest passenger has embarked the ship. 
data.groupby("embark_town")["age"].max().tail(1)

# 13. Create a data frame with the female passengers who are younger than 25. 
data[(data["sex"] == "female") & (data["age"] < 25)]

# 14. Create a data frame with the passengers who are younger than 20 and has embarked  the ship from “Queenstown” or “Southampton” 
data[((data["embark_town"] == "Queenstown") | (data["embark_town"] == "Southampton")) & (data["age"] < 20)]

# 15. Delete the column named “who”. 
data.drop("who",axis=1,inplace=True)

# 16. Create a column that has the result of the “age/fare” formula. 
data["age/fare"] = data["age"]/data["fare"]

# 17. Find the average ages of male and female passengers.
data.groupby("sex")["age"].mean()

# 18. Find the average ticket price that the male and female passengers paid according to  ticket class. 
data.groupby(["class","sex"])["fare"].mean()

# 19. Find the number of male and female passengers that survived according to the ticket  class.
len(data[(data["class"] == "female") & (data["alive"] =="yes")])
