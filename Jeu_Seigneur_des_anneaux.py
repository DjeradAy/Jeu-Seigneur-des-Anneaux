import random

class Personnage:
    def __init__(self, nom, force):
        #attributss  du personnage
        self._nom = nom
        self._vie = 100
        self._force = force
        self._experience = 0
        self._degats = 0
        self.tour = 'joueur1' 

    def frappe(self, cible):
        #attaquer une cible
        force_frappe = random.randint(1, self._force)
        if not cible.esquive():
            cible.recoitDegat(self, force_frappe)

    def esquive(self):
        #déterminer si le personnage esquive l'attaque
        return random.random() < 0.2

    def recoitDegat(self, adversaire, force_frappe):
        #recevoir des dégâts
        self._degats += force_frappe
        self._vie = max(0, self._vie - force_frappe)

    # Getters et Setters pour les attributs
    def get_nom(self):
        return self._nom

    def set_nom(self, nom):
        self._nom = nom

    def get_vie(self):
        return self._vie

    def set_vie(self, vie):
        self._vie = vie

    def get_force(self):
        return self._force

    def set_force(self, force):
        self._force = force

    def get_experience(self):
        return self._experience

    def set_experience(self, experience):
        self._experience = experience

    def get_degats(self):
        return self._degats

    def set_degats(self, degats):
        self._degats = degats

class Magicien(Personnage):
    FORCE_FRAPPE_1 = 10
    FORCE_FRAPPE_2 = 15

    def __init__(self, nom, force):
        super().__init__(nom, force)  # Appel du constructeur de la classe parente

    def lanceUnSort(self, adversaire):
        #lancer un sort sur l'adversaire
        force_frappe = random.randint(1, self.FORCE_FRAPPE_1)
        if not adversaire.esquive():
            adversaire.recoitDegat(self, force_frappe)
            print(self.get_nom(), "lance un sort et inflige", force_frappe, "points de dégâts à", adversaire.get_nom())
        else:
            print(adversaire.get_nom(), "esquive l'attaque de", self.get_nom())

    def lanceUnRayonDeLumièreSombre(self, adversaire):
        #lancer un rayon de lumière sombre sur l'adversaire
        force_frappe = random.randint(1, self.FORCE_FRAPPE_2)
        if not adversaire.esquive():
            adversaire.recoitDegat(self, force_frappe)
            print(self.get_nom(), "lance un rayon de lumière sombre et inflige", force_frappe, "points de dégâts à", adversaire.get_nom())
        else:
            print(adversaire.get_nom(), "esquive l'attaque de", self.get_nom())

    def attaque(self, adversaire):
        #attaque aléatoire
        attaque = random.choice([self.lanceUnSort, self.lanceUnRayonDeLumièreSombre])
        attaque(adversaire)

class RoiSorcier(Personnage):
    FORCE_FRAPPE_1 = 5
    FORCE_FRAPPE_2 = 20

    def __init__(self, nom, force):
        super().__init__(nom, force)  # Appel du constructeur de la classe parente

    def frappeAvecSonEpee(self, adversaire):
        #frapper l'adversaire avec l'épée
        force_frappe = random.randint(1, self.FORCE_FRAPPE_1)
        if not adversaire.esquive():
            adversaire.recoitDegat(self, force_frappe)
            print(self.get_nom(), "frappe avec son épée et inflige", force_frappe, "points de dégâts à", adversaire.get_nom())
        else:
            print(adversaire.get_nom(), "esquive l'attaque de", self.get_nom(), "en se couchant")

    def attaqueAvecSonNazgul(self, adversaire):
        #attaquer l'adversaire avec le Nazgûl
        force_frappe = random.randint(1, self.FORCE_FRAPPE_2)
        if not adversaire.esquive():
            adversaire.recoitDegat(self, force_frappe)
            print(self.get_nom(), "attaque avec son Nazgûl et inflige", force_frappe, "points de dégâts à", adversaire.get_nom())
        else:
            print(adversaire.get_nom(), "esquive l'attaque de", self.get_nom(), "en se baissant")

    def attaque(self, adversaire):
        #attaque aléatoire
        attaque = random.choice([self.frappeAvecSonEpee, self.attaqueAvecSonNazgul])
        attaque(adversaire)

class Combat:
    def demarrerCombat(self, magicien, roiSorcier):
        #démarrer le combat
        print("Le combat entre", magicien.get_nom(), "et", roiSorcier.get_nom(), "va commencer!")
        print("Celui qui alliera puissance, précision et défense gagnera")
        print("Que le meilleur gagne !")

        while magicien.get_vie() > 0 and roiSorcier.get_vie() > 0:
            if magicien.tour == 'joueur1':
                print(magicien.get_nom(), "attaque!")
                magicien.attaque(roiSorcier)
                magicien.set_experience(magicien.get_experience() + 1)
                print(magicien.get_nom(), "a maintenant", magicien.get_experience(), "points d'expérience.")
                print("Il reste", max(0, roiSorcier.get_vie()), "points de vie à", roiSorcier.get_nom())
                magicien.tour = 'joueur2'
            else:
                print(roiSorcier.get_nom(), "attaque!")
                roiSorcier.attaque(magicien)
                roiSorcier.set_experience(roiSorcier.get_experience() + 1)
                print(roiSorcier.get_nom(), "a maintenant", roiSorcier.get_experience(), "points d'expérience.")
                print("Il reste", max(0, magicien.get_vie()), "points de vie à", magicien.get_nom())
                magicien.tour = 'joueur1'

        print("Fin du combat!")
        if magicien.get_vie() <= 0:
            print(roiSorcier.get_nom(), "a vaincu", magicien.get_nom(), "!")
        else:
            print(magicien.get_nom(), "a vaincu", roiSorcier.get_nom(), "!")


# Lancement du code
if __name__ == "__main__":
    magicien = Magicien("Gandalf", 20)
    roi_sorcier = RoiSorcier("Sauron", 30)
    combat = Combat()
    combat.demarrerCombat(magicien, roi_sorcier)
