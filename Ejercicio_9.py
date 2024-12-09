usuario = float(input("Cantidad a Invertir:"))
interes_anual = int(input("Interes anual en %:"))
numeros_años = int(input("Cantidad de años"))




print(f"El capital obtenido es de: {usuario*(interes_anual / 100 + 1) ** numeros_años :.2f}")

