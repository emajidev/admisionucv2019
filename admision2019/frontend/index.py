from flask import Flask, render_template, json, request
from pprint import pprint
from admissionsapi.socketserver.go import Go

host = 'localhost'
port = 3010



app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/admin')
def dashboard_admin():
    lista = {'A','B','C','D'}

    return render_template('admin.html',lista=data["student"]['name'])
    
@app.route('/showSignUp',methods=['GET','POST'])
def showSignUp():
    return render_template('signup.html')

@app.route('/signUp',methods=['POST'])
def signUp():
    # create user code will be here !!
    ci = request.form['inputCi']
    email = request.form['inputEmail']
    phone = request.form['inputPhone']
    name = request.form['inputName']
    lastName= request.form['inputlastName']
    # create json for singUp
    data = {
       "student":
           {"ci":ci,
            "email":email,
            "phone":phone,
            "name":name,
            "lastName":lastName,
            }
    }
   
  
  
    jsonSingUp = json.dumps(data)
    DecoSingUp = json.loads(jsonSingUp)

    print("json: "+ jsonSingUp)
    print("json decodificado, estraccion data name: "+ str(DecoSingUp["student"]['name']))
    return ci + email + phone + name +lastName

def cb(fut):
    print('RESULT ----------')
    (header, body) = fut.result()
    print('header:')
    pprint(header)
    print('')
    print('body:')
    pprint(body)
    print('----------')

@app.route('/signIn',methods=['POST'])
def signin():
    # create user code will be here !!
    ci = request.form['inputCi']
    email = request.form['inputEmail']
    body = {
        'ci': ci,
        'email':email,
    }
    token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjp7ImNpIjoyMjU0MDgyMCwiZW1haWwiOiJlcmljQG1haWwuY29tIn0sImV4cCI6MTU3MjQ2MzA5Mn0.37RYLjikjTol0wRKfoxMGlIdQe8B2nlUcLDaVkmoOCI'
    print("conexion")
    Go('POST', '/signIn', host_port = (host, port), body=body).with_callback(cb)
    return "conexion"

if __name__ == '__main__':
    app.run(debug =True)
    
