import csv

"""
En raison de la disposition des livrables, (un fichier.py par algorithme, pas plus)
il m'était impossible de rajouter un document README.txt si je souhaitais respecter 
les consignes du projet 07.
Néanmoins il me tient à coeur de vous proposer une utilisation optimale, et compréhenssible
de mon projet.
Ainsi, en bas de script, vous retrouverez les indications permettant d'executer l'algorithme.
"""

def open_data(args):
    list_test = []

    for cd_data in args:
        with open(cd_data) as fichier_csv:

            reader = csv.reader(fichier_csv, delimiter=",")
            next(reader)

            for ligne in reader:
                if float(ligne[1]) > 0 and 0 < float(ligne[2]) <= 100:
                    el_dict = {"name": ligne[0],
                               "amount": int((float(ligne[1])) * 100),
                               "benefice": ((float(ligne[1])) * (
                                   float(ligne[2])) / 100)}
                    list_test.append(el_dict)
    return list_test

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

def optimized(value_limit, *args):
    list_test = open_data(args)
    value_limit_up = value_limit*100
    matrice = gener_matrice(value_limit_up, list_test)
    good_comp_and_action = gener_good_list(value_limit_up, list_test, matrice)
    best_combinaison = good_comp_and_action[0]
    cost_action_best_comb = good_comp_and_action[1]
    best_benef = benef_action_comb(matrice)

    return best_benef, cost_action_best_comb, best_combinaison

def print_optimized(value_limit, *args):
    list_test = open_data(args)
    value_limit_up = value_limit*100
    matrice = gener_matrice(value_limit_up, list_test)
    good_comp_and_action = gener_good_list(value_limit_up, list_test, matrice)
    best_combinaison = good_comp_and_action[0]
    cost_action_best_comb = good_comp_and_action[1]
    best_benef = benef_action_comb(matrice)

    print("\nNom de l action | Cout de l action | Profit calcule de l action")
    for el in best_combinaison:
        print(f"{el['name']} | {el['amount']} | {el['benefice']}")
    print(f"\nTotal du cout des actions: {cost_action_best_comb} euro \nTotal du profit calcules des actions: {best_benef} euro")


"""
L'algorithme dynamique prend au minimum deux arguments:
    Le coût maximal accordé par le client (dans notre exemple le coût total 
        correspondra aux consigne du projet 7, soit 500).
    Le chemin d'accès au document csv qui renseignera les données pour notre algorithme.
Des exemples de renseignement d'arguments seront proposés en fin d'annotation.

Néanmoins, par soucis de présentation, deux fonctions vous sont proposées :
La première fonction :
optimized(value_limit, *args)
Elle renvoie un tuple, où vous retrouverai :
    en indice 0 : Le bénéfice total calculé de la meilleure combinaison
    en indice 1 : Le coût total de la meilleure combinaison
    en indice 2 : Une liste de dictionnaire des meilleurs combinaisons avec leur nom, leur cout, et leur bénéfice calculé

Le seconde fonction :
print_optimized(value_limit, *args)
Elle affichera en console une présentation des résultats ci dessus.
L'objectif de cette fonction est d'améliorer la lisibilité du résultat de l'algorithme.

Exemple de renseignement d'arguments :

Afficher le résultat de l'algorithme pour les 1 000 actions du dataset1 avec un cout maximal accordé de 500 :
print_optimized(500, "docs/dataset1_Python+P7.csv")

Avoir un retour du résultat de l'algorithme pour les 1 000 actions du dataset2 avec un cout maximal accordé de 500 :
optimized(500, "docs/dataset2_Python+P7.csv")

Afficher le résultat de l'algorithme pour les 2 000 actions du dataset1 et du dataset2 avec un cout maximal accordé de 500 :
print_optimized(500, "docs/dataset1_Python+P7.csv", "docs/dataset2_Python+P7.csv")

note : le chemin d'accès proposé (exemple : "docs/dataset1_Python+P7.csv") est à titre d'exemple, 
il peut changer en fonction de l'emplacement dans lequel vous avez enregistrez votre dataset.

En vous remerciant pour l'intérêt et le temps accordé à mon projet.
"""