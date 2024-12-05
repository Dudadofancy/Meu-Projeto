class SistemaVoo:
 #FUNÇÃO CONSTRUTOR MÉTODO ONDE INICIA A CLASSE
 
 def __init__(self):
    self.voos = []
    self.reservas = []

 def adicionar_voo(self, voo):
    self.voos.append(voo)

 def exibir_voos(self):
    for i, voo in enumerate(self.voos):
        print(f"{i+1}. {voo.codigo} - {voo.origem} para {voo.destino} - {voo.data} {voo.hora} - R${voo.preco:.2f}")

 def realizar_reserva(self, reserva):
    self.reservas.append(reserva)

 def exibir_reservas(self):
    for i, reserva in enumerate(self.reservas):
        print(f"Reserva {i+1}:")
        print(f"- Voo: {reserva.voo.codigo} - {reserva.voo.origem} para {reserva.voo.destino}")
        print(f"- Passageiro: {reserva.passageiro.nome} - {reserva.passageiro.cpf}")

