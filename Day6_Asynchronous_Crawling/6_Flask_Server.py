from flask import Flask
import time

app = Flask(__name__)


@app.route('/AAA')
def index_AAA():
    time.sleep(2)
    return 'Hello AAA'

@app.route('/BBB')
def index_BBB():
    time.sleep(2)
    return 'Hello BBB'

@app.route('/CCC')
def index_CCC():
    time.sleep(2)
    return 'Hello CCC'

if __name__=='__main__':
    app.run(threaded=True)