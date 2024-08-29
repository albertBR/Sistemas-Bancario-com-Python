#Importei datetime para registrar a hora e data das transições.
import datetime

# Registro de transições.
movimentacoes = []
saques_diarios = 0
limite_saque_dia = 3
limite_saque_valor = 500

def mostrar_extrato(movimentacoes):
    if movimentacoes:
        print("Extrato da conta:")
        for transacao in movimentacoes:
            print(transacao)
        else:
            print("Sem saldo em sua conta.")

def mostrar_saldo(saldo):
    print(f"Saldo: R$ {saldo:.2f}")

def menu_inicial():
    saldo = 0
    saques_diarios = 0
    data_ultimo_saque = datetime.date.today()
    
    print("Bem vindo ao Gerenciador de Conta!")
    
    while True:
        
        operacao_selecionada = print("\nEscolha uma opção: Digite 1 para extrato, 2 para depóstio e 3 para saque. ")
        
        if operacao_selecionada == '1':
            mostrar_extrato(movimentacoes)
            mostrar_saldo(saldo)
        elif operacao_selecionada == '2':
            valor_deposito = input("Valor do depósito: R$ ")
            # Criei um bloco para não encerrar a operação
            try:
                valor_deposito = float(valor_deposito)
                if valor_deposito > 0:
                    saldo += valor_deposito
                    now = datetime.datetime.now()
                    movimentacoes.append(f"Depósito: R$ {valor_deposito:.2f} - Saldo: R$ {saldo:.2f}")
                else:
                    print("Valor inválido. Tente novamente.")
            except ValueError:
                print("Por favor, Insira um valor válido.") 
        elif operacao_selecionada == '3':
             today = datetime.date.today()
             if today != data_ultimo_saque:
                 saques_diarios = 0
                 data_ultimo_saque = today
        
             if saques_diarios >= limite_saque_dia:
                print(f"Você excedeu o limite de saques diários ({limite_saque_dia}).") 
                continue
        
             saque_selecionado = input("Valor do saque: R$ ")
             try:
                 saque_selecionado = float(saque_selecionado)
                 if saque_selecionado > 0 and saque_selecionado <= saldo:
                     if saque_selecionado <= limite_saque_valor:
                         saldo -= saque_selecionado
                         now = datetime.datetime.now()
                         movimentacoes.append(f"Saque: R$ {saque_selecionado:.2f} - Saldo: R$ {saldo:.2f}")
                         saques_diarios += 1
                         data_ultimo_saque = today
                     else:
                         print("Valor do saque excede o limite permitido.")
                 else:
                     print("Valor inválido. Tente novamente.")
             except ValueError:
                 print("Por favor, insira um número válido. ")
        else:
             print("Opção inválida. Tente novamente.")

menu_inicial()
         
                  
             
                  
        