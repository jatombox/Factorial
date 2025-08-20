numero=int(input("ingrese el numero al cual calcular el factorial:"))

factorial=1

for i in range(1,numero+1):
  factorial=factorial*i
  print(f"Paso {i}: factorial = {factorial}")