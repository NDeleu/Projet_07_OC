import csv

list_test = []

with open("docs/dataset2_Python+P7.csv") as fichier_csv:

    reader = csv.reader(fichier_csv, delimiter=",")
    next(reader)

    for ligne in reader:
        if float(ligne[1]) > 0 and 0 < float(ligne[2]) <= 100:
            el_dict = {"name": ligne[0], "amount": int((float(ligne[1]))*100), "benefice": ((float(ligne[1]))*(float(ligne[2]))/100)}
            list_test.append(el_dict)

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
        el_good["amount"] /= 100
        cost_action_best_comb += el_good["amount"]

    return good_list, cost_action_best_comb

def benef_action_comb(matrice):
    return matrice[-1][-1]

def optimized(value_limit, list_test):
    value_limit_up = value_limit*100
    matrice = gener_matrice(value_limit_up, list_test)
    good_comp_and_action = gener_good_list(value_limit_up, list_test, matrice)
    best_combinaison = good_comp_and_action[0]
    cost_action_best_comb = good_comp_and_action[1]
    best_benef = benef_action_comb(matrice)

    return best_benef, cost_action_best_comb, best_combinaison

print(optimized(500, list_test))