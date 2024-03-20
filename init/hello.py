# a = 'Hello'
# b = ', world!'
# print(a + b)   ### imprime 'Hello, world!'

# a = 5
# print(a + b)   ### ERROR: TypeError: unsupported operand type(s) for +: 'int' and 'str'

#!/usr/bin/env python3

# acá importamos los módulos que usamos -- sys es un módulo estándar
import sys

# Ponemos nuestro código en una función main()
def main():
    print('Hello there', sys.argv[1])
    # Los argumentos de la líena de comando están en sys.argv[1], sys.argv[2] ...
    # sys.argv[0] es el nombre del propio script como sucede en C

# Código estándar para llamar main() cuando arranca en programa.
if __name__ == '__main__':
    main()

# python3 hello.py "Sistemas Operativos"
