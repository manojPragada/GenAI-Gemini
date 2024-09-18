from flask import Flask, render_template, request
from waitress import serve
from main import askGemini

app = Flask(__name__)
@app.route('/')
@app.route('/index')
def index():
    return render_template('home.html')

@app.route('/submit-message', methods=['POST'])
def submitmessage():
    message = request.form['message']
    return askGemini(message)

if __name__ == '__main__':
    # app.run(debug=True, host='0.0.0.0', port=8080)
    serve(app, host='0.0.0.0', port=8080)
    