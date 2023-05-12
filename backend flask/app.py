from  flask import Flask,render_template,request

app=Flask(__name__)

#New change

@app.route("/test",methods=['GET'])
def test():

    return "API is working"

@app.route("/")
def defualt():
    return "Working"

@app.route("/forecast")
def forecast():
    return "hello world"

@app.route("/postjson",methods=['POST'])
def json():
    #json that is being inputted
    op=request.json["name"]

    
    print(op)
    return "JSON received"

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response


if (__name__=="__main__"):
    app.run(debug=True)