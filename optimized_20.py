import csv
"""
list_test = []

with open("docs/dataset1_Python+P7.csv") as fichier_csv:

    reader = csv.reader(fichier_csv, delimiter=",")
    next(reader)

    i = 0
    for ligne in reader:
        if i < 20 and float(ligne[1]) > 0 and 0 < float(ligne[2]) <= 100:
            el_dict = {"name": ligne[0], "amount": int((float(ligne[1]))*100), "benefice": ((float(ligne[1]))*(float(ligne[2]))/100)}
            list_test.append(el_dict)
            i += 1
"""
list_test = [{"name": "Action-1", "amount": 20, "benefice": 0.25},
             {"name": "Action-2", "amount": 30, "benefice": 3},
             {"name": "Action-3", "amount": 50, "benefice": 7.5},
             {"name": "Action-4", "amount": 70, "benefice": 14},
             {"name": "Action-5", "amount": 60, "benefice": 10.2},
             {"name": "Action-6", "amount": 80, "benefice": 20},
             {"name": "Action-7", "amount": 22, "benefice": 1.54},
             {"name": "Action-8", "amount": 26, "benefice": 2.86},
             {"name": "Action-9", "amount": 48, "benefice": 6.24},
             {"name": "Action-10", "amount": 34, "benefice": 9.18},
             {"name": "Action-11", "amount": 42, "benefice": 7.14},
             {"name": "Action-12", "amount": 110, "benefice": 9.90},
             {"name": "Action-13", "amount": 38, "benefice": 8.74},
             {"name": "Action-14", "amount": 14, "benefice": 0.14},
             {"name": "Action-15", "amount": 18, "benefice": 0.54},
             {"name": "Action-16", "amount": 8, "benefice": 0.64},
             {"name": "Action-17", "amount": 4, "benefice": 0.48},
             {"name": "Action-18", "amount": 10, "benefice": 1.4},
             {"name": "Action-19", "amount": 24, "benefice": 5.04},
             {"name": "Action-20", "amount": 114, "benefice": 20.52}
             ]

def gener_matrice(value_limit, list_test):
    matrice = [[0 for x in range(value_limit + 1)] for x in range(len(list_test) + 1)]

    for i in range(1, len(list_test)+1):
        for y in range(1, value_limit+1):
            if list_test[i-1]["amount"] <= y:
                matrice[i][y] = max(list_test[i-1]["benefice"] + matrice[i-1][y-list_test[i-1]["amount"]], matrice[i-1][y])
            else:
                matrice[i][y] = matrice[i-1][y]

    return matrice

def gener_good_list(value_limit, list_test, matrice):
    good_list = []
    n = len(list_test)
    y = value_limit
    cost_action_best_comb = 0

    while y >= 0 and n >= 0:
        el_tested = list_test[n-1]
        if matrice[n][y] == matrice[n-1][y - el_tested["amount"]] + el_tested["benefice"]:
            y -= el_tested["amount"]
            good_list.append(el_tested)
        n -= 1

    for el_good in good_list:
        # el_good["amount"] /= 100
        cost_action_best_comb += el_good["amount"]

    return good_list, cost_action_best_comb

def benef_action_comb(matrice):
    return matrice[-1][-1]

def optimized(value_limit, list_test):
    value_limit_up = value_limit # *100
    matrice = gener_matrice(value_limit_up, list_test)
    good_comp_and_action = gener_good_list(value_limit_up, list_test, matrice)
    best_combinaison = good_comp_and_action[0]
    cost_action_best_comb = good_comp_and_action[1]
    best_benef = benef_action_comb(matrice)

    return best_benef, cost_action_best_comb, best_combinaison

# print(optimized(500, list_test))

"""
with open("docs/Res_optimized_20_tableau", "w") as file:
    brute_force_rep = optimized(500, list_test)
    file.write("Nom de l action | Cout de l action | Profit en pourcentage de l action\n")
    for el in brute_force_rep[2]:
        file.write(f"{el['name']} | {el['amount']} | {el['benefice']}\n")
    file.write(f"\nTotal du cout des actions: {brute_force_rep[1]} euro \nTotal du profit calcules des actions: {brute_force_rep[0]} euro")
"""