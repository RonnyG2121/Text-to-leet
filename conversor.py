"""
Este módulo contendrá un clase capaz de recorrer una cadena de caracteres ingresada por el usuario para convertirla en código leet o 1337.
"""


class Leet:

# Diccionario que le asigna el carácter correspondiente ca dada letra
    dict_leet = {
        "a": "4",
        "b": "I3",
        "c": "[",
        "d": "|)",
        "e": "3",
        "f": "|=",
        "g": "(_+",
        "h": ")-(",
        "i": "1",
        "j": "]",
        "k": "|<",
        "l": "7",
        "m": "|V|",
        "n": "|\|",
        "o": "()",
        "p": "|>",
        "q": "0_",
        "r": "I2",
        "s": "$",
        "t": "-|-",
        "u": "(_)",
        "v": "\/",
        "w": "\/\/",
        "x": "×",
        "y": "¥",
        "z": "%",
        "1": "L",
        "2": "R",
        "3": "E",
        "4": "A",
        "5": "S",
        "6": "b",
        "7": "T",
        "8": "B",
        "9": "g",
        "0": "o"
        }

# Método de clase que se usa para convertir el carácter a código leet. Recibirá un parámetro para poder pasarle la información
    @classmethod
    def converter(cls, text):

# Variable usada para sumarle cada carácter a cada vuelta de bucle
        resultado = ""

# Bucle for que recorre el diccionario y le asigna cada carácter donde corresponda
        for i in text:

# Ignorando el carácter en minúscula o mayúscula y convirtiéndolo a string
            i = str(i.lower())

# Comprobando si el carácter está en el diccionario
            if i in cls.dict_leet:
                resultado += cls.dict_leet[i] # Esto es lo que pasa el valor de cada clave en el diccionario

# Si no está, se devuelve el carácter original
            else:
                resultado+= i

# Regresamos la variable resultado
        return resultado

# Creando método constructor que llama al método converter
    def __init__(self, texto):
        self._texto = texto
        self._resultado = Leet.converter(self._texto)

# Creando el método str para poder imprimir el objeto
    def __str__(self):

        return "{}".format(self._resultado)


# Zona de pruebas
if __name__ == "__main__":
    palabra = input("Ingrese un texto aquí")
    mi_leet = Leet(palabra)
    print(mi_leet)
