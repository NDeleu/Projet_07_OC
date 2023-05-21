from itertools import combinations
import csv

list_test = []

with open("docs/dataset1_Python+P7.csv") as fichier_csv:

    reader = csv.reader(fichier_csv, delimiter=",")
    next(reader)

    i = 0
    for ligne in reader:
        if i < 20:
            el_dict = {"name": ligne[0], "amount": float(ligne[1]), "benefice": float(ligne[2])}
            list_test.append(el_dict)
            i += 1

def gener_list_combinaison(list_test):
    list_combinaison = []
    for i in range(1, len(list_test)+1):
        combs = combinations(list_test, i)
        list_combinaison.extend(list(combs))
    return list_combinaison


def cost_action_comb(comb):
    value_count = 0
    for i in comb:
        value_count += i["amount"]
    return value_count

def gener_good_list(value_limit, list_combinaison):
    good_list = []
    for comb in list_combinaison:
        if cost_action_comb(comb) <= value_limit:
            good_list.append(comb)
    return good_list

def benef_action_comb(comb):
    value_count = 0
    for i in comb:
        value_count += (i["amount"]*i["benefice"])/100
    return value_count

def gener_best_comb(good_list):
    best_benef = 0
    best_combinaison = []
    cost_action_best_comb = 0
    for comb in good_list:
        if benef_action_comb(comb) > best_benef:
            best_benef = benef_action_comb(comb)
            best_combinaison = list(comb)
    cost_action_best_comb = cost_action_comb(best_combinaison)
    return best_benef, cost_action_best_comb, best_combinaison

def brute_force(value_limit, list_test):
    return gener_best_comb(gener_good_list(value_limit, gener_list_combinaison(list_test)))

print(brute_force(500, list_test))