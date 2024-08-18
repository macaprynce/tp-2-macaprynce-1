def change():
    expense = 23.75
    money = 100
    vuelto = money // expense
    print("ingresar gasto:")
    print(f"{expense})
    print("dinero recibido")
    print(f"{money})
    print()
    print("vuelto")
    print()
    print("pesos:")
    print(int(money-expense))
    print("centavos:")
    print(int((float(money-expense)-int(money-expense))*100))
