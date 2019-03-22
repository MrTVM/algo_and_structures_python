"""
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""

import collections

def by_profit(company):
    return company.profit


Company = collections.namedtuple('Company', 'name profit')

companies =[]
n = int(input('Введите количесво предприятий: '))
net_profit = 0
for i in range(n):
    name_company = input('Введите наименование предприятия: ')
    profits = {}
    year_profit = 0
    for j in range(1, 5):
        text = 'Введите прибыль за {} квартал:'.format(j)
        profit = float(input(text))
        profits[j] = profit
        year_profit += profit
    companies.append(Company(name_company, year_profit))
    net_profit += year_profit

companies = sorted(companies, key = by_profit, reverse = True)
print(companies)
avg_profits = net_profit / n
print(avg_profits)

separator = True
for comp in companies:
    if comp.profit > avg_profits:
        if separator == True:
            print('---Компании с годовой прибылью выше средней---')
            separator = False
        print('Компания: {}, Прибыль: {}'.format(comp.name, comp.profit))
    else:
        if separator == False:
            print('---Компании с годовой прибылью ниже средней---')
            separator = True
        print('Компания: {}, Прибыль: {}'.format(comp.name, comp.profit))





