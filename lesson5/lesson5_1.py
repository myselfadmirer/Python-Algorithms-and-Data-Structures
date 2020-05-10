# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для каждого
# предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести
# наименования предприятий, чья прибыль выше среднего и ниже среднего.


from collections import namedtuple, OrderedDict

# Использование в решении и namedtuple, и OrderedDict не было необходимым, но очень хотелось попробовать поработать с
# несколькими объектами модуля collections одновременно.

n = int(input('Введтите количество предприятий:\n'))
Company = namedtuple('Company', 'name, profit')
company_list = []
sum_prof = 0
companies = OrderedDict()

while len(company_list) < n:
    name = input('Наименование:\n')
    while True:
        profit = input('Прибыль предприятия за 4 квартала:\n')
        try:
            profit = float(profit)
        except ValueError as e:
            print('Данные по прибыли введены неверно:', e)
            continue
        else:
            break
    company_info = Company(name, profit)
    company_list.append(company_info)
    companies[name] = profit
    sum_prof += profit

# company_list - Массив с карточками предприятий. Можно посмотреть, что даже при таком вводе с использованием
# временных переменных, в массив сохраняется именно namedtuple, а не просто кортеж. При желании можно раскомментировать
# строчку ниже:
# print(f'Массив с карточками предприятий{company_list}')

av_profit = sum_prof / n
print(f'Средняя прибыль: {av_profit}')

print(
    '\n'.join(
        [
            f"Компании, прибыль которых выше средней: "
            f"{', '.join([key for key, value in companies.items() if value >= av_profit])}.\n"
            f"Компании, прибыль которых ниже средней: "
            f"{', '.join([key for key, value in companies.items() if value < av_profit])}."
        ]))
