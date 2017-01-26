from flask import *
import bcrypt
import user
import todo
import json
from validate_email import validate_email

app = Flask(__name__)

test_string = "AakarshM"
hashed = bcrypt.hashpw(test_string.encode('utf-8'), bcrypt.gensalt())
#check = bcrypt.checkpw("garo".encode('utf-8'), hashed)
check2 = bcrypt.checkpw("AakarshM".encode('utf-8'), hashed)

print(check2)

@app.route('/')
def index():
    return "welcome"

@app.route('/createuser', methods=['POST'])
def createUser():
    data = request.get_json()
    email = data['email'].lower()
    password = data['password']
    is_valid = validate_email(email)
    print(str(is_valid) + "  " + email)
    if len(password) < 7:
        return "Password is too short"
    if is_valid == False:
        return "Email is invalid"
    else:
        hashedpw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        creation = user.create_user(email, hashedpw)
        if not creation:
            return "Error, user already exists with the email"
            print(str(creation))
        else:
         return "User created with email: " + email

@app.route('/login', methods=['POST'])
def loginUser():
    data = request.get_json()
    email = data['email']
    password = data['password']
    verifyUser = user.verify_user(email, password.encode('utf-8'))
    if verifyUser:
        session['auth'] = email
        return "Success"
    else:
        return "Failed; incorrect password"


@app.route('/changepassword',methods=['PATCH'])
def changePassword():
    data = request.get_json()
    email = data['email']

@app.route('/logout', methods=['DELETE'])
def logout():
    if 'auth' in session:
        session.pop('auth', None)
        return "User logged out"
    else:
        return "No user logged in"

@app.route('/ct', methods=['POST'])
def ct():
    todo.create_todo()

@app.route('/gt', methods=['GET'])
def gt():
    logged_in_email = session['auth']
    if not logged_in_email:
        return "Nothing"
    else:
        r = todo.retrieve_todo(logged_in_email)
        obj = {"items": r, "user": logged_in_email}
        return jsonify(obj)



if __name__ == "__main__":
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?.RT'
    app.run()
