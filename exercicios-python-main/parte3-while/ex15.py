positivo = 0
numero = int(input("Digite um numero ou digite 0 se quizer sair: "))

while numero != 0:
     if numero > 0:
        positivos = positivos + 1
        numero = float(input("Digite outro número (0 para sair): "))

print("Quantidade de números positivos digitados:", positivos)