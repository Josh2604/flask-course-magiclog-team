from flask import Flask,render_template,request

app = Flask(__name__)


@app.route('/name', methods=['GET','POST'])
@app.route('/name/<string:name>')
def sumar(**args):
    print(args)
    return ""

@app.route('/', methods=['GET'])
def index():
    name = request.args.get("name")
    print("this is the name", name)
    return "Hola mundo!!!"

@app.route('/render', methods=['GET'])
def render():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)