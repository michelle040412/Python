#Muestra en la consola los artículos y precios actuales

Articulo=["ZAPATOS", "TENIS","CAMISETAS","JEANS"]
Price= [350000,280000,175000,200000]

print("Precio de los articulos")
print("El articulo ", Articulo[0], "cuesta ", Price[0])
print("El articulo ", Articulo[1], "cuesta ", Price[1])
print("El articulo ", Articulo[2], "cuesta ", Price[2])
print("El articulo ", Articulo[3], "cuesta ", Price[3])

#También mostrar el costo total de los cuatro artículos

CostoTotal=(Price[0]+Price[1]+Price[2]+Price[3])
print("el costo de los 4 articulos es:")
print(CostoTotal)

# el promedio de venta
PROMEDIO= (CostoTotal/4)
print(El promedio de los articulo es: )
print(PROMEDIO)

# Subir el precio de los Jeans en un 6.2%
NuevoPrecioJeans=(Price[3]+6.2%)
print(Los jean aunmentaron a: )
print(NuevoPrecioJeans)

#Disminuir el precio de los Zapatos en un 0.8%
NuevoPrecioZapatos=(price[0]-0.8%)
print(Los zapatons disminuyeron a: )
print(NuevoPrecioZapatos)
