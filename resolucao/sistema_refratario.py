from abc import ABC, abstractmethod

class MetodoPagamento(ABC):
    @abstractmethod
    def pagar(self, pedido):
        pass

class Notificador(ABC):
    @abstractmethod
    def notificar(self, pedido):
        pass



class PagamentoCartao(MetodoPagamento):
    def pagar(self, pedido):
        print(f"Pagando R${pedido['valor']} com cartao de credito...")

class PagamentoBoleto(MetodoPagamento):
    def pagar(self, pedido):
        print(f"Gerar boleto de R$ {pedido['valor']}...")     

class PagamentoPix(MetodoPagamento):
    def pagar(self, pedido):
        print(f"pagamento via PIX Realisado de R$ {pedido['valor']}...")          


class NotificadorEmail(Notificador):
    def notificar(self, pedido):
        print(f"Enviando e-mail para {pedido['cliente_email']}...")

class NotificadorSMS(Notificador):
    def notificar(self, pedido):
        print(f"Enviando SMS para {pedido['cliente_telefone']}...")

# --- outras clasess de pagamento e notificadores

class ProcessadorDePedidos:
    def __init__(self, pagamento, notificador):
        self.pagamento = pagamento
        self.notificador = notificador

    def processar(self, pedido):
        print(f"Processando pedido #{pedido['id']}...")
        self.pagamento.pagar(pedido)
        self.notificador.notificar(pedido)
        pedido['status'] = 'concluido'
        print("Pedido concluído!\n")

# --- bloco principal ---
if __name__ == "__main__":
    # Passo 1: criar um pedido de exemplo
    pedido1 = {
        'id': 1001,
        "valor": 250,
        "cliente_email": "cliente@exemplo.com",
        "cliente_telefone": "11999999999",
        'status': 'pendente'

    }

    # teste de combinaçoes
  
    combinacoes = [ 
    (PagamentoCartao(),  NotificadorEmail()),
    (PagamentoPix(),  NotificadorSMS()),
    ( PagamentoBoleto(), NotificadorEmail()),
    ]


    for pagamento, notificador in combinacoes:
        processador = ProcessadorDePedidos(pagamento, notificador)
        processador.processar(pedido1)


      