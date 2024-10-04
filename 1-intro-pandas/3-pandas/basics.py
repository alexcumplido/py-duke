
# Reflection Questions
# What real-world data could you model with a DataFrame?
# How are DataFrame columns similar to variables in Python?
# When would you use iloc vs loc for selecting data?
# What are some DataFrame creation options you can use?
# How might DataFrame indexes improve performance?

# Challenge Exercises
# Create a DataFrame for storing weather data
# Select a row from mid-point using iloc
# Filter rows matching certain numeric criteria with loc
# Load a CSV file into a DataFrame
# Set the index to another column like datesa

import pandas as pd
import random

# Create an empty pandas DataFrame
data = {
    "Name": ["John", "Anna", "Peter", "Linda"],
    "Age": [23, 36, 29, 45],
    "Score": [90, 85, 88, 75]
}

df = pd.DataFrame(data)
# print(df)

# Create a  Dataframe from dictionary, list or lists
data = [["carl", 30, 124], ["Carlos", 22, 100] ,["Car", 43, 14]]
df = pd.DataFrame(data, columns=["name", "age", "score"])
# print(df)

# Dataframe from a  file
file_path = "../../files/USCG.Search.Rescue.Stats.csv"
df_csv = pd.read_csv(file_path)

# print( df_csv.head(10), df_csv.tail(5),  df_csv.describe())

# Selecting columns
# print(df_csv[['Cases', 'Sorties']])

# Selecting rows
# print(df_csv.iloc[3])

# Selecting a range of rows
# print(df_csv.iloc[10:15])

# Select a column range of rows
# print(df_csv.iloc[20:40, 3])

# Selecting by label name
# print(df_csv.loc[1992])

# Selecting by range label name
# print(df_csv.loc[1992:2000])

# Selecting by range label name and column
# print(df_csv.loc[1992:2000, ['Cases', 'Sorties']])

# Selecting data using boolean mask
mask = [False for _ in range(len(df_csv))]
mask[3:7] = [True] * 4
# print(df_csv[mask])

# Create mask using comparision opeartors
mask_csv = df_csv.loc[:,'Lives Lost After CG Notification'] < df_csv.loc[:,'Lives Lost Before CG Notification']
# print(df_csv[mask_csv])

# Using Pandas boolean operations
boolean_mask = (df_csv.loc[:, 'Cases'] < 60000) & (df_csv.loc[:, 'Sorties'] > 45000)
# print(df_csv[boolean_mask])

# Creating new columns
new_columm = df_csv.loc[:,'Saved per Sortie'] = df_csv.loc[:,'Lives Saved'] / df_csv.loc[:,'Sorties']
# print(df_csv['Saved per Sortie'])


"""LAB: Looking at DataFrames Data"""

colors = ["Red", "Green", "Blue"]
num_rows = 100

df = pd.DataFrame({
    'color': [colors[random.randint(0,2)] for _ in range(num_rows)],
    'integers': [random.randint(0,15) for _ in range(num_rows)],
    'floats': [random.random() for _ in range(num_rows)]
})


#Use the DataFrame head() method to view the top five rows. Try giving it a number as an argument to control how many rows are displayed.

# print(df.head(5))

#View summary statistics using the DataFrame describe() method.

# print(df.describe())

# If you change the argument to include='all', it will display statistics for all columns in the data frame, inserting NaN (not a number) when the data type is not appropriate for the statistic. Try viewing statistics for all frames using describe().

# print(df.describe(include='all'))

# You can select a column using bracket syntax very similar to that used with dictionaries. Put the column name, as a string, in brackets after the DataFrame name. Try this with the column 'color'

# print(df['color'])

#Try selecting the columns 'color' and 'floats' by supplying them as a list of strings in the same bracket syntax.

# print(df[['color', 'floats']])

#Now let's try the .loc[] syntax. It also uses bracket syntax, but in this case you will specify both rows and columns to select. Select all of the rows by supplying a lone colon as the first argument, and the column 'color' by supplying it as a second argument (remember that arguments must be separted by a comma).

# print(df.loc[:,'color'])

# Now specify a slice, 10:13, for the first argument and a list of columns, ['color', 'integers'], as a second, to select four rows (the upper bound in loc[] is included) and two columns.

# print(df.loc[10:13, ['color', 'integers']])

#Now try the iloc[] syntax. This used the position of rows and columns to determine selection. In this DataFrame, the labels for the rows are the same as their position, so we can use the same slice 10:13 as the first argument. For the second, use the slice 0:2 to select the first two columns. Notice that with iloc[], the upper bound is not inclusive, so you will get three rows and two columns.

print(df.iloc[10:13, 0:2])


""""LAB: Selecting DataFrame data"""

# # Create a mask named 'red_mask' with True for all rows where the color is equal to 'Red'. Remember that the equals operator is a double equals ==.

red_mask = df.loc[:,'color'] == 'Red'
print(red_mask)

# New create a DataFrame named 'red_df' by using the mask with the data frame df. You can use the mask in the simple bracket syntax to filter the DataFrame.

red_df = df[red_mask]
print(red_df)

# Columns have a method, .unique(), which will return all unique values in that column. Call this method on the red_df.color to confirm that it only contians 'Red' values.

check_red = red_df.color.unique()
print(check_red)

#Now use the not operator, ~, in combination with red_mask, to create a new DataFrame named 'no_red'. Simply put ~ in front of the mask to negate it. Check the values of no_red.color using the .unique() method to confirm that there are no 'Red' values.

no_red = df[~red_mask]
print(no_red.color.unique())

# Create a new mask named 'three_mask' for all rows where integers is less than three
three_mask = df.loc[:,'integers'] <= 3

#Create a new DataFrame named 'mixed_df' containing only rows whose color is 'Red' and whose integer value is equal or less than 3 by using the 'and' operator, `&` between that masks. 

mixed_df = df[red_mask & three_mask]
print(mixed_df.color.unique())
print(mixed_df.integers.unique())

