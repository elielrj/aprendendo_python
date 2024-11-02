try:
    dividendo = int(input('Digite um número p/ dividir: '))

    divisor = int(input('Digite um número divisor: '))

    quaciente = dividendo /divisor

    print(f'Resultado da divisão é: {quaciente}')

except ZeroDivisionError:
    print('Divisão não é possível')
finally:
    print('Terminou!')