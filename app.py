from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/ping')
def ping():
    # Grabbing user input from the website URL
    host = request.args.get('host')
    
    # VULNERABILITY: Command Injection! 
    # Never put user input directly into an OS command
    os.system("ping -c 1 " + host)
    
    return "Pinged the host!"

if __name__ == '__main__':
    app.run(debug=True)
