from flask import Flask, render_template, request, send_from_directory
import os, logging
from multiprocessing import Process
app = Flask(__name__, static_folder='assets')

#Surpress Messages
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        requestString = request.form['submit']

        if requestString == 'Start':
            print "Control Script Launched"
            os.system("python XBeeControl_send.py control")
            return render_template('/MapOverlay.html')

        if requestString == 'Stop':
            print "Stopping Control"
            os.system("python XBeeControl_send.py stop")
            return render_template('/MapOverlay.html')

        if requestString == 'Kill':
            print "Killing Control"
            os.system("python XBeeControl_send.py kill")
            return render_template('/MapOverlay.html')

        if requestString == 'Align':
            print "Moving Left"
            os.system("python XBeeControl_send.py align")
            return render_template('/MapOverlay.html')

        if 'up' in requestString or 'down' in requestString or 'left' in requestString or 'right' in requestString:
            params = requestString.split()
            print "Moving tracker " + params[0]
            os.system("python XBeeControl_send.py " + params[0] + params[1])
            return render_template('/MapOverlay.html')
        '''

        if 'down' in requestString:
            print "Moving tracker down"
            tracker = requestString.split()[1]
            #os.system("python XBeeControl_send.py down" + tracker)
            return render_template('/MapOverlay.html')
        '''
    
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

@app.route('/assets/<filename>')
def get_image(filename):
    print filename
    return send_from_directory(app.static_folder, filename)

if __name__ == '__main__':
    app.run(
            port=int("8080")
            )
