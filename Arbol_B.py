class NodoB:
    def __init__(self, grado, hoja=True):
        self.grado = grado
        self.hoja = hoja
        self.claves = []
        self.hijos = []

    def buscar_clave(self, clave):
        i = 0
        while i < len(self.claves) and clave > self.claves[i]:
            i += 1
        return i if i < len(self.claves) and self.claves[i] == clave else -1


class ArbolB:
    def __init__(self):
        self.raiz = None

    def insertar(self, clave):
        if not self.raiz:
            self.raiz = NodoB(self.grado)
            self.raiz.claves.append(clave)
        else:
            if len(self.raiz.claves) == (2 * self.grado) - 1:
                nueva_raiz = NodoB(self.grado, hoja=False)
                nueva_raiz.hijos.append(self.raiz)
                self.dividir_hijo(nueva_raiz, 0)
                self.raiz = nueva_raiz

            self.insertar_no_lleno(self.raiz, clave)

    def insertar_no_lleno(self, nodo, clave):
        i = len(nodo.claves) - 1
        if nodo.hoja:
            nodo.claves.append(None)
            while i >= 0 and clave < nodo.claves[i]:
                nodo.claves[i + 1] = nodo.claves[i]
                i -= 1
            nodo.claves[i + 1] = clave
        else:
            while i >= 0 and clave < nodo.claves[i]:
                i -= 1
            i += 1
            if len(nodo.hijos[i].claves) == (2 * self.grado) - 1:
                self.dividir_hijo(nodo, i)
                if clave > nodo.claves[i]:
                    i += 1
            self.insertar_no_lleno(nodo.hijos[i], clave)

    def dividir_hijo(self, padre, i):
        grado = self.grado
        hijo = padre.hijos[i]
        nuevo_hijo = NodoB(grado, hoja=hijo.hoja)
        padre.claves.insert(i, hijo.claves[grado - 1])
        padre.hijos.insert(i + 1, nuevo_hijo)
        nuevo_hijo.claves = hijo.claves[grado:(2 * grado) - 1]
        hijo.claves = hijo.claves[0:grado - 1]
        if not hijo.hoja:
            nuevo_hijo.hijos = hijo.hijos[grado:2 * grado]
            hijo.hijos = hijo.hijos[0:grado]

    def buscar(self, clave):
        return self.buscar_en_nodo(self.raiz, clave)

    def buscar_en_nodo(self, nodo, clave):
        i = 0
        while i < len(nodo.claves) and clave > nodo.claves[i]:
            i += 1
        if i < len(nodo.claves) and clave == nodo.claves[i]:
            return True
        if nodo.hoja:
            return False
        return self.buscar_en_nodo(nodo.hijos[i], clave)

    def eliminar(self, clave):
        if not self.buscar(clave):
            print("La clave no existe en el arbol")
            return
        self.eliminar_en_nodo(self.raiz, clave)

    def eliminar_en_nodo(self, nodo, clave):
        i = 0
        while i < len(nodo.claves) and clave > nodo.claves[i]:
            i += 1
        if clave == nodo.claves[i]:
            if nodo.hoja:
                del nodo.claves[i]
            else:
                # Logica para eliminar en un nodo no hoja
                pass
        else:
            if nodo.hoja:
                print("La clave no existe en el arbol")
                return
            elif len(nodo.hijos[i].claves) >= self.grado:
                self.eliminar_en_nodo(nodo.hijos[i], clave)
            elif len(nodo.hijos[i].claves) == self.grado - 1:
                # Reequilibrar el árbol si el nodo hijo tiene menos claves
                pass

    def imprimir(self):
        if self.raiz:
            self._imprimir(self.raiz)

    def _imprimir(self, nodo, prefijo=""):
        print(prefijo + str(nodo.claves))
        if not nodo.hoja:
            for i in range(len(nodo.hijos)):
                self._imprimir(nodo.hijos[i], prefijo + "  ")


if __name__ == "__main__":
    arbol_b = ArbolB()
    grado = int(input("Introduce el grado del arbol B: "))
    arbol_b.grado = grado

    while True:
        opcion = input("Seleccione una opcion:\n  1. Insertar clave\n  2. Eliminar clave\n  3. Buscar clave\n  4. Imprimir arbol\n  5. Salir\nOpcion: ")
        if opcion == "1":
            clave = int(input("Introduce la clave a insertar: "))
            arbol_b.insertar(clave)
        elif opcion == "2":
            clave = int(input("Introduce la clave a eliminar: "))
            arbol_b.eliminar(clave)
        elif opcion == "3":
            clave = int(input("Introduce la clave a buscar: "))
            print(f"¿La clave {clave} esta en el arbol? {arbol_b.buscar(clave)}")
        elif opcion == "4":
            print("Arbol B:")
            arbol_b.imprimir()
        elif opcion == "5":
            break
        else:
            print("Opcion no valida.")
