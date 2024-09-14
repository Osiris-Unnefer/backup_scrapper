#backup scanning script, The script is functional but not optimized
print("make by    https://github.com/Osiris-Unnefer\n\n\n\n\n\n\n")
import subprocess
#----------------variables------------------
compteur = 1
extension0 =''
extension = '.bak'
extension1 = '.backup'
extension2 = '.old'
extension3 = '.swp'
extension4 = '.~'
extension5 = '.tmp'
erreurs = ["404","unable"]
#-------------changement wordlist-----------
word_list = 'wordlist1.txt' #changeable
remake = input(f"La wordlist choisie est '{word_list}', voulez vous la changer ? (o/n) ->") 
if remake == 'o':
     word_list = input("nouvelle wordlist -> ") #nom de la wordlist / chemin de la wordlist

#---------------choix de l'extension-----------
mode = int(input("\n[1] Uniquement .bak (généralement plus courante)\n[2] Uniquement .backup\n[3] Les deux (plus lent)\n[4] Global (.bak/.backup/.old/.swp/.~/.tmp)\n\nMode chosit -> ")) 
#---------------commandes-----------
url = input('URL -> ')
with open(word_list, 'r') as fichier:
        for ligne in fichier:
            ligne_wordlist = ligne.strip() 
 #-------------------------------------------------.bak-------------------------------
            commande = subprocess.run(["wget", url+ligne_wordlist+extension], capture_output=True, text=True)
            sortie = commande.stdout + commande.stderr
            verification_erreur = any(chaque_erreur in sortie for chaque_erreur in erreurs)

            if mode == 3:
#-------------------------------------------------.backup-------------------------------
                commande1 = subprocess.run(["wget", url+ligne_wordlist+extension1], capture_output=True, text=True)
                sortie1 = commande.stdout + commande.stderr
                verification_erreur1 = any(chaque_erreur in sortie1 for chaque_erreur in erreurs)
                if verification_erreur1:
                    print(f"Essai numéro {compteur} non résultant pour {ligne_wordlist+extension1} ")
                    compteur = compteur + 1
                else: 
                    print(f"==============================================================\nFichier {ligne_wordlist+extension1} a été téléchargé\n==============================================================")
            if mode == 4:
#-------------------------------------------------.backup-------------------------------
                commande1 = subprocess.run(["wget", url+ligne_wordlist+extension1], capture_output=True, text=True)
                sortie1 = commande.stdout + commande.stderr
                verification_erreur1 = any(chaque_erreur in sortie1 for chaque_erreur in erreurs)
                if verification_erreur1:
                    print(f"Essai numéro {compteur} non résultant pour {ligne_wordlist+extension1} ")
                    compteur = compteur + 1
                else: 
                    print(f"==============================================================\nFichier {ligne_wordlist+extension1} a été téléchargé\n==============================================================")
#-------------------------------------------------.old-------------------------------
                commande2 = subprocess.run(["wget", url+ligne_wordlist+extension2], capture_output=True, text=True)
                sortie2 = commande.stdout + commande.stderr
                verification_erreur2 = any(chaque_erreur in sortie2 for chaque_erreur in erreurs)
                if verification_erreur2:
                    print(f"Essai numéro {compteur} non résultant pour {ligne_wordlist+extension2} ")
                    compteur = compteur + 1
                else: 
                    print(f"==============================================================\nFichier {ligne_wordlist+extension2} a été téléchargé\n==============================================================")
#-------------------------------------------------.swp-------------------------------
                commande3 = subprocess.run(["wget", url+ligne_wordlist+extension3], capture_output=True, text=True)
                sortie3 = commande.stdout + commande.stderr
                verification_erreur3 = any(chaque_erreur in sortie3 for chaque_erreur in erreurs)
                if verification_erreur3:
                    print(f"Essai numéro {compteur} non résultant pour {ligne_wordlist+extension3} ")
                    compteur = compteur + 1
                else: 
                    print(f"==============================================================\nFichier {ligne_wordlist+extension3} a été téléchargé\n==============================================================")
#-------------------------------------------------extesion ~-------------------------------

                commande4 = subprocess.run(["wget", url+ligne_wordlist+extension4], capture_output=True, text=True)
                sortie4 = commande.stdout + commande.stderr
                verification_erreur4 = any(chaque_erreur in sortie4 for chaque_erreur in erreurs)
                if verification_erreur4:
                    print(f"Essai numéro {compteur} non résultant pour {ligne_wordlist+extension4} ")
                    compteur = compteur + 1
                else: 
                    print(f"==============================================================\nFichier {ligne_wordlist+extension4} a été téléchargé\n==============================================================")
#-------------------------------------------------tmp-------------------------------
                commande5 = subprocess.run(["wget", url+ligne_wordlist+extension5], capture_output=True, text=True)
                sortie5 = commande.stdout + commande.stderr
                verification_erreur5 = any(chaque_erreur in sortie5 for chaque_erreur in erreurs)
                if verification_erreur5:
                    print(f"Essai numéro {compteur} non résultant pour {ligne_wordlist+extension5} ")
                    compteur = compteur + 1
                else: 
                    print(f"==============================================================\nFichier {ligne_wordlist+extension5} a été téléchargé\n==============================================================")
#-------------------------------------------------.bak-------------------------------
            if verification_erreur:
                print(f"Essai numéro {compteur} non résultant pour {ligne_wordlist+extension} ")
                compteur = compteur + 1
            else: 
                print(f"==============================================================\nFichier {ligne_wordlist+extension} a été téléchargé\n==============================================================")
