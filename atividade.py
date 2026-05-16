def calcula_desconto(x):
    desconto = x * 0.16
    total = x - desconto
    return desconto, total


valor = float(input("Digite o valor da compra: R$"))

if valor > 250:
    desconto, total = calcula_desconto(valor)
    print(f"\nO valor final da compra foi de R${total:.2f} com o desconto de R${desconto:.2f}")

else:
    print(f"\nO valor final da compra foi de R${valor:.2f}")