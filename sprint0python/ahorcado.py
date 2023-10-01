import random

#Lista de las palabras ordenadas por dificultad

words = {

    "facil": ["casa", "agua", "azul"],
    "normal": ["garaje", "cabeza", "guardia"],
    "dificil" : ["curiosidad", "paracaidas", "coagulacion"]

}

def chooseAWord(difficulty):

    return random.choice(words[difficulty])

#El juego en sí mismo

def startGame():

    print("Bienvenido al ahorcado")
    print("Facil")
    print("Normal")
    print("Dificil")
    difficulty = input("Elige la dificultad\n")

    if difficulty not in words:

        print("Elige una dificultad válida")
        startGame()
        return
    
    word = chooseAWord(difficulty)
    guessedWord = ["_" for _ in word]
    maxTries = 6
    tries = 0
    triedLetters = []

    print("Comienza el juego!")
    showGameStatus(guessedWord, tries, triedLetters)
    
    while tries < 6:

        letter = input("\nEscribe una letra ")

        if len(letter) != 1 or not letter.isalpha():

            print("\nEscribe solo una letra")
            continue
        
        if letter in triedLetters:

            print("\nYa has escrito esa letra antes")
            continue

        triedLetters.append(letter)

        if letter in word:

            for i in range(len(word)):

                if word[i] == letter:

                    guessedWord[i] = letter
        
        else:

            tries += 1

        
        showGameStatus(guessedWord, tries, triedLetters)

        if "".join(guessedWord) == word:

            print("Enhorabuena, has ganado!")

        elif tries == maxTries:

            print(f"Lo siento, has perdido! La palabra era: {word}")

        
    playAgain()

#Función que muestra el estado de la partida

def showGameStatus(guessedWord, tries, triedLetters):

    actualStatus = " ".join(guessedWord)
    print(f"Palabra actual: {actualStatus}")
    print(f"Intentos restantes: {6 - tries}")
    print(f"Letras intentadas: {', '.join(triedLetters)}")


#Función para preguntarle al usuario si quiere volver a jugar

def playAgain():

    retry = input("¿Quieres volver a jugar? (s/n)").lower()

    if retry == "s":

        tries = 0
        startGame()

    else:

        print("Gracias por jugar!")


startGame()