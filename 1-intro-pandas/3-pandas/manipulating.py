# Reflection Questions
# What are some common use cases for filtering DataFrames?
# How can chaining multiple Boolean operators enable more precise data selection?
# When might you use isin() versus repeated equality checks with == ?
# What are benefits of using loc[] over column-wise data access?
# Where might complex Boolean filters become difficult to manage?

# Challenges
# Filter a DataFrame to only show values greater than the mean
# Combine filters to find rows matching multiple Boolean conditions
# Use isin() to filter categorical data like product types
# Slice DataFrame with .loc[] using a Boolean filter
# Chain complex filters with multiple Boolean operators


import pandas as pd

### Manipulating Pandas Dataframe

data = {
    "first": ['Carl', 'Francis', 'Sam'],
    "last": ['Po', 'Nyguen', 'Smith'],
    "age": [32, 45, 22],
    'CH_count':[12,  14, 39]
}


df = pd.DataFrame(data)

# print(df.rename(index={0:'a', 1:'b', 2: 'c'}, inplace=True))
# df.reset_index(index=0, inplace=True)
# df.drop(columns='first_name')
# df.drop(index=0)

# """
# LAB: Manipulating DataFrames
# Rename and create and drop columns
# """

df.rename(columns={"first": 'First', 'last': 'Last', 'age': 'Age'}, inplace=True)
df['Name'] = df['First'] + ' ' + df['Last']
# df.drop(columns=['Name'], inplace=True)
# df.drop(columns=['First', 'Last'])

# Add rows
new_data = {
    'first':['Sue', 'Boya'],
    'last':['Rankler', 'Maple'],
    'age':[93, 12],
    'CH_count':[22, 1]
}
new_clients = pd.DataFrame(new_data)
new_clients.rename(columns={"first": 'First', 'last': 'Last', 'age': 'Age'}, inplace=True)
new_clients['Name'] = new_clients["First"] + ' ' + new_clients['Last']

new_dataframe = pd.concat([df, new_clients])
new_dataframe.reset_index(drop=True, inplace=True)

# Update to specific value

new_dataframe.loc[0:1, 'First'] =  'Alexandre'
new_dataframe.loc[0:1, 'CH_count'] =  -1

print(new_dataframe)

# Update using math operations
new_dataframe['CH_count'] + 1
new_dataframe['CH_count'] += 10

# Update using replace method

print(new_dataframe.replace(49, 500))

# Applying functions to df

even_odd = {
    'even': range(20, 0, - 2),
    'odd': range(1, 21, 2)
}

df_numbers = pd.DataFrame(even_odd)

print(df_numbers.apply(sum))

def hundred_plus(col):
    if sum(col) > 100:
        return 'Greater than 100'
    return 'Not greater than 100'

df_func =  df_numbers.apply(hundred_plus)
print(df_func)

def label(row):
    if row['even'] % 3 == 0:
        return True
    elif row['odd'] % 3 == 0:
        return True
    return False    

df_func_rows = df_numbers.apply(label, axis=1)
print(df_func_rows)

def label_expand(row):
    ret_eval = [False, False]
    if row['even'] > 6: ret_eval[0] = True
    if row['odd'] > 6: ret_eval[1] = True
    return ret_eval

print(df_numbers.apply(label_expand, axis=1))
print(df_numbers.apply(label_expand, axis=1, result_type='expand'))


def fiv_three(row):
    if row %3 == 0:
        return 'Divisible by 3'
    return 'Not divisible by 3'

print(df_numbers['even'].apply(fiv_three))

