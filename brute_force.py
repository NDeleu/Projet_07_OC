from itertools import combinations

"""
En raison de la disposition des livrables, (un fichier.py par algorithme, pas plus)
il m'était impossible de rajouter un document README.txt si je souhaitais respecter 
les consignes du projet 07.
Néanmoins il me tient à coeur de vous proposer une utilisation optimale, et compréhenssible
de mon projet.
Ainsi, en bas de script, vous retrouverez les indications permettant d'executer l'algorithme.
"""

list_test = [{"name": "Action-1", "amount": 20, "benefice": 5},
             {"name": "Action-2", "amount": 30, "benefice": 10},
             {"name": "Action-3", "amount": 50, "benefice": 15},
             {"name": "Action-4", "amount": 70, "benefice": 20},
             {"name": "Action-5", "amount": 60, "benefice": 17},
             {"name": "Action-6", "amount": 80, "benefice": 25},
             {"name": "Action-7", "amount": 22, "benefice": 7},
             {"name": "Action-8", "amount": 26, "benefice": 11},
             {"name": "Action-9", "amount": 48, "benefice": 13},
             {"name": "Action-10", "amount": 34, "benefice": 27},
             {"name": "Action-11", "amount": 42, "benefice": 17},
             {"name": "Action-12", "amount": 110, "benefice": 9},
             {"name": "Action-13", "amount": 38, "benefice": 23},
             {"name": "Action-14", "amount": 14, "benefice": 1},
             {"name": "Action-15", "amount": 18, "benefice": 3},
             {"name": "Action-16", "amount": 8, "benefice": 8},
             {"name": "Action-17", "amount": 4, "benefice": 12},
             {"name": "Action-18", "amount": 10, "benefice": 14},
             {"name": "Action-19", "amount": 24, "benefice": 21},
             {"name": "Action-20", "amount": 114, "benefice": 18}
             ]

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

def gener_good_list(list_combinaison):
    value_limit = 500
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

def brute_force():
    brute_force_rep = gener_best_comb(gener_good_list(gener_list_combinaison(list_test)))
    return brute_force_rep[0], brute_force_rep[1], brute_force_rep[2]

def print_brute_force():
    brute_force_rep = gener_best_comb(gener_good_list(gener_list_combinaison(list_test)))

    print("\nNom de l action | Cout de l action | Profit en pourcentage de l action")
    for el in brute_force_rep[2]:
        print(f"{el['name']} | {el['amount']} | {el['benefice']}")
    print(f"\nTotal du cout des actions: {brute_force_rep[1]} euro \nTotal du profit calcules des actions: {brute_force_rep[0]} euro")

"""
L'algorithme brute force ne prend aucun argument, décision prise relativement à la consigne de la partie 1 du projet 7.

Néanmoins, par soucis de présentation, deux fonctions vous sont proposées :
La première fonction :
brute_force()
Elle renvoie un tuple, où vous retrouverai :
    en indice 0 : Le bénéfice total calculé de la meilleure combinaison
    en indice 1 : Le coût total de la meilleure combinaison
    en indice 2 : Une liste de dictionnaire des meilleurs combinaisons avec leur nom, leur cout, et leur bénéfice en pourcentage
    
Le seconde fonction :
print_brute_force()
Elle affichera en console une présentation des résultats ci dessus.
L'objectif de cette fonction est d'améliorer la lisibilité du résultat de l'algorithme.

En vous remerciant pour l'intérêt et le temps accordé à mon projet.
"""
