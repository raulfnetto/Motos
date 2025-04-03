#Class Moto - Raul Netto Code

class Moto:

    total_moto = 0
    lista_moto = []

#Declaração de Funções
    def __init__(self,marca,modelo,cilindrada):
        self.marca = marca
        self.modelo = modelo
        self.cilindrada = cilindrada

        Moto.total_moto += 1

        Moto.lista_moto.append(self)

    def exibir_detalhes(self):
        print(f"Moto {self.marca}, do modelo: {self.modelo} com {self.cilindrada} de cilindradas.")

#Métodos
    #Quantidade de motos
    @classmethod
    def listar_motos(cls):
        if cls.lista_moto:
            print("\nLista de motos cadastradas:")
            for moto in cls.lista_moto:
                print(f"- {moto.marca} {moto.modelo} ({moto.cilindrada}cc)")
        else:
            print("Não há motos cadastradas.")

    @classmethod
    def quantidade_motos(cls):
        print(f"Total de motos criadas: {cls.total_moto}")
    #Remover motos
    @classmethod   
    def remover_moto(cls):
        if cls.total_moto >0:
            cls.total_moto -= 1
            print("Uma moto foi removida.")
        else:
            print("Não há motos para remover")
    #Remover moto específica
    @classmethod
    def remover_moto_especifica(cls,modelo):
        for moto in cls.lista_moto:
            if moto.modelo == modelo:
                cls.lista_moto.remove(moto)
                cls.total_moto -= 1
                print(f"Moto {moto.modelo} foi removida com sucesso!")
                return
        print(f"Moto {modelo} não encontrada.")
     
#Declaração de Motos
moto1 = Moto("Yamaha","Fazer 250ys",250)
moto2 = Moto("Dafra","Kansas",150)
moto3 = Moto("Yamaha","MT03",300)

#Chamamento de Funções
moto1.exibir_detalhes()
moto2.exibir_detalhes()
moto3.exibir_detalhes()

Moto.listar_motos()

Moto.quantidade_motos()

Moto.remover_moto_especifica("Kansas")

Moto.quantidade_motos()

