from twilio.rest import Client

import datetime

# Substitua as informações abaixo pelas suas credenciais do Twilio
TWILIO_ACCOUNT_SID = 'ACaabb4fa240fe829a585826090de12843'
TWILIO_AUTH_TOKEN = 'c3a975a14bfab202bc0fe0c1db22b8d7'
TWILIO_PHONE_NUMBER = '+15736854272'  
# Número de telefone fornecido pelo Twilio

def enviar_sms(mensagem, numero_destinatario):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    mensagem = client.messages.create(
        body=mensagem,
        from_=TWILIO_PHONE_NUMBER,
        to=numero_destinatario
    )
    print(f"SMS enviado para {numero_destinatario}: {mensagem.sid}")

def tarefas_diarias():
    tarefas = [
        "Lavar as louças",
        "Limpar o fogão",
        "Retirar o lixo",
        "Varrer ou passar o aspirador de pó",
        "Passar um pano úmido no chão",
        "Organizar as coisas espalhadas",
        "Arrumar as camas",
        "Lavar a roupa (depende do volume de roupa)"
    ]

    mensagem = "Tarefas diárias:\n" + "\n".join(tarefas)
    return mensagem

def tarefas_semanais():
    tarefas = {
        "Segunda-feira": ["Trocar as toalhas"],
        "Terça-feira": ["Limpar o forno"],
        "Quarta-feira": ["Lavar o banheiro"],
        "Quinta-feira": ["Trocar a roupa de cama"],
        "Sexta-feira": ["Limpar o interior do micro-ondas"],
        "Sábado": ["Tirar o pó dos móveis e objetos"],
        "Domingo": ["Lavar o banheiro"]
    }

    mensagem = "Tarefas semanais:\n"
    for dia, tarefas_dia in tarefas.items():
        mensagem += f"{dia}:\n"
        for tarefa in tarefas_dia:
            mensagem += f"- {tarefa}\n"
    
    return mensagem

def tarefas_mensais():
    tarefas = {
        1: ["Organizar guarda-roupas"],
        2: ["Limpar os armários da cozinha"],
        15: ["Virar os colchões"],
        20: ["Limpar a máquina de lavar"]
    }

    mensagem = "Tarefas mensais:\n"
    for dia, tarefas_dia in tarefas.items():
        if isinstance(dia, int):
            mensagem += f"Dia {dia}:\n"
        else:
            mensagem += f"{dia}:\n"
        for tarefa in tarefas_dia:
            mensagem += f"- {tarefa}\n"
    
    return mensagem

# Solicitar o número de celular para enviar os SMS
numero_destinatario = input("Digite o número de celular para enviar os SMS (formato: +5511xxxxxxxxx): ")

# Obter as mensagens das tarefas
mensagem_diarias = tarefas_diarias()
mensagem_semanais = tarefas_semanais()
mensagem_mensais = tarefas_mensais()

# Enviar os SMS
enviar_sms(mensagem_diarias, numero_destinatario)
enviar_sms(mensagem_semanais, numero_destinatario)
enviar_sms(mensagem_mensais, numero_destinatario)
