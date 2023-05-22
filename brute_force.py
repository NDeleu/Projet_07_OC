from itertools import combinations
import csv
import sys
import time

def default_list():
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
    return list_test

def open_data_20(cd_data):
    list_test = []

    print(cd_data)
    with open(cd_data) as fichier_csv:

        reader = csv.reader(fichier_csv, delimiter=",")
        next(reader)

        i = 0
        for ligne in reader:
            if i < 20:
                if float(ligne[1]) > 0 and 0 < float(ligne[2]) <= 100:
                    el_dict = {"name": ligne[0],
                               "amount": float(ligne[1]),
                               "benefice": (float(ligne[1]) * float(ligne[2])) / 100}
                    list_test.append(el_dict)
                    i += 1

    return list_test

def open_data_all(args):
    list_test = []

    for cd_data in args:
        print(cd_data)
        with open(cd_data) as fichier_csv:

            reader = csv.reader(fichier_csv, delimiter=",")
            next(reader)

            for ligne in reader:
                if float(ligne[1]) > 0 and 0 < float(ligne[2]) <= 100:
                    el_dict = {"name": ligne[0],
                               "amount": float(ligne[1]),
                               "benefice": (float(ligne[1]) * float(ligne[2])) / 100}
                    list_test.append(el_dict)
    return list_test

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
        value_count += i["benefice"]
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
    brute_force_rep = gener_best_comb(gener_good_list(value_limit, gener_list_combinaison(list_test)))

    print("\nNom de l action | Cout de l action | Profit en valeur calculee de l action")
    for el in brute_force_rep[2]:
        print(f"{el['name']} | {el['amount']} | {el['benefice']}")
    print(f"\nTotal du cout des actions: {brute_force_rep[1]} euro \nTotal du profit calcules des actions: {brute_force_rep[0]} euro")

def test_arg_one(el_tested):
    try:
        int(el_tested)
    except ValueError:
        return False
    return True

def test_input(input_tested):
    try:
        int(input_tested)
    except ValueError:
        return False
    return True

def input_enter_func():
    input_enter = input("Saisissez 1 si vous désirez les 20 premières données\nSaisissez 2 si vous désirez l'ensemble des données [Déconseillé en brute force]\n")
    if test_input(input_enter) is False:
        print("Veillez saisir un entier , 1 ou 2\nExemple :\n1")
        input_enter_func()
    else:
        return int(input_enter)

exemple_chemin = "C:\\Users\\ndele\\PycharmProjects\\Projet_07_OC\\docs\\dataset1_Python+P7.csv"

if len(sys.argv) == 1:
    print(f"Merci de renseigner au minimum un entier qui est le plafond du coût des actions a la suite de l'appel de l'algorithme. \nExemple :\npython brute_force.py 500\nL'algorithme s'effectura alors sur le tableau test\nIl vous est possible de renseigner d'autres data en renseignant les chemins d acces des fichiers data\nExemple\npython brute_force.py 500 chemindacces1\nVous pouvez aussi cumuler plusieurs fichiers data\nExemple\npython brute_force.py 500 chemindacces1 chemindacces2\nExemples de chemin d acces:\n{exemple_chemin}")
else:
    if test_arg_one(sys.argv[1]) is True:
        value_limit = int(sys.argv[1])
        if len(sys.argv) == 2:
            start_time = time.time()
            brute_force(value_limit, default_list())
            end_time = time.time()
            print("Temps d'execution : ", end_time-start_time)
        else:
            list_args = []
            input_selected = input_enter_func()
            for i in sys.argv:
                if i == sys.argv[0]:
                    pass
                elif i == sys.argv[1]:
                    pass
                else:
                    list_args.append(i)
            if input_selected == 1:
                start_time = time.time()
                brute_force(value_limit, open_data_20(list_args[0]))
                end_time = time.time()
                print("Temps d'execution : ", end_time - start_time)
            elif input_selected == 2:
                start_time = time.time()
                brute_force(value_limit, open_data_all(list_args))
                end_time = time.time()
                print("Temps d'execution : ", end_time - start_time)
    else:
        print("Merci de renseigner un entier pour le plafond du coût des actions comme premier argument. \nExemple :\npython brute_force.py 500")

