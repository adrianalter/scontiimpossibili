import requests

def send_to_telegram(message):
    bot_token = ''
    bot_chatID = ''
    send_text = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={bot_chatID}&parse_mode=Markdown&text={message}'
    response = requests.get(send_text)
    return response.json()

# Esempio di messaggio
send_to_telegram("Nuova offerta su Amazon: [Blue Yeti Bianco](https://amzn.to/3YAltnK)")
