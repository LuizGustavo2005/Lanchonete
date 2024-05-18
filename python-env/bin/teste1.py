class Cardapio:
    def __init__(self, codigo, nome, preco):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco

    def mostrar_cardapio(self):
        self.cardapio = []

        item1 = Cardapio(100, "Cachorro quente", 1.20)
        item2 = Cardapio(101, "Bauru simples", 1.30)
        item3 = Cardapio(102, "Bauru com ovo", 1.50)
        item4 = Cardapio(103, "Chesseburguer", 1.20)
        item5 = Cardapio(104, "Hambúrguer", 1.30)
        item6 = Cardapio(105, "Refrigerante", 1.00)

        self.cardapio.extend([item1, item2, item3, item4, item5, item6])

        for item in self.cardapio:
            print(f"COD: {item.codigo} {item.nome} R${item.preco:.2f}")

    def receber_pedido(self):
        while True:
            try:
                pedido = int(input("\nDigite o código do lanche: "))

                self.quantidade = int(input("Quantas unidades vai querer?: "))

                for item in self.cardapio:
                    if pedido == item.codigo:
                        print("Pedido anotado!")
                        self.pedido = item
                        return item

                print("Código inválido, tente novamente")

            except ValueError:
                print("Valor inválido")

    def imprimir_notafiscal(self):
        preco_final = self.pedido.preco * self.quantidade
        print(f"************Seu pedido************\n")

        print(f"PEDIDO: {self.quantidade}x {self.pedido.nome}")
        print(f"VALOR FINAL: R${preco_final}")


cardapio = Cardapio(0, "", 0)
cardapio.mostrar_cardapio()
cardapio.receber_pedido()
cardapio.imprimir_notafiscal()

# Created by: Luiz Gustavo
