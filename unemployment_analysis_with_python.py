
"""# Task
Analyze the unemployment rate in India using the data from "/content/Unemployment in India.csv".

## Load the data

### Subtask:
Load the dataset "Unemployment in India.csv" into a pandas DataFrame.

**Reasoning**:
Import the pandas library and load the dataset into a pandas DataFrame.
"""

import pandas as pd

df = pd.read_csv('/content/Unemployment in India.csv')

"""**Reasoning**:
Display the first few rows of the DataFrame to verify successful loading.


"""

display(df.head())

"""## Explore the data

### Subtask:
Display the first few rows and check the data types and missing values.

**Reasoning**:
Display the first few rows, data types, and missing values of the dataframe.
"""

display(df.head())
display(df.info())
display(df.isnull().sum())

"""## Analyze the unemployment rate

### Subtask:
Calculate and visualize the overall unemployment rate and its trend over time.

**Reasoning**:
I will start by cleaning the data. The first step is to drop the rows with missing values as they are consistent across all columns and only represent a small portion of the data. Next, I will convert the 'Date' column to datetime objects to enable time-series analysis. Finally, I will calculate the overall mean unemployment rate and plot the unemployment rate over time to visualize the trend. This single code block will complete all the instructions for the given subtask.
"""

df.dropna(inplace=True)
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
overall_unemployment_rate = df['Estimated Unemployment Rate (%)'].mean()
print(f"Overall Estimated Unemployment Rate: {overall_unemployment_rate:.2f}%")

import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('seaborn-whitegrid')
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='Date', y='Estimated Unemployment Rate (%)')
plt.title('Trend of Estimated Unemployment Rate in India Over Time')
plt.xlabel('Date')
plt.ylabel('Estimated Unemployment Rate (%)')
plt.show()

"""**Reasoning**:
The previous command failed because of a KeyError: 'Date'. This indicates that the column name is not exactly 'Date'. I need to check the column names to identify the correct date column name and then retry the conversion to datetime objects and subsequent steps.


"""

display(df.columns)

"""**Reasoning**:
The previous output showed that the column name for the date is ' Date' with a leading space. I will correct the column name, convert it to datetime objects, and then proceed with calculating the overall unemployment rate and plotting the trend as originally planned.


"""

df.rename(columns={' Date': 'Date'}, inplace=True)
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
overall_unemployment_rate = df['Estimated Unemployment Rate (%)'].mean()
print(f"Overall Estimated Unemployment Rate: {overall_unemployment_rate:.2f}%")

import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('seaborn-whitegrid')
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='Date', y='Estimated Unemployment Rate (%)')
plt.title('Trend of Estimated Unemployment Rate in India Over Time')
plt.xlabel('Date')
plt.ylabel('Estimated Unemployment Rate (%)')
plt.show()

"""**Reasoning**:
The previous command failed with a KeyError: 'Estimated Unemployment Rate (%)'. Similar to the 'Date' column, this indicates a potential issue with the column name. I need to inspect the column names again to find the correct name for the unemployment rate column and then proceed with the analysis and visualization.


"""

display(df.columns)

"""**Reasoning**:
The previous output shows that the column name ' Estimated Unemployment Rate (%)' also has a leading space. I will rename this column to remove the leading space and then proceed with calculating the mean unemployment rate and plotting the time trend, which are the remaining steps to complete the subtask.


"""

df.rename(columns={' Estimated Unemployment Rate (%)': 'Estimated Unemployment Rate (%)'}, inplace=True)
overall_unemployment_rate = df['Estimated Unemployment Rate (%)'].mean()
print(f"Overall Estimated Unemployment Rate: {overall_unemployment_rate:.2f}%")

import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('seaborn-whitegrid')
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='Date', y='Estimated Unemployment Rate (%)')
plt.title('Trend of Estimated Unemployment Rate in India Over Time')
plt.xlabel('Date')
plt.ylabel('Estimated Unemployment Rate (%)')
plt.show()

"""**Reasoning**:
The previous command failed because the style 'seaborn-whitegrid' was not found. I will try a different valid matplotlib style to generate the plot and complete the remaining steps of the subtask.


"""

plt.style.use('ggplot')
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='Date', y='Estimated Unemployment Rate (%)')
plt.title('Trend of Estimated Unemployment Rate in India Over Time')
plt.xlabel('Date')
plt.ylabel('Estimated Unemployment Rate (%)')
plt.show()

"""## Analyze regional unemployment

### Subtask:
Analyze and visualize the unemployment rate across different regions or states.

**Reasoning**:
Calculate the mean estimated unemployment rate for each region, sort the results, and then create a bar plot to visualize the average unemployment rate by region.
"""

import matplotlib.pyplot as plt
import seaborn as sns

# Calculate the mean estimated unemployment rate for each region
average_unemployment_by_region = df.groupby('Region')['Estimated Unemployment Rate (%)'].mean().sort_values(ascending=False)

# Create a bar plot
plt.figure(figsize=(15, 8))
sns.barplot(x=average_unemployment_by_region.index, y=average_unemployment_by_region.values, palette='viridis')

# Add titles and labels
plt.title('Average Estimated Unemployment Rate by Region in India', fontsize=16)
plt.xlabel('Region', fontsize=12)
plt.ylabel('Average Estimated Unemployment Rate (%)', fontsize=12)

# Rotate x-axis labels for readability
plt.xticks(rotation=90)

# Display the plot
plt.tight_layout()
plt.show()

"""## Analyze unemployment by different factors

### Subtask:
Explore the unemployment rate based on other factors like gender, age group, etc., if available in the dataset.

**Reasoning**:
Identify relevant columns, group by these columns, calculate the mean unemployment rate, and display the result.
"""

# Identify columns that can be used for analysis by factors
# Based on df.info() and df.head(), 'Area' is a potential factor.
# There are no explicit columns for gender or age group in the dataset.

# Group by 'Area' and calculate the mean of 'Estimated Unemployment Rate (%)'
average_unemployment_by_area = df.groupby('Area')['Estimated Unemployment Rate (%)'].mean()

# Print the resulting mean unemployment rates for each group
print("Average Estimated Unemployment Rate (%) by Area:")
print(average_unemployment_by_area)

"""## Summarize findings

### Subtask:
Provide a summary of the key insights and observations from the analysis.

**Reasoning**:
Synthesize the key findings from the previous analysis steps into a concise summary, highlighting the overall trend, regional differences, and urban vs. rural disparities.
"""

print("Key Insights and Observations from Unemployment Analysis in India:")
print("-" * 60)

# Overall trend
print("\nOverall Unemployment Trend:")
print("The analysis of the time series data showed fluctuations in the estimated unemployment rate over time.")
print("There were noticeable peaks and dips, indicating the dynamic nature of the job market during the observed period.")
print(f"The overall average estimated unemployment rate across India during this period was approximately {df['Estimated Unemployment Rate (%)'].mean():.2f}%.")

# Regional differences
print("\nRegional Unemployment Rates:")
print("Unemployment rates varied significantly across different regions of India.")
print(f"Regions with the highest average unemployment rates include: {average_unemployment_by_region.head(3).to_dict()}")
print(f"Regions with the lowest average unemployment rates include: {average_unemployment_by_region.tail(3).to_dict()}")
print("This suggests that regional economic conditions and employment opportunities differ considerably.")

# Urban vs. Rural
print("\nUrban vs. Rural Unemployment:")
print("There was a clear difference in unemployment rates between urban and rural areas.")
print(f"The average estimated unemployment rate in rural areas was approximately {average_unemployment_by_area['Rural']:.2f}%.")
print(f"The average estimated unemployment rate in urban areas was approximately {average_unemployment_by_area['Urban']:.2f}%.")
print("Urban areas generally experienced a higher average unemployment rate compared to rural areas based on this dataset.")

print("\nSummary:")
print("In summary, the analysis revealed that unemployment in India is influenced by both temporal trends and geographical factors. There are significant disparities in unemployment rates across different regions and between urban and rural areas.")

"""## Summary:

### Data Analysis Key Findings

*   The overall average estimated unemployment rate across India during the observed period was approximately 11.79%.
*   Unemployment rates varied significantly across different regions of India. Tripura, Haryana, and Jharkhand had the highest average unemployment rates, while Assam, Odisha, and Meghalaya had the lowest.
*   Urban areas generally experienced a higher average unemployment rate (approximately 13.17%) compared to rural areas (approximately 10.32%) based on this dataset.

### Insights or Next Steps

*   Further analysis could explore the factors contributing to the significant regional disparities in unemployment rates.
*   Investigating the reasons for the higher unemployment rate in urban areas compared to rural areas could provide valuable insights for policy interventions.

"""
