numero1 = 10
numero2 = 3
suma           = numero1 + numero2   # 13
resta          = numero1 - numero2   # 7
multiplicacion = numero1 * numero2   # 30
division       = numero1 / numero2   # 3.333...
division_entera= numero1 // numero2  # 3
residuo        = numero1 % numero2   # 1
potencia       = numero1 ** numero2  # 1000



print(f"""
Resultado de Operaciones Aritméticas:
suma:            {numero1} +  {numero2} = {suma}
resta:           {numero1} -  {numero2} = {resta}
multiplicacion:  {numero1} *  {numero2} = {multiplicacion}
division:        {numero1} /  {numero2} = {division:.4f}
division_entera: {numero1} // {numero2} = {division_entera}
residuo:         {numero1} %  {numero2} = {residuo}
potencia:        {numero1} ** {numero2} = {potencia}
""")


print("Ejercicio  1:suma de dos numeros")
print("--"*20)

numero1= float(input("ingrese el primer numero"))
numero2=folat(input("ingrese el segundo numero:"))

print(f"resultado:{numero1+numero2}")

#ejerciocio 2:Àrea de un rectangulo
base =float(input("ingrese la base del rectangulo:"))
altura=float(input("ingrese la altura del rectangulo:"))

area=base *altura #formula:base*altura

print(f"el àrea del rectangulo es:´{area}")

#ejercicio 5:conversion de minutos a horas y minutos 
minutos_totales=int(input("ingrese la cantida de minutos:"))

horas = minutos_totañes // 60 #division entera → horas completas 
minutos = minutos_totales % 60    # módulo → minutos restantes

print(f"{minutos_totales}minutos equivalen a {horas}horas y {minutos}minutos"
)
#ejercicio 4:Calculo del precio con descuento
precio  = float(input("Ingrese el precio del producto: "))
descuento = float(input("Ingrese el porcentaje de descuento: "))

valor_descuento = precio * (descuento / 100)   # valor que se descuenta
precio_final    = precio - valor_descuento      # precio con descuento

print(f"El precio final a pagar es: {precio_final}")


#Ejercicio 5: Intercambio de valores entre dos variables
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))

auxiliar = a   # guardar temporalmente el valor de a
a = b          # a toma el valor de b
b = auxiliar   # b toma el valor original de a

print(f"Después del intercambio: a = {a} , b = {b}")

TALLER #1 Ejercicios para resolver

#respuestas ejercicios 

print("ejercicio1:solicitar  largo y ancho de un terreno rectangular y calcular su perimetro" )

largo=float(input("ingrese el largo del terreno"))
ancho=float(input("ingrese el ancho del terreno"))

print(f"el perimetro del terreno es:{2*largo+2*ancho}")


"""
print("ejercicio2:solicitar tres numeros y mostrar su promedio")

numero1=(float(input("ingrese el numero 1:")))
numero2=(float(inpnut("ingrese el numero 2:")))
numero3=(float(input(ingrese el numero 3:)))

promedio=(numero1 + numero2 +numero3) /3
print(f"el promedio de los tres numeros es{promedio:.2f}")
t("ejercicio3:solicitar el nombre y la edad de una persona y mostrar un mensaje de presentacion")
"""

"""
print("ejercicio3:solicitar el nombre y la edad de una persona y mostrar un mensaje de presentacion")

nombre=str(input("ingrese su nombre"))
edad=float(input("ingrese su edad"))

print(f"hola mi nombre es :{nombre}y tengo{edad}años")

print("solicitar un valor en pesos colombianos y mostrar su equivalenteaproximado en dòlares(tasa fija:1usd=4000 cop")

valor=float(input("ingrese valor en pesos colombianos(COP)"))
print(f"el equivalente aproximado en dòlares(USD)es:{valor/4000}")
"""

"""
 
print(ejercicio5:solicitar una cantidad de segundos y convertirlos a horas,minutos y segundos)

cantidad=float("ingrese la cantidad de segundos")
horas   =float("ingrese la cantidad de segundos")
minutos =float("ingrese la cantidad de segundos")
segundos=float("ingrese la cantidad de segundos") 
"""









