# coding: utf-8

from wordDictionary import *

wordsDictionary = {}


# Permet d'afficher les options possibles au lancement du bot
def motusMenu():
    global wordsDictionary

    while True:
        os.system("cls")

        askMenu = int(input("| 1 - Trouver un mot\n| 2 - Mettre à jour le dictionnaire de mot\n| 3 - Quitter\nEntrer le"
                            " numéro de l'option qui vous intéresse : ")) | 0
        match askMenu:
            case 1:
                isFound, wordsTryedList, lettersFound, lettersInWord = ask(True)
                wordsList = initSearch(lettersFound, wordsDictionary)
                while not isFound:
                    wordsList = processSearch(wordsList, wordsTryedList, lettersFound, lettersInWord)
                    if len(wordsList) == 1:
                        print(f"Le mot est {wordsList[0]} !")
                    elif len(wordsList) == 0:
                        print("Le mot n'a pas été trouvé ! :(")
                        os.system("pause")
                        break
                    else:
                        testWord = calculateWordsScore(wordsList)
                        print(f"Essayer le mot {testWord} !")
                    found, wordsTryedList, lettersFound, lettersInWord = ask()
            case 2:
                print("Mise à jour du dictionnaire de mots...")
                wordsDictionary = updateDictionary()
            case 3:
                exit()
            case _:
                print("La valeur entrée est invalide !")


# Permet de trouver le mot le plus problème selon les options cités au-dessus
def initSearch(letterFound, words):
    print("Initialisation de la recherche ...")
    potentialWords = list(set(words.get(letterFound[0])))
    return potentialWords


# Permet de demander à l'utilisateur l'avancer de la recherche
def ask(isInit = False):
    foundLetters = "."
    lettersInWord = ""
    tryedWords = [""]

    # Après l'initialisation de la recherche
    if not isInit:
        isFoundAsk = input("Le mot a t-il été trouvé ? (yes or no)").lower()
        if isFoundAsk.startswith("y"):
            return True, tryedWords, foundLetters, lettersInWord

    tryedWords = input(
        "\nIndiquez le(s) mot(s) que vous avez essayé (séparez les mots par des virgules) >> ").lower().replace(" ",
                                                                                                                "")\
        .split(",")
    isInvalide = True
    while isInvalide:
        foundLetters = input(
            "Indiquez les lettres trouvées (en rouge) exemple : M..US.O. où les points représentent les"
            " lettres non trouvées >> ").replace(" ", "").lower()

        if foundLetters.startswith(".") or foundLetters == "" or (
                len(foundLetters) != len(tryedWords[0]) and len(tryedWords[0]) != 0):
            print("La valeur est invalide !")
        else:
            isInvalide = False

    lettersInWord = input("Indiquez les lettres en jaune (séparées par des virgules) >> ").lower().replace(" ",
                                                                                                           "").split(
        ",")
    return False, tryedWords, list(foundLetters), lettersInWord


# Fait la recherche du mot
def processSearch(potentialWords, tryedWords, lettersFound, lettersInWord):
    # Liste des lettres présentes dans le mot avec les points
    letters = list(lettersFound + lettersInWord)
    uniqueLetters = list(set(letters))
    uniqueLetters.remove(".")

    invalidLetters = []

    # Pour chaque mot on essaye
    for word in tryedWords:
        # Supprime les mots qui ont déjà été essayé et énumère les lettres invalides
        try:
            potentialWords.remove(word)
        except ValueError:
            print(f"Le mot {word} n'existe pas !")

        for uniqueLetter in uniqueLetters:
            word = word.replace(uniqueLetter, "")

        invalidLetters += list(set(list(word)))

    # Supprime les mots qui n'ont pas les lettres qui sont dans le mot recherché, qui n'ont pas la même longueur ou
    # dont les lettres sont mal positionnées + supprime les mots avec des lettres qui ne sont pas dans le mot recherché
    potentialWordsResult = []
    for potentialWord in potentialWords:
        toAdd = True

        for letter in invalidLetters:
            if potentialWord.find(letter) != -1:
                toAdd = False
                break

        if not toAdd:
            continue

        if len(lettersFound) != len(potentialWord):
            continue

        for letter in uniqueLetters:
            if potentialWord.find(letter) == -1:
                toAdd = False
                break

            if lettersFound.count(letter) != 0 and lettersInWord.count(letter) != 0:
                letterNb = lettersFound.count(letter) + 1
                if list(potentialWord).count(letter) != letterNb:
                    toAdd = False
                    break

        if not toAdd:
            continue

        for letterFound, letterWord in zip(lettersFound, potentialWord):
            if letterFound == ".":
                continue
            if letterWord != letterFound:
                toAdd = False
                break

        if toAdd:
            potentialWordsResult.append(potentialWord)

    potentialWordsResult.sort()
    return potentialWordsResult


# Permet d'associer un score à chaque mot et de ressortir le mot le plus intéréssant
def calculateWordsScore(wordsList):
    ranking = {}
    # Classement en fonction du nombre de lettre différente dans le mot et du score de chaque lettre
    for word in wordsList:
        ranking.setdefault(word, 0)
        for letter in word:
            ranking[word] += lettersRanking[letter] + (100 / word.count(letter))

    rankingBis = sorted(ranking.items(), key=lambda x: x[1], reverse=True)
    result = str(rankingBis[0]).split(",")
    resultBis = result[0].replace("'", "").replace('"', "").replace("(", "")
    return resultBis


# Execution de la procedure pour trouver le mot
if __name__ == '__main__':
    print("   _____          __               __________        __   \n",
          "  /     \\   _____/  |_ __ __  _____\\______   \\ _____/  |_ \n",
          " /  \\ /  \\ /  _ \\   __\\  |  \\/  ___/|    |  _//  _ \\   __\\\n",
          "/    Y    (  <_> )  | |  |  /\\___ \\ |    |   (  <_> )  |  \n",
          "\\____|__  /\\____/|__| |____//____  >|______  /\\____/|__|  \n",
          "        \\/                       \\/        \\/             \nby SomGrap\n")
    print("MotusBot, le bot qui trouve les mots pour vous !\n")
    print("Recherche du dictionnaire...")
    if not os.path.exists("./words.txt"):
        print("Le fichier du dictionnaire de mots n'a pas été trouvé !\nGénération du dictionnaire...")
        wordsDictionary = updateDictionary()
    else:
        print("Le fichier du dictionnaire de mots trouvé !\nMise à jour du dictionnaire...")
        wordsDictionary = synchronizeDictionary()
        print("Dictionnaire mit à jour !")

    print("Génération du classement des lettres en fonction du dictionnaire de mots...")
    doLetterRanking(wordsDictionary)
    print("Classement généré.")

    os.system("pause")

    motusMenu()
