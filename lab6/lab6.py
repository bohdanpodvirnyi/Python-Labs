import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data.csv')

first_ten = data[:10]

first_ten_agency = first_ten['Agency']

details = data[['Agency', 'Business Title', 'Work Location 1']][:10]

count = details['Agency'].value_counts().reset_index(name='counts')

bar1 = count.plot.bar(x='index', y='counts', rot=0)
plt.show()

avg_salary = data[['Salary Range From', 'Salary Range To']][:10].mean(axis=1)


salary = data[['Job Category', 'Work Location']][:10]

salary.loc[:, 'Average Salary'] = avg_salary

salary_by_category = salary[['Job Category', 'Average Salary']].plot.bar(x='Job Category', y='Average Salary')
plt.show()

salary_by_location = salary[['Work Location', 'Average Salary']].plot.bar(x='Work Location', y='Average Salary')
plt.show()