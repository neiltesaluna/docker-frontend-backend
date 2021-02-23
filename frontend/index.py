from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def index():

    try:
        req_data = requests.get('http://backend-service:5001')
        json_data = req_data.json()
    except:
        json_data = 'Backend service is down'

    return render_template('index.html', json_data=json_data)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
