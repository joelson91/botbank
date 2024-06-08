# Bot Bank
## Bot de Banco Virtual para Telegram

Este é um bot simples para Telegram que simula um banco virtual, permitindo aos usuários verificar seu saldo, fazer depósitos e saques.

### Funcionalidades:

* **Ver Saldo:** Exibe o saldo atual do usuário.
* **Depositar:** Permite ao usuário adicionar dinheiro à sua conta virtual.
* **Sacar:** Permite ao usuário retirar dinheiro da sua conta virtual (com validação de saldo).
* **Sair:** Encerra a interação com o bot.

### Como Usar:

1. **Crie um bot no Telegram:**
   - Converse com o BotFather (@BotFather) no Telegram e siga as instruções para criar um novo bot.
   - Anote o token do seu bot, pois você precisará dele para executar o código.

2. **Instale as Dependências:**
   - Certifique-se de ter o Python instalado em seu sistema.
   - Instale a biblioteca `pyTelegramBotAPI`:
     ```bash
     pip install pyTelegramBotAPI
     ```

3. **Configure o Bot:**
   - Abra o arquivo `seu_codigo.py` (substitua pelo nome do seu arquivo) e insira o token do seu bot na variável `API_TOKEN`.

4. **Execute o Bot:**
   - No terminal, execute o comando:
     ```bash
     python seu_codigo.py
     ```

5. **Interaja com o Bot:**
   - Inicie uma conversa com o seu bot no Telegram e envie o comando `/start`.
   - Use os botões inline para interagir com o bot e realizar as operações desejadas.

### Estrutura do Código:

* **`saldos`:** Dicionário para armazenar os saldos dos usuários.
* **`home(chat_id)`:** Função para exibir o menu principal com as opções.
* **`menu_keyboard()`:** Função para criar o teclado inline com os botões.
* **`depositar(message)`:** Função para processar depósitos, incluindo validação de entrada.
* **`sacar(message)`:** Função para processar saques, incluindo validação de saldo.
* **`start(message)`:** Manipulador do comando `/start`, inicializa o saldo do usuário e exibe o menu principal.
* **`callback_handler(call)`:** Manipulador de callbacks dos botões inline, executa a ação correspondente a cada botão.

### Melhorias Futuras:

* **Persistência de Dados:** Usar um banco de dados para armazenar os saldos dos usuários.
* **Autenticação:** Adicionar um sistema de autenticação para garantir a segurança das contas.
* **Mais Funcionalidades:** Implementar transferências entre contas, histórico de transações, extrato, etc.

### Observações:

* Este é um exemplo básico de um bot de banco virtual. Para uso em produção, é importante implementar medidas de segurança e persistência de dados.
* Este bot foi desenvolvido usando a biblioteca `pyTelegramBotAPI`. Consulte a documentação da biblioteca para obter mais informações sobre suas funcionalidades.

---

**Observação:** Substitua `SEU_TOKEN_AQUI` pelo token real do seu bot e `seu_codigo.py` pelo nome do arquivo onde você salvou o código.

**Licença:**

Este projeto está licenciado sob a licença MIT - veja o arquivo `LICENSE` para mais detalhes.