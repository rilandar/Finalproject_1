#Final project
#MIT License
"""
Copyright (c)
MIT License

Copyright (c) [2023] [Rasanjali Ilandara Devage]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

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


