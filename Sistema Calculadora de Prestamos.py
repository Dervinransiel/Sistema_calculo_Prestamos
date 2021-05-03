
#Crear un Sistema que solicite el monto, cantidad de cuotas o (plazo) en meses, 
#porcentaje de interes anual de un préstamo.Calcule la cuota mensual y muestre la tabla amortizada de los meses.

import math

print("Prestamo Bancario\n")

prestamo = float(input("Digite el monto del prestamo:"))
tiempo = int(input("Plazo del prestamo (meses):"))
interesAnual = float(input("interes a aplicar al prestamo:"))

#Formula para la cuenta fija 

interesMensual = (interesAnual/12)/100
cuota = ((prestamo*interesMensual)/(1-(math.pow((1+interesMensual),(tiempo*-1)))))

print("")
print("  Interes Anual: ", interesAnual, "%", "\t\t","Monto: $", prestamo)
print("  Plazo Meses: ", tiempo)
print("")
print("{:^10}{:^30}{:^25}{:^40}{:^40}".format("N°",   "cuota",   "Interes",  "Amortizacion",  "Saldo\n"))

nuevoSaldo = prestamo

for i in range(tiempo+1):
        if(i==0):
            print("{:^10}{:^10}{:^15}{:^12}{:^15}".format(i," "," "," ",prestamo))
        else:
            pagoInteres = nuevoSaldo*interesMensual
            amortizacion = cuota-pagoInteres
            nuevoSaldo = nuevoSaldo-amortizacion
            print("{:^10d}{:^102f}{:^12.2f}{:^10.2f}".format(i,cuota,pagoInteres,amortizacion,nuevoSaldo))


