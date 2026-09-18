"""
Solicitar la edad de una persona y determinar si es mayor o menor de edad.

"""
"""
#crear variables
print ("por favor ingresa los siguientes datos\ n")

var_nombre=input("nombre:") 
var__edad=int(input("edad:"))

#crear condicion

if var_edad>=18 :
    print(f"{var_nonmbre}Eres mayor de edad")
else:
    print(f"{var_nombre}Eres menor de Edad.")
    """
"""
#ejemplo 2.
print(ejercicio : Nota Final:)
var_nombre=input("Nombre:")
var_notafinal=float(input("Nota fina:"))

if var_notafina <0 or var_notafinal>5:
       print("Nota Invalida.")

   
    
elif var_notafinal>=  3.5   :
       print(f"Estudiante{var_nombre}GANO  🎉")
else:
       print(f"Estudiante{var_nombre}PERDIO ❌")
       """



#EJERCICIO 1

nombre = input("dame tu nombre")
Edad   = int(input("dame tu edad pero solo entero"))

if edad <=0:
       print("por favor digita el valor correcto")
elif edad >= 18:
       print(f"hola{nombre}tienes{edad}años.por lo tanto ya puedes beber")
else:
       print(f"Hola{nombre}tienes{edad}años,por tanto te faltan¨{18-edad}años,toma mas leche")



nombre = input("nombre:")
nota = float(input("nota"))

#0-3=insuficiente
if nota < 0 or nota > 5:
       print(f"{nota}invalida")

elif nota < 3:
       print(f"{nota}insuficiente")

elif nota < 3.5:
       print(f"{nota}aceptable")

elif nota < 4.5:
       print(f"{nota} Bueno")

else:
       print(f"{nota}Excelente")

       #EJERCICIO 2 ELABORA UN ALGORITMO QUE SOLICITE EL NOMBRE DE UN CLIENTE  
       nombre=input("nombre :")
       total_compra =float(input("Total compra($): "))


if total_compra < 100000 :
       print(f"""
       -Cliente {nombre}
       -Compra {total_compra} No tiene descuento
       """)
elif total_compra <299999:
       #Descuento 10%
       print(f"""
       -cliente{nombre}
       _compra{total_compra}
       -descuento {total_compra *0.1}:
       -Total a pagar :{total_compra-(total_compra*0.1)})
       -total pagar:{total_compra -(total_compra *0.1)}
       """)

elif total_compra < 499999 :
       #Descuento 15%
       print(f"""
       -cliente{nombre}
       _compra{total_compra}
       -descuento {total_compra *0.15}:
       -Total a pagar :{total_compra-(total_compra*0.15)}
        """)
else :
       -print(f"""cliente{nombre}
       _compra{total_compra}
       -descuento {total_compra *0.2}:
       -Total a pagar : {total_compra-(total_compra*0.2)}
        """)

# ============================================================================================
# EJERCICIO 3: ELABORAR UN ALGORITMO QUE SOLICITE EL NOMBRE DE UN CLIENTE
# Y EL VALOR TOTAL DE LA COMPRA Y CALCULE EL DESCUENTO SEGÚN EL VALOR.
# MENOS DE $100.000 - SIN DESCUENTO

# Entrada de datos
nombre = input("Nombre del cliente: ")
valor_compra = float(input("Valor total de la compra ($): "))

# Validación
if valor_compra <= 0:
    print("Error: El valor de la compra debe ser mayor a cero.")
else:
    # Determinar porcentaje de descuento
    if valor_compra < 100000:
        porcentaje = 0
    elif valor_compra < 300000:
        porcentaje = 10
    elif valor_compra < 500000:
        porcentaje = 15
    else:
        porcentaje = 20

    # Cálculos
    valor_descuento = valor_compra * (porcentaje / 100)
    total_pagar = valor_compra - valor_descuento

    # Salida final
    print(f"""
Nombre del cliente: {nombre}
Valor de la compra: ${valor_compra:,.2f}
Descuento aplicado: {porcentaje}%
Valor descuento: ${valor_descuento:,.2f}
Total a pagar: ${total_pagar:,.2f}
""")


#===========================================================================================================

       #ejercicio 4
print("Elabora un algoritmo que solicite el nonbre de una ciudad y la temperatura")

     

ciudad=input("ingrese el nombre de la ciudad:") 
temperatura=float(input("ingrese la temperatura actual en ºc :"))

if     temperatura <10:
       clasificaciòn ="muy frìa"
elif   temperatura >= 10 and temperatura <= 17:
       clasificaciòn = "frìa" 
elif   temperatura >= 18 and temperatura <=25:
       clasificaciòn = "templada"
elif   temperatura >=26 and temperatura <=32:
       clasificaciòn = "caliente"
else:  
       clasificaciòn = "muy caliente"

if     temperatura <18:
       recomendaciòn = "se recomienda llevar paraguas."
else:  
       recomendación="no es necesario llevar paraguas."

       print(f"""
       -Ciudad:{ciudad}
       Temperatura :   {temperatura}ºC
       -Clasificaciòn : {clasificaciòn}
       -recomendaciòn : ´{recomendaciòn}
       """)

#=========================================================================================================













        



