# coding: utf-8

from words import words


# Permet de trouver le mot le plus problème selon les options cités au-dessus
def initSearch(letterFound, wordList = words):
    print("Initialisation ...")
    potentialWords = list(set(wordList.get(letterFound[0])))
    return potentialWords


# Permet de demander à l'utilisateur l'avancer de la recherche
def ask(isInit = False):
    foundLetters = "."
    letterInWord = ""
    # Après l'initialisation de la recherche
    if not isInit:
        isFound = input("Le mot a t-il été trouvé ? (yes or no (y or n))").lower()
        if isFound.startswith("y"):
            return True, foundLetters, letterInWord

    while foundLetters.startswith("."):
        foundLetters = input(
            "Indiquez les lettres trouvées (en rouge) exemple : M..US.O. où les points représentent les"
            " lettres non trouvées >> ")
        if foundLetters.startswith("."):
            print("Il manque la première lettre !")
    founds = foundLetters.lower().replace(" ", "")
    foundLetters = []
    for letter in founds:
        foundLetters.append(letter)
    letterInWord = input("Indiquez les lettres en jaune (séparées par des virgules) >> ").lower().replace(" ",
                                                                                                          "").split(",")
    return False, foundLetters, letterInWord


# Fait la recherche du mot
def processSearch(potentialWords, tryedWords, letterFound, letterInWord):
    potentialWords = list(potentialWords)
    # Liste des lettres présentes dans le mot
    letters = list(set(letterFound + letterInWord))
    letters.remove(".")
    wordLetter = []
    # Pour chaque mot essayer
    for word in tryedWords:
        # Supprime les mots qui ont déjà été essayé et énumère les lettres invalides
        try:
            potentialWords.remove(word)
        except ValueError:
            print(f"Le mot {word} n'existe pas !")
        for letter in letters:
            word = word.replace(letter, "")
        for caract in word:
            wordLetter.append(caract)
    # Supprime les mots qui n'ont pas les lettes qui sont dans le mot recherché, qui n'ont pas la même longueur ou
    # dont les lettres sont mal positionnées + supprime les mots avec des lettres qui ne sont pas dans le mot recherché
    potentialWordsBis = potentialWords.copy()
    for potentialWord in potentialWordsBis:
        delete = False
        if len(wordLetter) > 0:
            for letter in wordLetter:
                if potentialWord.find(letter) != -1:
                    potentialWords.remove(potentialWord)
                    delete = True
                    break
            if delete:
                continue
        if len(letterFound) != len(potentialWord):
            potentialWords.remove(potentialWord)
            continue
        for letter in letters:
            if potentialWord.find(letter) == -1:
                potentialWords.remove(potentialWord)
                delete = True
                break
        if delete:
            continue
        for i in range(len(letterFound) - 1):
            print(i)
            if letterFound[i] == ".":
                continue
            if potentialWord[i] != letterFound[i]:
                potentialWords.remove(potentialWord)
                break
    print(len(potentialWords))
    potentialWords.sort()
    print(potentialWords)
    return potentialWords


# Execution de la procedure pour trouver le mot
if __name__ == '__main__':
    print("   _____          __               __________        __   \n",
          "  /     \\   _____/  |_ __ __  _____\\______   \\ _____/  |_ \n",
          " /  \\ /  \\ /  _ \\   __\\  |  \\/  ___/|    |  _//  _ \\   __\\\n",
          "/    Y    (  <_> )  | |  |  /\\___ \\ |    |   (  <_> )  |  \n",
          "\\____|__  /\\____/|__| |____//____  >|______  /\\____/|__|  \n",
          "        \\/                       \\/        \\/             \nby SomGrap\n")
    print("MotusBot, le bot qui trouve les mots pour vous !\n")
    wordsTryedList = input("Indiquez les mots que vous avez essayé (si vous avez essayez plusieurs mot, les séparés par"
                           " des virgules) >> ").lower().replace(" ", "").split(",")
    found, lettersFound, lettersInWord = ask(True)
    wordsList = initSearch(lettersFound)
    while not found:
        wordsList = processSearch(wordsList, wordsTryedList, lettersFound, lettersInWord)
        found, lettersFound, lettersInWord = ask()
