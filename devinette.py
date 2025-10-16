import random

print("Pense à un chiffre entre 1 et 10 et appuie sur Entrée quand tu es prêt.")
input()

possibles = list(range(1, 10))
trouver = False
essai = random.choice(possibles)
reponse = input(f"Est-ce que ton chiffre est {essai} ? (oui/non) : ").strip().lower()

if reponse == essai:
        print(f"Super ! J'ai deviné que ton chiffre était {essai} ! ")
else:
        print(f"Super! mais non :( !!!!  bug fixed ")

