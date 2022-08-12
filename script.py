import random

#le nombre a deviner
nombre_m = random.randint(0, 50)
#le nombre d'essais
num_try = 5


for i in range(5):
    devine = input("Devine le nombre : ")

    #input sera automatiquement en str donc je converti en int
    if devine.isdigit():
        devine = int(devine)
    #et si l'utilisateur entre autre chose qu'un nombre je renvoi au debut de la boucle
    else :
        print("Veuillez entrer un nombre valide.")
        continue

#check les deux nombre (l'input et le nombre générer aléatoirement)
    if devine == nombre_m:
        print(f"Bravo ! Le nombre mystère était bien {nombre_m} !")
        break

    else:
        #input != nombre_m ---> un essai en moin
        if devine > nombre_m :
            print(f"Le nombre mysrère est plus petit que {devine}")
        else :
            print(f"Le nombre mysrère est plus grand que {devine}")
        num_try -= 1

        #check si il reste encore des essai a l'utilisateur 
        if num_try == 0:
            print(f"Dommage ! Le nombre mystère était {nombre_m}")
            break
        else:
            print(f"il vous reste {num_try} essais")

#Sortie de la boucle : Fin
print("Fin du jeu")
