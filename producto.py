ciclo = 0

while ciclo == 0:
    nom = input("Cual es su nombre?\n")
    doc = int(input("Cual es su numero de documento?\n"))
    monedasO = int(input("Cual es la moneda que posee?\n1.Dolar\n2.Euro\n3.Peso Colombiano\n4.Dolar Canadiense\n5.Real\n\n8.Salir\n"))
    if monedasO == 8:
        ciclo = 1
        break
    cantidad = int(input("Cuanto dinero quiere cambiar?\n"))
    if monedasO == 1:
        saldoPeso = 4779 * cantidad
    elif monedasO == 2:
        saldoPeso = 5083 * cantidad
    elif monedasO == 3:
        saldoPeso = 1 * cantidad
    elif monedasO == 4:
        saldoPeso = 3507 * cantidad
    elif monedasO == 5:
        saldoPeso = 919 * cantidad

    monedasF = int(input("A que moneda desea convertir?\n1. Dolar\n2.Euro\n3.Peso Colombiano\n4.Dolar Canadiense\n5.Real\n"))
    if monedasO == monedasF:
        print("Usted no puede intercambiar por la misma moneda")
    elif monedasO < 1 or monedasF> 5 or monedasO>5 or monedasF<1:
        print("Seleccionó una moneda inválida")
    elif monedasF == 1:
        decision = int(input("Esta transacción será con una tasa de interes del 12%, ¿Seguro de que deseas realizarla?\n1. Si\n2. No\n"))
        if decision == 1:
            tasaInteres = int(saldoPeso*0.12)
            saldoPeso = saldoPeso - tasaInteres
            saldoPeso = int(saldoPeso / 4779)
            print("Senor/a", nom, "identificado/a con número de documento", doc, ", cambiamos sus",cantidad, " por " , saldoPeso,"$ ,ademas, la tasa interes en COP es", tasaInteres, "$")
        else:
            print("Vuelva pronto!")
    elif monedasF == 2:
        decision = int(input("Esta transacción será con una tasa de interes del 10%, ¿Seguro de que deseas realizarla?\n1. Si\n2. No\n"))
        if decision == 1:
            tasaInteres = int(saldoPeso*0.10)
            saldoPeso = saldoPeso - tasaInteres
            saldoPeso = int(saldoPeso / 5083)
            print("Senor/a", nom, "identificado/a con número de documento", doc, ", cambiamos sus",cantidad, " por " , saldoPeso,"€ ,ademas, la tasa interes en COP es", tasaInteres, "$")
        else:
            print("Vuelva pronto!")
    elif monedasF == 3:
        tasaInteres = int(saldoPeso*0.04)
        saldoPeso = saldoPeso - tasaInteres
        saldoPeso = int(saldoPeso / 1)
        print("Senor/a", nom, "identificado/a con número de documento", doc, ", cambiamos sus",cantidad, " por " , saldoPeso,"COP$ ,ademas, la tasa interes en COP es", tasaInteres, "$")

    elif monedasF == 4:
        tasaInteres = int(saldoPeso*0.09)
        saldoPeso = saldoPeso - tasaInteres
        saldoPeso = int(saldoPeso / 3507)
        print("Senor/a", nom, "identificado/a con número de documento", doc, ", cambiamos sus",cantidad, " por " , saldoPeso,"C$ ,ademas, la tasa interes en COP es", tasaInteres, "$")
    elif monedasF == 5:
        tasaInteres = int(saldoPeso*0.07)
        saldoPeso = saldoPeso - tasaInteres
        saldoPeso = int(saldoPeso / 919)
        print("Senor/a", nom, "identificado/a con número de documento", doc, ", cambiamos sus",cantidad, " por " , saldoPeso,"R$ ,ademas, la tasa interes en COP es de", tasaInteres, "$")