# Reprocessamento de Pedidos Omie

Este projeto tem como objetivo automatizar o reprocessamento de pedidos via API da Omie. Ele lê um arquivo de IDs de pedidos, envia cada um para a API e registra os resultados em um log.

## Estrutura do Projeto

```
ReprocessamentoOmie/
│-- main.py
│-- pedidosId.txt
│-- logs/
│   ├── envios.log
│-- README.md
│-- requirements.txt
│-- .gitignore
```

## Funcionalidades

### `PedidoProcessor`
A classe principal do projeto, responsável por gerenciar todo o fluxo de processamento dos pedidos.

#### Métodos:
- **`__init__(self, file_path)`**: Inicializa o objeto com o caminho do arquivo de pedidos e configura os diretórios necessários.
- **`ler_pedidos(self)`**: Lê os pedidos do arquivo `pedidosId.txt`. Retorna uma lista de pedidos ou um erro caso o arquivo esteja vazio.
- **`enviar_pedido(self, pedido_id)`**: Envia um pedido individualmente para a API e registra o status do envio.
- **`registrar_log(self, mensagem)`**: Registra as mensagens de status no arquivo `logs/envios.log`.
- **`processar_pedidos(self)`**: Executa o fluxo completo de leitura e envio de pedidos, com um intervalo de 5 segundos entre cada requisição.

## Como Utilizar

### **Configurando o projeto em outro computador**

1. **Clonar o repositório:**
   ```sh
   git clone https://github.com/SamuelSPrado/Reprocessamento-de-Pedidos
   cd ReprocessamentoOmie
   ```

2. **Criar um ambiente virtual (opcional, mas recomendado):**
   ```sh
   python -m venv .venv
   ```

3. **Ativar o ambiente virtual:**
   - **Windows:**
     ```sh
     .venv\Scripts\activate
     ```
   - **Mac/Linux:**
     ```sh
     source .venv/bin/activate
     ```

4. **Instalar dependências:**
   ```sh
   pip install -r requirements.txt
   ```

5. **Preencher o arquivo `pedidosId.txt`** com os IDs dos pedidos, um por linha.

6. **Executar o script:**
   ```sh
   python main.py
   ```

7. **Verificar os logs:** Os resultados das requisições serão armazenados em `logs/envios.log`.

## Tratamento de Erros

- Caso o arquivo `pedidosId.txt` não exista, o programa exibe uma mensagem de erro.
- Se o arquivo estiver vazio, o sistema retorna um erro informando a situação.
- Exceções de requisições HTTP são tratadas e registradas no log.

## Melhorias Futuras
- Implementar de um sistema de reenvio para pedidos com erro.
- Suporte para múltiplas threads e processamento paralelo.
