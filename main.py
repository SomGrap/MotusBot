from words import words


# Permet de trouver le mot le plus problème selon les options cités au-dessus
def searchWord(letterNb, wordsTryed, lettersFnd, lettersInWrd):
    print("test")


# Execution de la procedure pour trouver le mot
if __name__ == '__main__':
    print("Petite présentation tel un mec qui veut montrer qu'il a des skills alors qu'il connait juste le 'color a'")
    print("   _____          __               __________        __   \n",
          "  /     \\   _____/  |_ __ __  _____\\______   \\ _____/  |_ \n",
          " /  \\ /  \\ /  _ \\   __\\  |  \\/  ___/|    |  _//  _ \\   __\\\n",
          "/    Y    (  <_> )  | |  |  /\\___ \\ |    |   (  <_> )  |  \n",
          "\\____|__  /\\____/|__| |____//____  >|______  /\\____/|__|  \n",
          "        \\/                       \\/        \\/             \n")
    print("MotusBot, le bot qui trouve le mot pour vous !\n")
    letterNumber = 0
    while letterNumber == 0:
        try:
            letterNumber = int(input("Indiquez le nombre de lettre dans le mot >> "))
        except ValueError:
            print("Vous ne pouvez pas entrer du texte ici !")
        if 6 > letterNumber or letterNumber > 9:
            print("Les mots de Motus comporte entre 6 et 9 lettres !")
            letterNumber = 0
    wordsTryedList = input("Indiquez les mots que vous avez essayé (si vous avez essayez plusieurs mot, les séparés par"
                           "des virgules) >> ")
    lettersFound = input("Indiquez les lettres trouvées (en rouge) exemple : ..I.A.Z. >> ")
    lettersInWord = input("Indiquez les lettres présent dans le mot et non citées au-dessus (en jaune) >> ")
    print("Recherche ...")
    searchWord(letterNumber, wordsTryedList, lettersFound, lettersInWord)
