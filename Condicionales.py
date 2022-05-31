# Declaramos una variable
calificacion =input("introduce tu porfavor calificacion de la AZ-900 porfavor: ")

calificacion = int(calificacion)
    #Preguntamos si la calificacion es menor de 700
if calificacion < 700 :
    print("veees, por no estudiar") # si es menor a 700 muestra esto
elif calificacion > 1000:
    print("Mientes, no puedes sacar mas de mil")
else :
    print("Felicidades, pasa por tu certificado")

    #verificador de matoria de edad
edad = input("introduce tu edad: ")
edad = int(edad)

if edad >= 18 and edad <= 100 :
    print("Bienvenido al mamitas")
elif edad>100 :
    print("Si vienes acompado de tus abuelos, si podemos fiar") 
elif edad<0:
    print("no eres viajero del tiempo")
else :
    print("no puedes llevarte esos cigarros")   