#Final project


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#data needed to create a plot, give data names, age,a nd income
data = {'Name': ['Alice', 'Richard', 'Chan', "Lisa"],
        'Age': [24,20,30,26],
        'Income': [52000, 60000, 75000, 90000]}

#define df to use the data printed above
df = pd.DataFrame(data)

#generate a graph/define x/yaxis, title, and bar color
plt.figure(figsize=(8,5))
plt.bar(df['Name'],df['Income'],color='blue')
plt.title('Income Comparison')
plt.xlabel('Name')
plt.ylabel('Income($)')
plt.show()

#define the average income for the provided data
average_income = np.mean(df['Income'])
message= f"""
Income Summary:
Average Income: ${average_salary:.2f}
Highest Income" ${df['Salary'].max()} (earned by) {df.loc[df['Income'].idxmax(), 'Name']})
"""

print(message)


