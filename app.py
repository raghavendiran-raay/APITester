from flask import Flask,jsonify, request

app = Flask(__name__)

@app.route('/calculator/greeting', methods=['POST','GET'])
def greeting():
    if request.method == 'GET':
        return "Hello world!"


@app.route('/calculator/add', methods=['POST','GET'])
def add():
    # write your code here...
    return ""


@app.route('/calculator/subtract', methods=['POST','GET'])
def subtract():
    # write your code here...
    return ""

if __name__ == '__main__':

    app.run(host="0.0.0.0",debug=True, port=3000)