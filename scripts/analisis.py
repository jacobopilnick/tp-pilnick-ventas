import csv
import matplotlib.pyplot as plt

fechas = []
montos = []

total = 0
cantidad = 0

with open("datos/ventas.csv", newline="", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)

    for fila in lector:
        fechas.append(fila["fecha_venta"])
        monto = float(fila["monto_vendido"])
        montos.append(monto)

        total += monto
        cantidad += 1

promedio = total / cantidad

print("Cantidad de ventas:", cantidad)
print("Total vendido: $", total)
print("Promedio de ventas: $", round(promedio, 2))

plt.figure(figsize=(10,5))
plt.bar(fechas, montos)
plt.title("Ventas por día")
plt.xlabel("Fecha")
plt.ylabel("Monto vendido ($)")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
