from flask import Flask
from flask import request
import subprocess,socket
app = Flask(__name__)

@app.route('/',methods = ['POST', 'GET'])
def mp2_2():
    if request.method == 'POST':
       p = subprocess.Popen(["python", "stress_cpu.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
       output, errors = p.communicate()
       return "SUCCESS"
    else:
       return socket.gethostname()

if __name__ == '__main__':
   app.run()