import mysql.connector as mysql

class General:
    def __init__(self, host, user, password, database):
        try:
            self.connection = mysql.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
            self.cursor = self.connection.cursor()
            print("Connexion à la base de données réussie !")
        except mysql.Error as err:
            print(f"Erreur de connexion à la base de données : {err}")

    def ajouter_client(self, ID, Nom, Prenom, sexe):
        try:
            # Ajout du client à la base de données
            requete = "INSERT INTO client (Id_client, Nom, Prenom, sexe) VALUES (%s, %s, %s, %s)"
            valeurs = (ID, Nom, Prenom, sexe)
            self.cursor.execute(requete, valeurs)
            self.connection.commit()
            print("Client ajouté avec succès !")
        except mysql.Error as err:
            print(f"Erreur lors de l'ajout du client : {err}")
        except ValueError as val_err:
            print(f"Erreur de valeur invalide : {val_err}")

    def afficher_clients(self):
        try:
            # Récupération de la liste des clients depuis la base de données
            requete = "SELECT * FROM client"
            self.cursor.execute(requete)
            rows = self.cursor.fetchall()
            if not rows:
                print("Aucun client à afficher.")
            else:
                print("Liste des clients :")
                for client in rows:
                    print(client)
        except mysql.Error as err:
            print(f"Erreur lors de l'affichage des clients : {err}")

    def supprimer_client(self, ID):
        try:
        # Vérification de l'existence du client
            if not self.client_existe(ID):
                print("L'ID du client à supprimer n'existe pas.")
            return
        # Suppression du client de la base de données
            requete = "DELETE FROM client WHERE Id_client = %s"
            valeurs = (ID,)
            self.cursor.execute(requete, valeurs)
            self.connection.commit()
            print("Client supprimé avec succès !")
        except mysql.Error as err:
            print(f"Erreur lors de la suppression du client : {err}")


    def modifier_client(self, ID, Nouvel_ID, Nouveau_Nom, Nouveau_Prenom, nouveau_sexe):
        try:
            # Vérification de l'existence du client
            if not self.client_existe(ID):
                print("Le client avec cet ID n'existe pas.")
                return

            # Le client existe, procéder à la modification
            requete = "UPDATE client SET Id_client = %s, Nom = %s, Prenom = %s, sexe = %s WHERE Id_client = %s"
            valeurs = (Nouvel_ID, Nouveau_Nom, Nouveau_Prenom, nouveau_sexe, ID)
            self.cursor.execute(requete, valeurs)
            self.connection.commit()
            print("Client modifié avec succès !")
        except mysql.Error as err:
            print(f"Erreur lors de la modification du client : {err}")

    def client_existe(self, ID):
        try:
            # Vérification de l'existence du client dans la base de données
            requete_verif = "SELECT * FROM client WHERE Id_client = %s"
            self.cursor.execute(requete_verif, (ID,))
            row = self.cursor.fetchone()
            return row is not None  # Si row est non vide, cela signifie que le client existe
        except mysql.Error as err:
            print(f"Erreur lors de la vérification de l'existence du client : {err}")
            return False

    def __del__(self):
        self.cursor.close()
        self.connection.close()
