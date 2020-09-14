import json

dict_prof = {}
dict_aver = {}
with open('text7.txt', 'r', encoding='UTF-8') as txt:
    count = 0
    suma = 0
    for line in txt:
        name, ownership, income, costs = line.split()
        profit = int(income) - int(costs)
        dict_prof[name] = profit
        suma += profit
        count += 1
    dict_aver['average_profit'] = suma/count
lists = [dict_prof, dict_aver]
with open("text7.json", "w") as txt:
    json.dump(lists, txt)
