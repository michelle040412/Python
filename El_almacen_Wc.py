#Muestra en la consola los artículos y precios actuales
"""
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
print('El promedio de los articulo es: ')
print(PROMEDIO)

# Subir el precio de los Jeans en un 6.2%
NuevoPrecioJeans=(Price[3]+6.2%)
print('Los jean aunmentaron a: ')
print(NuevoPrecioJeans)

#Disminuir el precio de los Zapatos en un 0.8%
NuevoPrecioZapatos=(price[0]-0.8%)
print('Los zapatons disminuyeron a:' )
print(NuevoPrecioZapatos)
"""
#valor hora
a = 20000
b = 10000
c = 5000
salario_tope = 1500000


print('el valor de la hora de trabajo en el proyecto a')
print(a)

print('el valor de la hora de trabajo en el proyecto b')
print(b)

print('el valor de la hora de trabajo en el proyecto c')
print(c)

#salario mensual
salario_1 = ((a*8)*30)
print('el salario mensual del proyecto A')
print(salario_1)

salario_2 = ((b*8)*30)
print('el salario mensual del proyecto B')
print(salario_2)

salario_3 = ((c*8)*30)
print('el salario mensual del proyecto C')
print(salario_3)

if salario_1 > salario_tope:
    print('Salario es mayor a tope máximo')
else:
    Nuevo_Salario = ((a*0.06)*30)
    print('salario concepto de hora extra')
    print(Nuevo_Salario)

if salario_2 > salario_tope:
    print('Salario es mayor a tope máximo')
else:
    Nuevo_Salario = ((b*0.06)*30)
    print('salario concepto de hora extra')
    print(Nuevo_Salario)


if salario_3 > salario_tope:
    print('Salario es mayor a tope máximo')
else:
    Horas_extras= ((c*0.06)+ c)
    Nuevo_Salario = ((Horas_extras*8)*30)
    print('salario por concepto de hora extra')
    print(Nuevo_Salario)
