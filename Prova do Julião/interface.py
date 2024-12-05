#IMPORTA AS CLASSES

from sistemadevoo import SistemaVoo
from voo import Voo
from passageiro import Passageiro
from reserva import Reserva

 # Função que inicia o sistema e exibe o menu interativo.
def main():
 sistema = SistemaVoo()

# Loop principal do menu que mantém o programa em execução até que o cliete decida sair.
 while True:
    print("\nSistema de Vôos Baratos")
    print("1. Cadastrar voo")
    print("2. Exibir vôos")
    print("3. Realizar reserva")
    print("4. Exibir reservas")
    print("5. Sair")

 # Solicita ao cliente  que escolha uma opção do menu.
    escolha = input("Escolha: ")

    if escolha == "1":
        codigo = input("Código do voo: ")
        origem = input("Origem: ")
        destino = input("Destino: ")
        data = input("Data (DD/MM/AAAA): ")
        hora = input("Hora (HH:MM): ")
        preco = float(input("Preço: R$"))
        voo = Voo(codigo, origem, destino, data, hora, preco)
        sistema.adicionar_voo(voo)
        print("Voo cadastrado!")

 #Exibe todos os voos cadastrados.
    elif escolha == "2":
        sistema.exibir_voos()

#Realiza uma reserva para um voo específico.
    elif escolha == "3":
        sistema.exibir_voos()
        escolha_voo = int(input("Escolha o voo (0 para cancelar): ")) - 1
       
 # Verifica se o usuário não escolheu cancelar 
        if escolha_voo >= 0:
            nome = input("Nome do passageiro: ")
            cpf = input("CPF: ")
            email = input("E-mail: ")
            passageiro = Passageiro(nome, cpf, email)
            lista_voos = sistema.voos
            print(lista_voos)
            reserva = Reserva(lista_voos[escolha_voo  - 1], passageiro)
            sistema.realizar_reserva(reserva)
            print("Reserva realizada!")

#Exibe todas as reservas feitas.
    elif escolha == "4":
        sistema.exibir_reservas()


    elif escolha == "5":break

    else:
        print("Opção inválida.")




if __name__ == "__main__":
 main()


