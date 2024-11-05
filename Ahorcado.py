palabras = ["computadora","ventana","gato","playa","libro","teclado","casa","perro","ciudad","arcoiris","invierno","verano","mesa","parque","nube","bosque","escuela","estudiante","familia","amigo","radio","internet","almohada","silla","ropa","zapatos","tren","carro","pintura","futbol","nadar","reloj","manzana","banana","naranja","pera","uva"]
def elegir_palabra(lista):
    from random import choice
    palabra_elegida = choice(lista)
    for letra in palabra_elegida:
        print("_", end = " ")
    return palabra_elegida


def pedir_letra():
    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    ingreso = 1
    while ingreso not in abc:
        ingreso = input("\nIngresa una letra: ")
    return ingreso

def mostrar_progreso(palabra,letras_correctas):
    progreso = ""
    for n in palabra:
        if n in letras_correctas:
            progreso += n + " "
        else:
            progreso += "_ "
    print(progreso)
def validar_letra(palabra):
    vidas = 6
    lista_incorrectas = []
    letras_correctas = []
    while vidas > 0:
        letra = pedir_letra()

        if letra not in palabra:
            vidas -= 1
            lista_incorrectas.append(letra)
            print(f"\nla letra {letra} no esta en la palabra, tienes {vidas} vidas")
            print(lista_incorrectas)

        else:
            print(f"\nMuy bien, la letra {letra} se encuentra en la palabra.")
            letras_correctas.append(letra)

        mostrar_progreso(palabra,letras_correctas)

        if set(palabra) == set(letras_correctas):
            print(f"\nFelicidades, has adivinado la palabra {palabra}")
            return True



    print(f"\nTe has quedado sin vidas, la palabra era {palabra}")




validar_letra(elegir_palabra(palabras))