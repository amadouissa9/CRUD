import mysql.connector
from general import General

class MenuPrincipal:
    def __init__(self):
        self.general_instance = General(host="localhost", user="root", password="", database="crud")

    def afficher_menu(self):
        while True:
            print("\n Menu des tâches :")
            print("1. Ajouter un Client")
            print("2. Modifier les informations d'un client ")
            print("3. Afficher les Clients")
            print("4. Supprimer un Client")
            print("5. Quitter le programme")
            choix = input("Entrez votre choix : ")

            if choix == "1":
                ID = input("Entrez le Numéro du Client : ")
                Nom = input("Entrez le nom : ")
                Prenom = input("Entrez le Prenom : ")
                sexe = input("Entrez le sexe : ")
                self.general_instance.ajouter_client(ID, Nom, Prenom, sexe)
            elif choix == "2":
                try:
                    ID = input("Entrez l encien  Numéro du Client à Modifier : ")
                    Nouvel_ID = input("Entrez le Nouveau Numéro du Client : ")
                    Nouveau_Nom = input("Entrez le nouveau nom : ")
                    Nouveau_Prenom = input("Entrez le nouveau Prenom : ")
                    nouveau_sexe = input("Entrez le nouveau sexe : ")
                    self.general_instance.modifier_client(ID, Nouvel_ID, Nouveau_Nom, Nouveau_Prenom, nouveau_sexe)
                except mysql.Error as err:
                    print(f"Erreur lors de la modification du client : {err}")
            elif choix == "3":
                self.general_instance.afficher_clients()
            elif choix == "4":
                ID = input("Entrez le Numéro du Client à Supprimer : ")
                self.general_instance.supprimer_client(ID)
            elif choix == "5":
                print("Au revoir !")
                break
            else:
                print("Choix invalide. Veuillez réessayer SVP!.")

if __name__ == "__main__":
    menu = MenuPrincipal()
    menu.afficher_menu()
