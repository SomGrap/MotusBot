# coding: utf-8

import requests
import os


lettersRanking = {}


# Permet de mettre à jour le dictionnaire de mots
def updateDictionary():
    dictionary = sortWords(doWebRequests())
    print("Dictionnaire généré !")
    doSaving = input("Enregistrer le dictionnaire de mot pour les prochaines session ? (yes or no) : ").lower()
    if doSaving.startswith("y"):
        saveDictionary(dictionary)
    elif doSaving.startswith("n"):
        pass
    else:
        print("La valeur entrée est invalide, le dictionnaire n'est donc pas sauvegardé !")

    return dictionary


# Renvoi les mots du site sutom
def doWebRequests():
    print("- Récupération du dictionnaire de mots de sutom.nocle.fr...")
    webData = requests.get("https://framagit.org/JonathanMM/sutom/-/raw/main/data/mots.txt")
    webDataLines = webData.text.splitlines()
    print(f"- {len(webDataLines)} mots trouvées !")
    return webDataLines


# Permet de trier les mots selon les paramètres choisie
def sortWords(words):

    list(words).sort()
    wordsResult = {}
    minWordLength = 6
    maxWordLength = 9
    authorizedLetters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                         "t", "u", "v", "w", "x", "y", "z"]

    isAnswered = False
    while not isAnswered:
        choice = int(input(f"\nParamètres du triage du dictionnaire de mots\n| 1 - Longueur minimum du mot"
                           f" ({minWordLength})\n| 2 - Longueur maximum du mot ({maxWordLength})\n| 3 - Liste"
                           f" des caractères autorisés\n| 4 - Valider les paramètres\n| 5 - Quitter\nEntrer le numéro"
                           f" du paramètre qui vous intéresse : ")) | 0

        match choice:
            case 1:
                minWordLength = int(input("Entrer la longueur minimum du mot : ")) | 6
                if minWordLength > maxWordLength:
                    print("Attention le nombre de lettre minimum est supérieur au nombre de lettre maximum !")
                print("Valeur modifiée")
            case 2:
                maxWordLength = int(input("Entrer la longueur maximum du mot : ")) | 9
                if minWordLength > maxWordLength:
                    print("Attention le nombre de lettre maximum est inférieur au nombre de lettre minimum !")
                print("Valeur modifiée")
            case 3:
                letterString = ""
                for authorizedLetter in authorizedLetters:
                    letterString += f" {authorizedLetter}"
                print(f"Liste actuelle des caractères autorisés >> {letterString}")
                newAuthorizedLetter = input("Entrer un caractère à bannir (laisser vide pour annuler) : ")
                if authorizedLetters.count(newAuthorizedLetter) > 0:
                    print("Ce caractère est déjà dans la liste !")
                else:
                    authorizedLetters.append(newAuthorizedLetter)
                    print("Caractère ajouté à la liste !")
            case 4:
                isAnswered = True
            case 5:
                print("Attention le dictionnaire de mots est vide !")
                return wordsResult
            case _:
                print("La valeur entrée est invalide !")

    for letter in authorizedLetters:
        wordsResult.setdefault(letter, [])
        lettersRanking.setdefault(letter, 0)

    print("- Lancement du trie !")
    wordNb = 0
    for word in words:
        word = word.lower()
        if len(word) < minWordLength or len(word) > maxWordLength:
            continue

        skip = False
        for letter in word:
            if authorizedLetters.count(letter) == 0:
                skip = True
                break

        if skip:
            continue

        wordsResult[word[0]].append(word)
        wordNb += 1

    print(f"- Le dictionnaire contient maintenant {wordNb} mots !")
    return wordsResult


# Permet de sauvegarder le dictionnaire de mots
def saveDictionary(dictionary):
    if not os.path.exists("./words.txt"):
        open("./words.txt", "x").close()

    with open("./words.txt", "w") as wordsFile:
        for letter, wordList in dictionary.items():
            for word in wordList:
                wordsFile.write(word + "\n")


# Permet de mettre à jour le dictionnaire de mots si le fichier words.txt existe
def synchronizeDictionary():
    with open("./words.txt", "r") as wordsFile:
        words = wordsFile.readlines()

    wordsDictionary = {}

    for word in words:
        word = word.replace("\n", "")
        wordsDictionary.setdefault(word[0], [])
        lettersRanking.setdefault(word[0], 0)
        wordsDictionary[word[0]].append(word)

    return wordsDictionary


# Permet de calculer le nombre de lettre pour chaque mot dans le dictionnaire et ainsi faire un classement
def doLetterRanking(dictionary):
    global lettersRanking

    for letter, words in dictionary.items():
        for word in words:
            for ltr in word:
                lettersRanking[ltr] += 1

    lettersRankingBis = sorted(lettersRanking.items(), key=lambda x: x[1], reverse=True)
    score = 27
    for key, value in lettersRankingBis:
        lettersRanking[key] = score
        score -= 1

    return lettersRanking
