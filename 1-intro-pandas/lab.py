import pandas as pd

# Goal

# Explore the relationship between life expectancy and happiness scores across countries.You will merge these datasets to allow exploration of the relationship between these factors. Finally, you will practice your EDA skills by visualizing and analyzing this relationship.

# Steps

# Import libraries
# Load life expectancy and happiness CSV data
# Clean column names in life expectancy dataframe
# Merge the two datasets into a combined dataframe
# Explore correlations
# Create scatterplot with regression line showing relationship between life expectancy and happiness

# Reflection Questions
# What do you notice about the correlation between life expectancy and happiness? Is there a strong relationship?
# Does wealth (GDP per capita) also seem to correlate with happiness? Why might this be?
# Do you see any outliers in the data? Particularly happy or unhappy countries relative to their life expectancy?
# Can you identify the United States on the scatterplot? Where does it lie relative to the regression line?
# What other factors might impact a country's average happiness besides life expectancy?

# Challenge Questions

# Try filtering the dataframe to explore patterns for different regions of the world. Do you notice any trends by region?
# Explore the relationships between other columns (health expenditure per capita, freedom to make life choices, generosity, perception of corruption, etc) and happiness. Do any stand out to you?
# Create a scatterplot matrix to explore multiple relationships visually. Do you notice any interesting patterns?
# Train a simple linear regression model to predict happiness from life expectancy. How accurate is the model? How could it be improved?
# Choose 5 countries and create a bar chart comparing their happiness components side-by-side. How do they differ in terms of supporting factors for happiness?


df_life_expectancy = pd.read_csv('../files/expectancy.csv')
df_happiness = pd.read_csv('../files/happiness-2021.csv')

df_life_happiness = df_happiness.merge(df_life_expectancy)



print(df_life_happiness.head())