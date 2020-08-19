from flask import Flask, request, jsonify, render_template


app=Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/math', methods=['POST'])
def math_operations():
    if request.json is not None:
        operation = request.json['operation']
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])
        if(operation=='add'):
            result = num1 + num2
        if(operation=='sub'):
            result = num1 - num2
        if(operation=='mul'):
            result = num1 * num2
        if(operation=='div'):
            result = num1 / num2

        print(result)
        return jsonify(result)
    else:
        return(jsonify('The request is not correct'))





if __name__=='__main__':
    print("app is running")
    app.run()