"""
for i in range(1,11,2):
    print(f"Dracarys😊")
"""
"""
mensaje=input("escribe tu mensaje:")
repeticion=int(input("cuantas veces quiere repetir mensaje :"))

for i in range(repeticion):
    print(f"{i+1} - {mensaje}")
    """

"""
    #Preguntar al nombre de estudiante
    #preguntar al profe :cuantas notas quiere registrar.
    #hacer el promedio de las notas y mostrarlo
    #promrdio >=3.5 mostrar estudiante gano -contrario perdio

print("=== Sistema de calificacion.=== ")
estudiante = input("Nombre del estudiante")
can_notas =int(input("cuantas notas vas a registrar:"))

promedio=0
for i in range(can_notas):
    notas =float(input(f"ingrese nota¨{i+1} : "))
    if notas not in range(0,5):
        print("nota invalida")
        break

    promedio += notas

promedio_final=promedio/can_notas

if  (promedio/can_notas)>=3.5:
     print(f"el estudiante{estudiante}-promedio{promedio_final:.1f}gano🎉")
else:
     print(f"el estudiante{estudiante} - promedio {promedio_final:.1f}perdio ❌")

   

while True:
    print("hoy es viernes.y el cuerpo lo sabe 💃🎉💃")
  """
  """
while True:
    menu = int(input("""
    seleccione opcion a realizar:
    1.sumar
    2.restar
    3.salir
    : """))

    if  menu==1:
        n1=int(input(" ingrese n1 :"))
        n2=int(input("ingrese n2 :"))
        print(f"resultado{n1+n2}")
    elif menu==2:
        n1=int(input("ingrese n1:"))
        n2=int(input("ingrese n2:"))
        print(f"resultado{n1-n2}")
    elif menu==3:
        print("saliendo del sistema")
        break
    else:
        print("opcion invalida")
        """
        
        
        
