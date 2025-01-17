from io import open 

texto="una line"
archivo=open("archivo.txt","a")
archivo.write(texto)
texto="\nuna linea nueva"
archivo.write(texto)
texto="\nuna linea nueva tres"
archivo.write(texto)

archivo.close()