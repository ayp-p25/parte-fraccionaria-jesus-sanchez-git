"""
• Ejercicio parte fraccionaria
• Jesús Alejandro Sánchez Muñoz 
• 758377 • Igenieria Mecanica 
• Algoritmos y Programcion 
• ESI232B2 • Jorge Zaldivar 
• 23/feb/25 
• 5 m
"""

A = float(input("Ingrese el numero que desee saber si posee decimales : \n"))
if A != 0:
    B = round(A)
    if (A%B)== 0  :
        print("No posee decimales")
    elif (A%B)!= 0:
        print("Si posee decimales")
else:
    print("No posee decimales")