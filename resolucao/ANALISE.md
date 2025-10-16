1️ Problemas no código original

ProcessadorDePedidos fazia tudo: processar pedido, pagar e notificar → quebra SRP.

Para adicionar pagamento ou notificação nova: era necessário mudar o processador → quebra OCP.

Processador dependia de classes concretas (cartão, boleto) → quebra DIP.

2️ Refatoração

Criamos abstrações: MetodoPagamento e Notificador.

Cada pagamento ou notificador ficou em uma classe própria.

O processador apenas orquestra o pedido, chamando os métodos das abstrações.

3️ Vantagens da refatoração

SRP: Cada classe tem uma única responsabilidade.

OCP: É fácil adicionar novos pagamentos ou notificadores sem mudar o processador.

DIP: O processador depende de abstrações, não de implementações concretas.

Flexível: Podemos adicionar Pix, SMS ou outras formas de pagamento e notificação facilmente.