import os
import time
import requests
from datetime import datetime
from secrets import ENDPOINT


class PedidoProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.api_url = ENDPOINT
        self.log_file = "logs/envios.log"
        os.makedirs("logs", exist_ok=True)

    def ler_pedidos(self):
        try:
            with open(self.file_path, "r") as file:
                pedidos = [line.strip() for line in file.readlines() if line.strip()]
                if not pedidos:
                    raise ValueError("Erro: O arquivo de pedidos está em branco!")
                return pedidos
        except FileNotFoundError:
            print("Arquivo de pedidos não encontrado!")
            return []
        except ValueError as e:
            print(e)
            return []

    def enviar_pedido(self, pedido_id):
        url = f"{self.api_url}{pedido_id}"
        try:
            response = requests.post(url)
            status = response.status_code
            mensagem = "SUCESSO" if status == 200 else f"\nERRO [{status}]\nVerifique se os ID's estão corretos antes de enviar!"
        except requests.RequestException as e:
            mensagem = f"ERRO [{str(e)}]"

        log_msg = f"{datetime.now()} {pedido_id} {mensagem}"
        print(log_msg)
        self.registrar_log(log_msg)

    def registrar_log(self, mensagem):
        with open(self.log_file, "a") as log:
            log.write(mensagem + "\n")

    def processar_pedidos(self):
        pedidos = self.ler_pedidos()
        for pedido_id in pedidos:
            self.enviar_pedido(pedido_id)
            time.sleep(5)  # Aguarda 5 segundos entre cada envio


if __name__ == "__main__":
    processor = PedidoProcessor("pedidosId.txt")
    processor.processar_pedidos()
