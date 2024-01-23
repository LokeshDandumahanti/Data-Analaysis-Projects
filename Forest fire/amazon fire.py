import pandas as pd

# Load the dataset
forest_fires_data = pd.read_csv('C:/Users/vijay/OneDrive/Desktop/Forest fire/amazon.csv', encoding = 'latin1')

# Task 1: Display Top 5 Rows of The Dataset
print("Top 5 Rows of The Dataset:")
print(forest_fires_data.head())

# Task 2: Check Last 5 Rows
print("\nLast 5 Rows of The Dataset:")
print(forest_fires_data.tail())

# Task 3: Find Shape of Our Dataset (Number of Rows And Number of Columns)
num_rows, num_columns = forest_fires_data.shape
print(f"\nNumber of Rows: {num_rows}, Number of Columns: {num_columns}")

# Task 4: Getting Information About Our Dataset
print("\nInformation About Our Dataset:")
print(forest_fires_data.info())

# Task 5: Check For Duplicate Data and Drop Them
forest_fires_data.drop_duplicates(inplace=True)
print("\nDuplicate Data Dropped.")

# Task 6: Check Null Values In The Dataset
print("\nNull Values in the Dataset:")
print(forest_fires_data.isnull().sum())

# Task 7: Get Overall Statistics About The Dataframe
print("\nOverall Statistics About The Dataframe:")
print(forest_fires_data.describe())

# Task 8: Rename Month Names To English
month_mapping = {'Janeiro': 'January', 'Fevereiro': 'February', 'Março': 'March', 'Abril': 'April', 'Maio': 'May', 'Junho': 'June',
                 'Julho': 'July', 'Agosto': 'August', 'Setembro': 'September', 'Outubro': 'October', 'Novembro': 'November', 'Dezembro': 'December'}
forest_fires_data['month'] = forest_fires_data['month'].map(month_mapping)

# Task 9: Total Number of Fires Registered
total_fires = forest_fires_data['number'].sum()
print(f"\nTotal Number of Fires Registered: {total_fires}")

# Task 10: In Which Month Maximum Number of Forest Fires Were Reported?
max_fires_month = forest_fires_data.groupby('month')['number'].sum().idxmax()
print(f"\nMonth with Maximum Number of Forest Fires: {max_fires_month}")

# Task 11: In Which Year Maximum Number of Forest Fires Was Reported?
max_fires_year = forest_fires_data.groupby('year')['number'].sum().idxmax()
print(f"\nYear with Maximum Number of Forest Fires: {max_fires_year}")

# Task 12: In Which State Maximum Number of Forest Fires Was Reported?
max_fires_state = forest_fires_data.groupby('state')['number'].sum().idxmax()
print(f"\nState with Maximum Number of Forest Fires: {max_fires_state}")

# Task 13: Find Total Number of Fires Were Reported In Amazonas
total_fires_amazonas = forest_fires_data[forest_fires_data['state'] == 'Amazonas']['number'].sum()
print(f"\nTotal Number of Fires Reported In Amazonas: {total_fires_amazonas}")

# Task 14: Display Number of Fires Were Reported In Amazonas (Year-Wise)
fires_amazonas_yearwise = forest_fires_data[forest_fires_data['state'] == 'Amazonas'].groupby('year')['number'].sum()
print("\nNumber of Fires Reported In Amazonas (Year-Wise):")
print(fires_amazonas_yearwise)

# Task 15: Display Number of Fires Were Reported In Amazonas (Day-Wise)
fires_amazonas_daywise = forest_fires_data[forest_fires_data['state'] == 'Amazonas'].groupby('date')['number'].sum()
print("\nNumber of Fires Reported In Amazonas (Day-Wise):")
print(fires_amazonas_daywise)

# Task 16: Find Total Number of Fires Were Reported In 2015 And Visualize Data Based on Each ‘Month’
fires_2015 = forest_fires_data[forest_fires_data['year'] == 2015]
total_fires_2015 = fires_2015.groupby('month')['number'].sum()
print("\nTotal Number of Fires Reported In 2015 Based on Each Month:")
print(total_fires_2015)

# Task 17: Find Average Number of Fires Were Reported From Highest to Lowest (State-Wise)
average_fires_statewise = forest_fires_data.groupby('state')['number'].mean().sort_values(ascending=False)
print("\nAverage Number of Fires Reported From Highest to Lowest (State-Wise):")
print(average_fires_statewise)

# Task 18: To Find The State Names Where Fires Were Reported In 'dec' Month
december_fires_states = forest_fires_data[forest_fires_data['month'] == 'December']['state'].unique()
print("\nState Names Where Fires Were Reported In 'December':")
print(december_fires_states)
