# Número informado pelo usuário
num = int(input("Digite um número: "))

# Variáveis
fib1 = 0
fib2 = 1

# Loop para gerar os termos da sequência até que o próximo termo seja maior que o número informado
while fib2 < num:
    # Calcula o próximo termo como a soma dos dois números anteriores
    fib3 = fib1 + fib2
    # Atualiza as variáveis para os próximos números da sequência
    fib1 = fib2
    fib2 = fib3

# Verifica se o número informado pertence à sequência
if fib2 == num:
    print(num, "pertence à sequência de Fibonacci.")
else:
    print(num, "não pertence à sequência de Fibonacci.")