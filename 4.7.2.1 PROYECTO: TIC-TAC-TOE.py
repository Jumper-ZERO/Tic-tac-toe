#Tic-tac-toe Game
#Autor: Jeremi Aron Chancan Labajos

#Import para colores
import sys

#Declaracion de Variables
color= sys.platform == 'linux'
colors=["\033[3;36mX\033[0m", "\033[3;32mO\033[0m"]

positions=[i for i in range(1,10)]
positions_of={
        "X": [],
        "O": []
        }
status=[i for i in positions_of.keys()]
turn_status=status[0] #who's turn is it
in_game=True

#Bienvenida de Inicio
bienvenida="   Tic Tac Toe  "
print("+","=" * (len(bienvenida)+7),"+",sep="")
print("|", bienvenida," |",sep=" "*3)
print("+","=" * (len(bienvenida)+7),"+",sep="")
print()

print("+-------+-------+-------+")
print("|       |       |       |",end="     "*2 + "Reglas:" + "\n")
print("|   1   |   2   |   3   |",end="     "*2 + "1) Elige jugar con 'X' o 'O' (pulsa enter usar 'X')" + "\n")
print("|       |       |       |",end="     "*2 + "" + "\n")
print("+-------+-------+-------+")
print("|       |       |       |")
print("|   4   |   X   |   6   |")
print("|       |       |       |")
print("+-------+-------+-------+")
print("|       |       |       |")
print("|   7   |   8   |   9   |")
print("|       |       |       |")
print("+-------+-------+-------+")

#Definicion de Funciones Principales
def Configurations():
    input("Ingresa con quien quieres comenzar: ")

def Draw():
    text=f"Es Turno de \"{turn_status}\""
    spaces_border=len(text)+(23-len(text))
    spaces_text=23-(len(text))>>1

    print("+","-" * spaces_border,"+",sep="")
    print("|"," " * spaces_text,text, " " * spaces_text, "|", sep="") 
    print("+","-" * spaces_border,"+",sep="")



    print("+-------"*3,sep="",end="+\n")
    for i in range(0,9,3):
        print("|       "*3,sep="",end="|\n")
        print(f"|   {positions[i]}   |   {positions[i+1]}   |   {positions[i+2]}   |")
        print("|       "*3,sep="",end="|\n")
        print("+-------"*3,sep="",end="+\n")

def EnterMove(status):
    try:
        move=int(input(f"Ingresa tu movimiento para {status}: "))
        if move in positions:
            print("Pusiste: "+ str(move) + " en el turno de "+ status)
            print()
            if color:
                if status == "X":
                    positions[move-1] = colors[0]
                elif status == "O":
                    positions[move-1] = colors[1]
            else:
                positions[move-1] = status
            positions_of[status].append(move)
        else:
            print("Solo puedes poner los numeros disponibles: ",end="\n\n\t")
            if color: 
                positions_free=[ i for i in positions if i!=colors[0] and i!=colors[1]]
            else:
                positions_free=[ i for i in positions if i!="X" and i!="O" ]
            for i in positions_free:
                print(i, end="  ")
            print("\n")
            EnterMove(status)

    except ValueError:
        print("\n\tSolo puedes poner numeros enteros\n")
        EnterMove(status)

def TurnChange():
    status[0], status[1] = status[1], status[0]
    global turn_status 
    turn_status=status[0]

def VictoryFor():
    cases_of_victory=[(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]
    global in_game
    
    def show_mensaje(mensaje):
        text=mensaje
        spaces_border=len(text)+(23-len(text))
        spaces_text=23-(len(text))>>1

        print()
        print("+","=" * spaces_border,"+",sep="")
        print("|"," " * spaces_text,text, " " * spaces_text, "|", sep="") 
        print("+","=" * spaces_border,"+",sep="")
        print()

    if any(set(caso).issubset(positions_of[turn_status]) for caso in cases_of_victory):
        in_game=False
        show_mensaje(f"El ganador es {turn_status}🎉")
        
    elif len([ i for i in positions if i!="X" and i!="O" ]) == 0:
        in_game=False
        show_mensaje("Empate ⚔ ")

def Game():
    EnterMove(turn_status)
    Draw()
    VictoryFor()
    TurnChange()

#Declaracion de Funciones
while in_game:
    try:
        Game()
    except KeyboardInterrupt:
        print("\n\n\tNo te rindas tan facil vuelve para la revancha\n")
        break
