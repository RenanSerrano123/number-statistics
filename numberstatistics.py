def calcular_estatisticas(valores):
    soma = sum(valores)
    media = soma / len(valores)
    minimo = min(valores)
    maximo = max(valores)
    return soma, media, minimo, maximo
def main():
    n = int(input())
    numeros = []
    for i in range(n):
        numero = int(input())
        numeros.append(numero)
    soma, media, minimo, maximo = calcular_estatisticas(numeros)
    print(f"{soma}")
    print(f"{media:.2f}")
    print(f"{minimo}")
    print(f"{maximo}")
main()