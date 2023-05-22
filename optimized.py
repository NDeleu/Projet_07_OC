import csv
import sys
import time

def default_list():
    list_test = [{"name": "Action-1", "amount": int((float(20)) * 100), "benefice": float(0.25)},
                 {"name": "Action-2", "amount": int((float(30)) * 100), "benefice": float(3)},
                 {"name": "Action-3", "amount": int((float(50)) * 100), "benefice": float(7.5)},
                 {"name": "Action-4", "amount": int((float(70)) * 100), "benefice": float(14)},
                 {"name": "Action-5", "amount": int((float(60)) * 100), "benefice": float(10.2)},
                 {"name": "Action-6", "amount": int((float(80)) * 100), "benefice": float(20)},
                 {"name": "Action-7", "amount": int((float(22)) * 100), "benefice": float(1.54)},
                 {"name": "Action-8", "amount": int((float(26)) * 100), "benefice": float(2.86)},
                 {"name": "Action-9", "amount": int((float(48)) * 100), "benefice": float(6.24)},
                 {"name": "Action-10", "amount": int((float(34)) * 100), "benefice": float(9.18)},
                 {"name": "Action-11", "amount": int((float(42)) * 100), "benefice": float(7.14)},
                 {"name": "Action-12", "amount": int((float(110)) * 100), "benefice": float(9.90)},
                 {"name": "Action-13", "amount": int((float(38)) * 100), "benefice": float(8.74)},
                 {"name": "Action-14", "amount": int((float(14)) * 100), "benefice": float(0.14)},
                 {"name": "Action-15", "amount": int((float(18)) * 100), "benefice": float(0.54)},
                 {"name": "Action-16", "amount": int((float(8)) * 100), "benefice": float(0.64)},
                 {"name": "Action-17", "amount": int((float(4)) * 100), "benefice": float(0.48)},
                 {"name": "Action-18", "amount": int((float(10)) * 100), "benefice": float(1.4)},
                 {"name": "Action-19", "amount": int((float(24)) * 100), "benefice": float(5.04)},
                 {"name": "Action-20", "amount": int((float(114)) * 100), "benefice": float(20.52)}
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
                               "amount": int((float(ligne[1])) * 100),
                               "benefice": (float(ligne[1]) * float(ligne[2])) / 100}
                    list_test.append(el_dict)
                    i += 1

    return list_test

def open_data_all(args):
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

def optimized(value_limit, list_test):
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
    input_enter = input(
        "Saisissez 1 si vous désirez les 20 premières données\nSaisissez 2 si vous désirez l'ensemble des données\n")
    if test_input(input_enter) is False:
        print("Veillez saisir un entier , 1 ou 2\nExemple :\n1")
        input_enter_func()
    else:
        return int(input_enter)

exemple_chemin = "C:\\Users\\ndele\\PycharmProjects\\Projet_07_OC\\docs\\dataset1_Python+P7.csv"

if len(sys.argv) == 1:
    print(f"Merci de renseigner au minimum un entier qui est le plafond du coût des actions a la suite de l'appel de l'algorithme. \nExemple :\npython optimized.py 500\nL'algorithme s'effectura alors sur le tableau test\nIl vous est possible de renseigner d'autres data en renseignant les chemins d acces des fichiers data\nExemple\npython optimized.py 500 chemindacces1\nVous pouvez aussi cumuler plusieurs fichiers data\nExemple\npython optimized.py 500 chemindacces1 chemindacces2\nExemples de chemin d acces:\n{exemple_chemin}")
else:
    if test_arg_one(sys.argv[1]) is True:
        value_limit = int(sys.argv[1])
        if len(sys.argv) == 2:
            start_time = time.time()
            optimized(value_limit, default_list())
            end_time = time.time()
            print("Temps d'execution : ", end_time - start_time)
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
                optimized(value_limit, open_data_20(list_args[0]))
                end_time = time.time()
                print("Temps d'execution : ", end_time - start_time)
            elif input_selected == 2:
                start_time = time.time()
                optimized(value_limit, open_data_all(list_args))
                end_time = time.time()
                print("Temps d'execution : ", end_time - start_time)
    else:
        print(
            "Merci de renseigner un entier pour le plafond du coût des actions comme premier argument. \nExemple :\npython optimized.py 500")

