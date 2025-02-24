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
B = round(A)
if (A%B)== 0 :
    print("No tiene decimales")
else :
    print("Si tiene decimales")