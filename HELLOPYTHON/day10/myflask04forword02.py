from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def home():
    mylist = ["최윤성","김이현","공슬기","김민지"]
    return render_template('myflask03.html',list=mylist)
if __name__ == '__main__':
    app.run(debug=True)