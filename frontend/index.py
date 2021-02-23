from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def index():

    req_data = requests.get('http://backend-service')
    json_data = req_data.json()

    return render_template('index.html', json_data=json_data)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
