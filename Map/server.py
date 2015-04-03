from flask import Flask, render_template, request
import os, logging
from multiprocessing import Process
app = Flask(__name__)

#Surpress Messages
#log = logging.getLogger('werkzeug')
#log.setLevel(logging.ERROR)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST' and request.form['submit'] == 'Start':
        print "Control Script Launched"
        os.system("python XBeeControl_send.py control")
        return render_template('/MapOverlay.html')

    if request.method == 'POST' and request.form['submit'] == 'Stop':
        print "Stopping Control"
        os.system("python XBeeControl_send.py stop")
        return render_template('/MapOverlay.html')

    if request.method == 'POST' and request.form['submit'] == 'Kill':
        print "Killing Control"
        os.system("python XBeeControl_send.py kill")
        return render_template('/MapOverlay.html')

    if request.method == 'POST' and request.form['submit'] == 'Align':
        print "Moving Left"
        os.system("python XBeeControl_send.py align")
        return render_template('/MapOverlay.html')

    elif request.method == 'GET':
        return render_template('/MapOverlay.html')

def _test(argument):
    return "TEST: %s" % argument

@app.route('/data.json')
def json():
    return render_template('/data.json')

@app.route('/MapOverlayScript.js')
def javaScript():
    return render_template('/MapOverlayScript.js')

if __name__ == '__main__':
    app.run(
            port=int("8080")
            )
