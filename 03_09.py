from functools import reduce

employees = [{
    'name': 'Jane',
    'salary': 90000,
    'job_title': 'developer'
}, {
    'name': 'Bill',
    'salary': 50000,
    'job_title': 'writer'
}, {
    'name': 'Kathy',
    'salary': 120000,
    'job_title': 'executive'
}, {
    'name': 'Anna',
    'salary': 100000,
    'job_title': 'developer'
}, {
    'name': 'Dennis',
    'salary': 95000,
    'job_title': 'developer'
}, {
    'name': 'Albert',
    'salary': 70000,
    'job_title': 'marketing specialist'
}]

def is_developer(employee):
    return employee['job_title'] == 'developer'

def is_not_developer(employee):
    return employee['job_title'] != 'developer'

def get_salary(employee):
    return employee['salary']

developer_salaries = [get_salary(x) for x in employees if is_developer(x)]
non_developer_salaries = [get_salary(x) for x in employees if is_not_developer(x)]

def get_sum(acc, x):
    return acc + x

total_developer_salaries = reduce(get_sum, developer_salaries)
average_developer_salary = total_developer_salaries / len(developer_salaries)

total_non_developer_salaries = reduce(get_sum, non_developer_salaries)
average_non_developer_salary = total_non_developer_salaries / len(non_developer_salaries)

print(average_developer_salary)
print(average_non_developer_salary)