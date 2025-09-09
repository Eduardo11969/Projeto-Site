def calcular_imc(peso,altura):
    return peso/altura**2

def categoria_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 24.9:
        return "Peso normal"
    elif imc < 29.9:
        return "Sobrepeso"
    elif imc < 34.9:
        return "Obesidade I"
    elif imc < 39.9:
        return "Obesidade II"
    else:
        return "Obesidade lll"