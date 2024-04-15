import requests
from flask import Flask,render_template 
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/genres')
def genersPage():
    result = requests.get('https://librarymanagementpw.azurewebsites.net/api/genre')

    if (result.status_code == 200):
        return render_template('genres.html', json=result.json() , len=len(result.json()))
    else:
        return render_template('error.html', code=result.status_code)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)