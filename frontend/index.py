from flask import Flask, render_template
import requests

app = Flask(__name__)

def check_connection(api_route):
    try:
        req_data = requests.get('http://backend-service:5001'+api_route)
        json_data = req_data.json()
    except:
        json_data = 'Backend service is down'
    return json_data
    
@app.route('/', methods=['GET'])
def index():

    json_data = check_connection('/')

    return render_template('index.html', json_data=json_data)

@app.route('/products', methods=['GET'])
def products():

    json_data = check_connection('/products')

    return render_template('index.html', json_data=json_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
