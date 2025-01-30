from flask import Flask
import time
app = Flask(__name__)

@app.route('/name')
def get_name():
    return 'AWS MASTERCHEF'

@app.route('/version')
def get_version():
    return 'vl.0.0'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)