# Clase que representa una Pila
class Pila:
    def __init__(self):
        self.pila = []

    # Método para insertar un elemento en la pila (push)
    def push(self, elemento):
        self.pila.append(elemento)
        print(f"{elemento} agregado a la pila.")

    # Método para extraer el último elemento de la pila (pop)
    def pop(self):
        if not self.esta_vacia():
            elemento = self.pila.pop()
            print(f"{elemento} extraído de la pila.")
            return elemento
        else:
            print("La pila está vacía.")
            return None

    # Método para ver el último elemento de la pila sin eliminarlo (peek)
    def peek(self):
        if not self.esta_vacia():
            print(f"El elemento superior es: {self.pila[-1]}")
            return self.pila[-1]
        else:
            print("La pila está vacía.")
            return None

    # Método para verificar si la pila está vacía
    def esta_vacia(self):
        return len(self.pila) == 0

    # Método para mostrar la pila completa
    def mostrar_pila(self):
        print("Pila actual:", self.pila)

# Función principal para usar la pila
def main():
    mi_pila = Pila()

    # Agregar elementos a la pila
    mi_pila.push(10)
    mi_pila.push(20)
    mi_pila.push(30)

    # Mostrar la pila
    mi_pila.mostrar_pila()

    # Ver el elemento superior
    mi_pila.peek()

    # Extraer elementos de la pila
    mi_pila.pop()
    mi_pila.pop()

    # Mostrar la pila después de extraer
    mi_pila.mostrar_pila()

    # Extraer el último elemento
    mi_pila.pop()

    # Intentar extraer de una pila vacía
    mi_pila.pop()

if __name__ == "__main__":
    main()
