def calcula_imc(x, y):
    imc = x / (y ** 2)
    return imc


while True:

    peso = float(input("\nDigite o peso em kg: "))
    altura = float(input("digite a altura em m: "))
    imc = calcula_imc(peso, altura)

    match imc:
            
        case imc if imc < 16.9:
            print(f"\nSeu IMC obtido foi de {imc:.2f}, considerado muito abaixo do peso")
        
        case imc if 17 >= imc <= 18.4:
            print(f"\nSeu IMC obtido doi de {imc:.2f}, considerado abaixo do peso")

        case imc if 18.5 >= imc <= 24.9:
            print(f"\nSeu IMC obtido foi de {imc:.2f}, considerado 'normal'")

        case imc if 25 >= imc <= 29.9:
            print(f"\nSeu IMC obtido foi de {imc:.2f}, considerado acima do peso")

        case imc if 30 >= imc <= 34.9:
            print(f"\nSeu IMC obtido foi de {imc:.2f}, considerado 'Obesidade grau 1'")
            
        case imc if 35 >= imc <= 40:
            print(f"\nSeu IMC foi de {imc:.2f}, considerado 'Obesidade grau 2'")

        case imc if imc > 40:
            print(f"\nSeu IMC foi de{imc:.2f}, considerado 'Obesidade grau 3")

    resposta = input("\nDeseja calcular outro IMC? (S/N?): ").upper().strip()

    if resposta == "N":
        break


