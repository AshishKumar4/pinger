from flask import *
import hashlib
import json
import os
import time

app = Flask(__name__)
app.secret_key = os.urandom(32)#bytes(str(hex(random.getrandbits(128))), 'ascii')

API_KEY = hashlib.md5(b"I AM ALIVE!!!").hexdigest() # d3261fa60c79562a4b717f3bd3420ccc

@app.errorhandler(404)
def page_not_found(e):
    return render_template("/404.html")

global lastStamp
lastStamp = time.time()

@app.route("/verify/<apiKey>", methods=["GET", "POST"])
def verify(apiKey):
    if apiKey == 'd3261fa60c79562a4b717f3bd3420ccc':
        newStamp = time.time()
        global lastStamp
        lastStamp = newStamp 
        print("GOT VALID REQUEST!")
    return jsonify({'status': 'OK'})

@app.route("/", methods=["GET"])
@app.route("/dashboard", methods=["GET"])
def dashboard():
    global lastStamp
    status = 'Alive! :('
    css = 'is-success'
    if (time.time() - lastStamp) / 60 >= 5: # Check every 5 minutes. Should get ping every minute though
        status = 'Dead :D'
        css = 'is-danger'
    return render_template('/dashboard.html', userStatus=status, colorcss=css)
 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='80')