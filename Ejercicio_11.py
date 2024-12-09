cantidad = float(input("Ingrese cantidad de dinero:"))
tasa_de_interes = float(input("Ingrese tasa de interes:"))


cantidad_ahorros = (cantidad * ((tasa_de_interes/100 + 1)))
segundo_año = (cantidad_ahorros * ((tasa_de_interes/100 + 1)))
tercer_año = (segundo_año * ((tasa_de_interes/100 + 1)))


print(f"Cantidad de ahorros primer año {cantidad_ahorros:.2f} , segundo año {segundo_año:.2f} , tercer año {tercer_año:.2f}")
