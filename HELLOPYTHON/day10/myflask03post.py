from flask import Flask, request
app = Flask(__name__)
@app.route("/",methods=['GET','POST'])
def home():
    #return request.args.get('a')
    #a=request.form['a']
    a=request.form.get('a')
    return "post로 전달된 데이터({})".format(a)
if __name__ == '__main__':
    app.run(debug=True)