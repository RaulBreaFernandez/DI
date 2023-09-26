import random

#Lista con las posibilidades

posibilidades = ["piedra", "papel", "tijera"]
games = 0
wonGames = 0

while games < 5:
    
    playerPlay = input("Elige tu jugada(piedra, papel o tijera): ")
  
    while playerPlay != "piedra" and playerPlay != "papel" and playerPlay != "tijera":
        print("Porfavor eligue bien.")
        playerPlay = input("Elige tu jugada(piedra, papel o tijera): ")

    #Con el método random "elegimos" la jugada de la ia
    
    iaPlay = random.choice(posibilidades)

    #Comprobamos todos los posibles resultados y hacemos recuento de partidas totales y victorias del usuario

    if iaPlay == playerPlay:
        print("- Empate, no se cuenta la jugada")

    elif iaPlay == "piedra" and playerPlay == "tijera":

        print("Has perdido, piedra gana a tijera")
        games += 1
    
    elif iaPlay == "tijera" and playerPlay == "papel":

        print("- Has perdido, tijera gana a papel")
        games += 1

    elif iaPlay == "papel" and playerPlay == "piedra":

        print("- Has perdido, papel gana a piedra")
        games += 1

    elif iaPlay == "piedra" and playerPlay == "papel":

        print("Has ganado, papel gana a piedra")
        games += 1
        wonGames += 1

    elif iaPlay == "tijera" and playerPlay == "piedra":

        print("- Has ganado, piedra gana a tijera")
        games += 1
        wonGames += 1
    
    elif iaPlay == "papel" and playerPlay == "tijera":

        print("- Has ganado, tijera gana a papel")
        games += 1
        wonGames += 1

print("El juego ha acabado.")

#Comprobación del resultado
if wonGames >= 3:

    print("Enhorabuena, has ganado con un total de "+str(wonGames)+" rondas de 5 rondas totales")

else:

    print("Lo siento, has perdido con un total de "+str(wonGames)+" rondas de 5 rondas totales")