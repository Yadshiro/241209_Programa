peso_payaso = 112
peso_muñeca = 75

payaso = int(input("Cantidad de Payasos:"))
muñeca = int(input("Cantidad de Muñecas:"))

peso_paquete = (payaso * peso_payaso) + (muñeca * peso_muñeca)

print(f"El payaso del paquete es de: {peso_paquete} gramos")