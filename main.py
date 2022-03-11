# coding: utf-8

from words import words


# Permet de trouver le mot le plus problème selon les options cités au-dessus
def initSearch(tryedWords, found, inWord):
    print("Initialisation ...")
    potentialWords = list(set(words.get(found[0])))
    letters = list(set(found + inWord))
    letters.remove(".")
    wrd = []
    for word in tryedWords:
        # Supprime les mots qui ont déjà été essayé
        try:
            potentialWords.remove(word)
        except ValueError:
            print(f"Le mot {word} n'existe pas !")
        for letter in letters:
            word = word.replace(letter, "")
        for letter in word:
            wrd.append(letter)
    # Supprime les mots qui n'ont pas les lettes qui sont dans le mot recherché, qui n'ont pas la même longueur ou
    # dont les lettres sont mal positionnées + supprime les mots avec des lettres qui ne sont pas dans le mot recherché
    for potentialWord in potentialWords:
        delete = False
        if len(wrd) > 0:
            for letter in wrd:
                if potentialWord.find(letter) != -1:
                    potentialWords.remove(potentialWord)
                    delete = True
                    break
            if delete:
                continue
        print(len(found), " ", len(potentialWord))
        if len(found) != len(potentialWord):
            print("Supr")
            potentialWords.remove(potentialWord)
            continue
        print("end")
        for letter in letters:
            if potentialWord.find(letter) == -1:
                potentialWords.remove(potentialWord)
                delete = True
                break
        if delete:
            continue
        for i in range(len(found) - 1):
            if found[i] == ".":
                continue
            if potentialWord[i] != found[i]:
                potentialWords.remove(potentialWord)
                break
    return potentialWords


# Permet de demander à l'utilisateur l'avancer de la recherche
def ask():
    found = "."
    while found.startswith("."):
        found = input("Indiquez les lettres trouvées (en rouge) exemple : M..US.O. où les points représentent les"
                      " lettres non trouvées >> ")
        if found.startswith("."):
            print("Il manque la première lettre !")
    founds = found.lower().replace(" ", "")
    found = []
    for letter in founds:
        found.append(letter)
    inWord = input("Indiquez les lettres en jaune (séparées par des virgules) >> ").lower().replace(" ", "").split(",")
    return found, inWord


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
    lettersFound, lettersInWord = ask()
    print(initSearch(wordsTryedList, lettersFound, lettersInWord))
