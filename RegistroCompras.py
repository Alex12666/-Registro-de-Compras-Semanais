import os



class RegistroCompras:
    def __init__(self,pasta="compras"):
        self.pasta = pasta

        if not os.path.exists(self.pasta):
            os.makedirs(self.pasta)

            print(f"pasta criada com sucesso{self.pasta}")


        else:
            print(f"Past existente {self.pasta}")





    def salva_Compras(self,numero_de_compras,escricao):
        nome_arquivo = f"{numero_de_compras}.text"

        caminho_copleto = os.path.join(self.pasta,nome_arquivo)

        with open(caminho_copleto,'w',encoding='utf-8') as arquivos:

            arquivos.write(f"compra numero:{numero_de_compras}")

            arquivos.write(f"Decrisâo:{escricao}")

            print(f"Compra{numero_de_compras}salva com sucesso em {caminho_copleto}")


registre = RegistroCompras()  


print("=== REGISTRO DE COMPRAS DA SEMANA ===")



quntidade = int(input("Quantas compras você quer registrar nesta semana? "))


for i in range(1,quntidade + 1):

    print(f"\nCompra {i}:")
    escricao =input("Digite a descrição da compra: ")
    registre.salva_Compras(i,escricao)

    print("\nTodas as compras da semana foram registradas com sucesso.")




