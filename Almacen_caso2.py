# valor hora
a = 20000
b = 10000
c = 5000
salario_tope = 1500000

print('el valor de la hora de trabajo por proyecto')

print('El proyecto A')
print(a)

print('El proyecto B')
print(b)

print('El proyecto C')
print(c)

#salario mensual
salario_1 = (a*8)*30
print('el salario mensual del proyecto A')
print(salario_1)

salario_2 = (b*8)*30
print('el salario mensual del proyecto B')
print(salario_2)

salario_3 = (c*8)*30
print('el salario mensual del proyecto C')
print(salario_3)


if salario_1 > salario_tope:
    print('Salario A es mayor a tope máximo')
else:
    print('pagarle al empleado del proyecto A hora extra, el valor de la hora día incrementada en un 6%')
    Ajuste_Hora_ExtraA=(((a*0.06) + a)*3)
    Nuevo_salarioA= (salario_1+Ajuste_Hora_ExtraA)
    print(Nuevo_salarioA)

if salario_2 > salario_tope:
    print('Salario B es mayor a tope máximo')
else:
    print('pagarle al empleado del proyecto B hora extra, el valor de la hora día incrementada en un 6%')
    Ajuste_Hora_ExtraB=(((b*0.06) + b)*3)
    Nuevo_salarioB= (salario_2+Ajuste_Hora_ExtraB)
    print(Nuevo_salarioB)

if salario_3 > salario_tope:
    print('Salario C es mayor a tope máximo')
else:
    print('pagarle al empleado del proyecto C hora extra, el valor de la hora día incrementada en un 6%')
    Ajuste_Hora_ExtraC=(((c*0.06) + c)*3)
    Nuevo_salarioC= (salario_3+Ajuste_Hora_ExtraC)
    print(Nuevo_salarioC)
