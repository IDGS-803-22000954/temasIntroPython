from io import open 
import os

class Diccionario:

    espaniol=""
    ingles=""

    def __init__(self,a,b):
        self.espaniol=a
        self.ingles=b

    def insertar(self):
        texto=self.espaniol+":"+self.ingles+"\n"
        archivo=open("diccionario.txt","a")
        archivo.write(texto)
        archivo.close()
        print("Palabra insertada")
        input()

    def buscarEspaniol(self):
        archivo=open("diccionario.txt","r")
        lineas=archivo.readlines()
        diccionario={}
        for linea in lineas:
            español, ingles = linea.strip().split(':')
            diccionario[español] = ingles
        palabra=self.espaniol
        archivo.close()
        if palabra in diccionario:
            print(f"La palabra {palabra} en inglés es: {diccionario[palabra]}")
        else :
            print("La palabra no se encuentra")
        input()
    
    def buscarIngles(self):
        archivo=open("diccionario.txt","r")
        lineas=archivo.readlines()
        diccionario={}
        for linea in lineas:
            español, ingles = linea.strip().split(':')
            diccionario[ingles] = español
        palabra=self.ingles
        archivo.close()
        if palabra in diccionario:
            print(f"La palabra {palabra} en español es: {diccionario[palabra]}")
        else :
            print("La palabra no se encuentra")
        input()

def main():
    while True:
        os.system('cls')
        print("Menú de opciones")
        print("1. Insertar palabra")
        print("2. Buscar palabra")
        print("3. Salir")
        opcion = int(input("Selecciona una: "))
        if opcion == 1:
            a=input("Palabra en español: ")
            b=input("Su traducción al inglés: ")
            obj=Diccionario(a,b)
            obj.insertar()
        if opcion == 2:
            print("En qué idioma: ")
            print("1. Español")
            print("2. Inglés")
            lang=int(input())
            if lang == 1:
                a=input("Inserte la palabra: ")
                b=""
                obj=Diccionario(a,b)
                obj.buscarEspaniol()
            else:
                a=""
                b=input("Inserte la palabra: ")
                obj=Diccionario(a,b)
                obj.buscarIngles()
        if opcion == 3:
            break

if __name__ == "__main__":
    main()