import requests
from flask import Flask,render_template 
app = Flask(__name__)

def error(message, errorCode):
    return render_template('error.html', customMessage=message, code=errorCode)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/genres')
def genersPage():
    result = requests.get('https://librarymanagementpw.azurewebsites.net/api/gere')
    if (result.status_code == 200):
        return render_template('genres.html', json=result.json() , len=len(result.json()))
    else:
        return error(result.json(),result.status_code)

@app.route('/genres/<id>')
def genreId(id):
    result2 = requests.get(f'https://librarymanagementpw.azurewebsites.net/api/genre/{id}')
    if (result2.status_code == 200):
        return result2
    else:
        return error(result2.json(),result2.status_code)

@app.route('/video/<id>')
def videos(id):
    return f'Stai guardando il video {id}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)