precio_fresca = 3.49
precio_vieja = 0.4

cantidad_vendidas_dia = int(input("Cantidad de Barras vendidas"))
cantidad_vendidas_viejas = int(input("Cantidad de Barras vendidas"))

precio_habitual_vieja = precio_fresca * cantidad_vendidas_viejas *precio_vieja

precio_habitual_dia = precio_fresca * cantidad_vendidas_viejas

venta = precio_habitual_dia + precio_habitual_vieja

print(f"Monto de la barra de pan fresca: {precio_habitual_dia:.2f}")
print(f"Monto de la barra de pan vieja: {precio_habitual_vieja:.2f}")
print(f"monto tota: {venta}")