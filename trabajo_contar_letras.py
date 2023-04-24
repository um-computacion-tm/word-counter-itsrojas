import unittest

def contar_letras(palabras):
    resultado = {}
    for letras in palabras:
        if letras == " ":
            continue
    if letras in resultado:
        resultado[letras] += 1
    else:
        resultado[letras] = 1
    return resultado

if __name__ == '__main__':
    unittest.main()
