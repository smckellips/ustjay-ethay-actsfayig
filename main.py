import os

import requests
from flask import Flask, send_file, Response
from bs4 import BeautifulSoup

app = Flask(__name__)


def get_fact():

    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    return facts[0].getText()


@app.route('/')
def home():
    target_url = "https://hidden-journey-62459.herokuapp.com/"
    # initial = get_fact()
    form_data = {'input_text': get_fact()}
    
    response = requests.post(target_url + 'piglatinize/', data=form_data) 
    return response.url


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)

    # home()

