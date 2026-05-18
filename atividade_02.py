def calcula_imc(x, y):
    i = x / y ** 2
    return i


while True:

    peso = float(input("\nDigite o peso em kg: "))
    altura = float(input("digite a altura em m: "))
    imc = calcula_imc(peso, altura)

    match imc:
            
        case i if i <= 17:
            print(f"\nSeu IMC obtido foi de {imc:.2f}, considerado muito abaixo do peso")
        
        case i if i <= 18.5:
            print(f"\nSeu IMC obtido doi de {imc:.2f}, considerado abaixo do peso")

        case i if i <= 25:
            print(f"\nSeu IMC obtido foi de {imc:.2f}, considerado 'normal'")

        case i if i <= 30:
            print(f"\nSeu IMC obtido foi de {imc:.2f}, considerado acima do peso")

        case i if i <= 35:
            print(f"\nSeu IMC obtido foi de {imc:.2f}, considerado 'Obesidade grau 1'")
            
        case i if i <= 40:
            print(f"\nSeu IMC foi de {imc:.2f}, considerado 'Obesidade grau 2'")

        case i if i > 40:
            print(f"\nSeu IMC foi de{imc:.2f}, considerado 'Obesidade grau 3")

    resposta = input("\nDeseja calcular outro IMC? (S/N?): ").upper().strip()[0]

    if resposta != "S":
        break


