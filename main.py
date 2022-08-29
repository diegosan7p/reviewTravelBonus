import pandas as pd
from twilio.rest import Client

account_sid = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" #account sid Twilio
auth_token = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" #account sid Twilio
client = Client(account_sid, auth_token)

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']
for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mes de {mes} alguem bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        message = client.messages.create(
            to="+55119XXXXXXXX", #Your number sms
            from_="+XXXXXXXXXXX", #Your number Twilio
            body=f"No mes de {mes} alguem bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}")
        print(message.sid)