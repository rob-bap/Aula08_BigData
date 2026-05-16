def calcula_bonus(x):
    bonus = x * 0.10
    total = x + bonus
    return bonus, total  # "return" permite que valores enviados para função sejam retornados para o código
    # pass  # pula parte do algoritmo


n = float(input("Informe uma venda: RS"))

if n > 12000:
    bonus, total = calcula_bonus(n)
    print(f"\nValor da venda: R${n:.2f}")
    print(f"Valor da bonus: R${bonus:.2f}")
    print(f"Valor da total: R${total:.2f}")

else:
    print(f"\nValor da venda: R${n:.2f}")
    print(f"Bônus não aplicado.")