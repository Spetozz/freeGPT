from flask import Flask, render_template, request, jsonify
import g4f

from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('chat.html')


@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    return get_Chat_response(input)

def get_Chat_response(promt: str) -> str:
    response = g4f.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": promt}],
    )
    print(response)
    return response

if __name__ == '__main__':
    app.run()
