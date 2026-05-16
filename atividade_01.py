def calcula_multa(x):
    quantidade_multa = x - 100
    valor_multa = quantidade_multa * 4
    return quantidade_multa, valor_multa


peso = float(input("Digite a quantidade em quilos(kg): "))

if peso > 100:
    quantidade_multa, valor_multa = calcula_multa(peso)
    print(f"\nA quantidade pescada ultapassou o limite com {quantidade_multa} kg excedentes!")
    print(f"Uma multa de R${valor_multa:.2f} será aplicada.")

else:
    print(f"\nA quantidade pescada foi de {peso} kg, sem ultrapassar o limite de peso.")