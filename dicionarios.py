
def calcula_imc(peso=70, altura=1.75):
    return peso / (altura ** 2)

pessoas = {
    "Ana": {"peso": 55, "altura": 1.62},
    "Bruno": {"peso": 80, "altura": 1.80},
    "Carlos": {"peso": 68, "altura": 1.75},
    "Diana": {"peso": 72, "altura": 1.70}
}

for nome, dados in pessoas.items():
    imc = calcula_imc(dados["peso"], dados["altura"])
    print(f"{nome} - IMC: {imc:.2f}")
