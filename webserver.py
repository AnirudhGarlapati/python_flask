from flask import Flask
import requests
import logging

app = Flask(__name__)

logging.basicConfig(filename='record.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')


@app.route("/")
def home():
    response = requests.get("https://6god8pgyzf.execute-api.us-west-2.amazonaws.com/databases")
    return str(response.json())


if __name__ == "__main__":
    app.run(host='localhost', debug=False)
