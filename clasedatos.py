class Informacion:
    def mi_lista(self):
        lista_nombreperros=["kilo","kenda","kimbo"]
        for x in lista_nombreperros:
            print(x)

    def mi_tupla(self):
        tupla_nombreperros=("josy","leysi","ledo")
        for x in tupla_nombreperros:
            print(x)

    def mi_diccionario(self):
        diccionario_nombreperros={"jonathan","vale","bingley"}
        for x in diccionario_nombreperros:
            print(x)

    def mi_conjunto(self):
        conjunto_nombreperros={"tavo","sergio","wisho"}
        for x in conjunto_nombreperros:
            print(x)
        # creando el objeto
datos=Informacion()
print("listado de nombres de perros")
datos.mi_lista()

print("tupla de nombres de perros")
datos.mi_tupla()

print("diccionario de nombres de perros")
datos.mi_diccionario()

print("conjunto de nombres de perros")
datos.mi_conjunto()