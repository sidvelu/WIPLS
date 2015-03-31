from flask import Flask, render_template, request
import os, logging
from multiprocessing import Process
app = Flask(__name__)

#Surpress Messages
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

class okayScript(Process):
    def __init__(self):
        Process.__init__(self)
    def run(self):
        execfile("XBeeControl_okay.py", globals(), locals())

#Initialize Mag and CScript Procees
okayXbee = okayScript()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST' and request.form['submit'] == 'Start':
        okayXbee.start()
        print "Control Script Launched"
        os.system("python XBeeControl_send.py control")
        return render_template('/MapOverlay.html')

    if request.method == 'POST' and request.form['submit'] == 'Stop':
        okayXbee.terminate()
        print "Stopping Control"
        os.system("python XBeeControl_send.py stop")
        return render_template('/MapOverlay.html')

    if request.method == 'POST' and request.form['submit'] == 'Kill':
        print "Killing Control"
        os.system("python XBeeControl_send.py kill")
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
