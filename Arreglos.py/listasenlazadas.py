#clase que define un nodo de la lista enlazada
class nodo:
    def __init__(self, numero):
        #valor que contiene el nodo
        self.numero = numero
        #apunta a nuestro siguiente nodo
        self.siguiente = None
        #clase que va a admitir todos los nodos
        class listaEnlazada:
            def __init__(self):
                self.head=None
                def insertar_nodo_al_inicio(self,numero):
                    nuevo_nodo=nodo(numero)
                    if(self.head==None):
                        self.head=nodo(numero)
                        return
                    nuevo_nodo.siguiente=self.head
                    self.head=nuevo_nodo
                def insertar_nodo_al_final(self,numero):
                    nuevo_nodo=nodo(numero)
                    if(self.head==None):
                        self.head=nuevo_nodo
                        return
                    actual=self.head
                    while(actual.siguiente):
                        actual=actual.siguiente
                    actual.siguiente=nuevo_nodo
                    def imprimir_lista(self):
                        actual=self.head
                        while(actual):
                            print(actual.numero,"->",end="")
                            actual=actual.siguiente
                            print("None")
                            mi_lista=listaEnlazada()
                            mi_lista.insertar_nodo_al_inicio(5)
                            mi_lista.insertar_nodo_al_inicio(4)
                            mi_lista.insertar_nodo_al_inicio(3)
                            mi_lista.imprimir_lista()
