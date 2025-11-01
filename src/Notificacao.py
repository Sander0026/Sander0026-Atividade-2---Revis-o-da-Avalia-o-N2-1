from datetime import datetime

# Função que consome a FilaOrdemServico e envia notificações
# para o cliente e equipe logística sobre a nova Ordem de Serviço.

def Notificacao(FilaOrdemServico):

    if FilaOrdemServico.empty():
        print("Nenhuma Ordem de Serviço na fila para notificação.")
        return

    while not FilaOrdemServico.empty():
        os_dados = FilaOrdemServico.get()

        # Monta mensagem simulada
        mensagem_cliente = (
            f"\nNotificação enviada para {os_dados['Cliente']}:\n"
            f"Pedido {os_dados['PedidoID']} está pronto para expedição.\n"
            f"Ordem de Serviço: {os_dados['OS_ID']}\n"
            f"Galpão responsável: {os_dados['Galpao']} ({os_dados['Localizacao_Galpao']})\n"
            f"Distância estimada: {os_dados['Distancia_KM']} km\n"
            f"Gerado em: {os_dados['Data_Geracao']}\n"
        )

        mensagem_logistica = (
            f"\n Para equipe logística:\n"
            f"Nova OS registrada ({os_dados['OS_ID']})\n"
            f"Cliente: {os_dados['Cliente']}\n"
            f"Produto: {os_dados['Produto']}\n"
            f"Galpão: {os_dados['Galpao']}\n"
            f"Distância até o cliente: {os_dados['Distancia_KM']} km\n"
            f"Status atual: {os_dados['Status']}\n"
        )

        # Atualiza o status interno
        os_dados["Status"] = "NOTIFICADO"
        os_dados["Data_Notificacao"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Exibe notificações
        print(mensagem_cliente)
        print(mensagem_logistica)
        print(f"OS {os_dados['OS_ID']} marcada como NOTIFICADA.\n")