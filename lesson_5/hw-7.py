import json


def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)


companies_info = {}

with open('text_7.txt', 'r', encoding='utf-8') as file:
    for line in file:
        name, _, income, outcome = line.split()
        income, outcome = int(income), int(outcome)
        companies_info[name] = income - outcome

average_profit = {'average_profit': mean([num for num in companies_info.values() if num > 0])}

result = [companies_info, average_profit]

with open('text_7.json', 'w', encoding='utf-8') as file:
    json.dump(result, file, ensure_ascii=False)
