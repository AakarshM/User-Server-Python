from flask import *
import os


app = Flask(__name__)

#secret = os.urandom(10)
#print(secret)
#secret_key = "b\x8aF3\xcc\x9d\xa5M\x82\x88"


@app.route('/')
def index():
    return "welcome"



@app.route('/check', methods=['POST'])
def check():
     params = request.args
     print(params)
     if 'user' in session:
         return "logged in"
     else:
         return "No one logged in"


@app.route('/login', methods=['POST'])
def loginUser():
    data = request.get_json()
    email = data['email']
    password = data['password']


@app.route('/logout', methods=['DELETE'])
def logout():
    if 'user' in session:
        session.pop('user', None)
        return "User logged out"
    else:
        return "No user logged in"




if __name__ == "__main__":
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    app.run()