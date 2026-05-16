peso = float(input("Digite a peso: "))
altura = float(input("Digite a altura: "))

imc = peso / (altura ** 2)

match imc:

    case < 16.9
        print("")