from flask import Flask
import requests

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def index():

    req_data = requests.get('http://backend-service')
    return f'''
    <h1>Product list {req_data.text}</h1>
    '''



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
