from random import randint
def  update_score(score, die_value):
   if die_value == 1:
    return 0
   else:
     return score + die_value
def display_scoreboard(player_score , computer_score):
    print() 
    print("#" * 20)
    print(f"Jugador: {player_score}")
    print(f"Computadora: {computer_score}")
    print(f"#" * 20)
    print()
    
player_score = 0
computer_score = 0

welcome_massage = """
        Bienvenido a "Pig", un juego de dados!
        
En este juego, un usuario y un oponente de la computadora
debera tirar un dado de 6 caras en cada ronda.
Si el valor del dado es un 1, el jugador que saco el 1
pierde todos sus puntos.     
De lo contrario, el jugador obtiende el valor del dado
sumado a sus puntos.        
El primer jugador que alcance los 30 o mas puntos gana!        
"""
print(welcome_massage)
username = input("Cual es su nombre: ")

while True:
    input(f"¡Presiona 'Enter' para tirar el dado: {username}!\n")
    
    player = randint(1 , 6)
    print(f"{username} rueda un: {player}")
    
    computer = randint(1 , 6)
    print(f"Computadora rueda un {computer}")
    
    player_score = update_score(player_score , player)
    computer_score = update_score(computer_score , computer)
    display_scoreboard(player_score , computer_score)
    if player_score >= 30:
        print(f"{username} Ganastes!")
        break  
    elif computer_score >= 30:
        print("La Computadora Gano!")
        break