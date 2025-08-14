from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World111119999922222223333333333!"

if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0')
