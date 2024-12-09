peso_kg = float(input("Peso en Kilogramos"))
estatura = float(input("estatura en Metro"))

indice_masa_corporal = peso_kg / (estatura **2)

print(f"Tu indice de masa corporal es {indice_masa_corporal:.2f}")