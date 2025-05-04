from datetime import datetime

def calcular_saldo(transacoes):
    saldo = sum([transacao['valor'] for transacao in transacoes])
    return saldo

def gerar_extrato(transacoes):
    print("\n-------------------- EXTRATO ------------------------")
    saldo_atual = calcular_saldo(transacoes)
    data_extrato = datetime.now().strftime("%d/%m/%Y, às %H:%M:%S")
    print(f"Saldo: R$ {saldo_atual:.2f}       {data_extrato}\n")

    for transacao in transacoes:
        sinal = '+' if transacao['valor'] > 0 else '-'
        valor_formatado = f"{abs(transacao['valor']):.2f}".replace('.', ',')
        data = transacao['data'].strftime("%d/%m/%Y, às %H:%M:%S")
        print(f" {sinal} R$ {valor_formatado}      {data}")
    print("-----------------------------------------------------")

def exibir_menu():
    print("\n--- Menu ---")
    print("1. Ver Saldo")
    print("2. Ver Extrato")
    print("3. Fazer Depósito")
    print("4. Fazer Saque")
    print("5. Sair")

def criar_conta():
    print("\n--- Criação de Conta Bancária ---")
    conta = input("Conta: ")
    agencia = input("Agência: ")
    print(f"\nConta criada com sucesso!\nConta: {conta} | Agência: {agencia}")
    return conta, agencia

def ler_transacoes_input(tipo="depósito"):
    exemplo = "[+100, +200]" if tipo == "depósito" else "[-50, -30]"
    sinal_esperado = '+' if tipo == "depósito" else '-'

    while True:
        entrada = input(f"Digite os valores de {tipo}s (exemplo: {exemplo}): ").strip("[]").replace(" ", "")
        valores = entrada.split(",")

        transacoes = []
        erro = False

        for valor in valores:
            if not valor.startswith(sinal_esperado):
                print("❗ Por favor, indique o sinal à frente do valor.")
                erro = True
                break
            try:
                numero = float(valor)
                if numero == 0:
                    print("❗ O valor não pode ser zero!")
                    erro = True
                    break
                data = datetime.now()
                transacoes.append({"valor": numero, "data": data})
            except ValueError:
                print("❗ Valor inválido! Tente novamente com o formato correto.")
                erro = True
                break

        if not erro:
            return transacoes

def main():
    conta, agencia = criar_conta()

    transacoes = []

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1-5): ")

        if opcao == '1':
            saldo = calcular_saldo(transacoes)
            print(f"Saldo atual: R$ {saldo:.2f}")

        elif opcao == '2':
            gerar_extrato(transacoes)

        elif opcao == '3':
            novos_depositos = ler_transacoes_input("depósito")
            transacoes.extend(novos_depositos)
            print("✅ Depósito(s) registrado(s) com sucesso!")

        elif opcao == '4':
            novos_saques = ler_transacoes_input("saque")
            total_saque = sum([abs(t['valor']) for t in novos_saques])
            saldo_atual = calcular_saldo(transacoes)

            if total_saque > saldo_atual:
                print("❌ Saldo insuficiente para realizar todos os saques.")
            else:
                transacoes.extend(novos_saques)
                print("✅ Saque(s) registrado(s) com sucesso!")

        elif opcao == '5':
            print("👋 Saindo... Obrigado por usar nosso sistema bancário!")
            break

        else:
            print("⚠️ Opção inválida. Tente novamente.")

# Inicia o sistema
main()
