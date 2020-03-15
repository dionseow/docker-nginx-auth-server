from flask import Flask, request, Response
app = Flask(__name__)

@app.route("/auth")
def hello():
    print('1')
    if request.method == 'GET':
        if 'number' in request.headers:
            num = request.headers.get('number')
            print(num)
            if num == '12345':
                print('authenticated')
                return Response("{'message': 'Successfully authenticated'}",
                        status=200, mimetype='application/json')
    return Response("{'message': 'Failed'}", status=404, mimetype='application/json')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)
