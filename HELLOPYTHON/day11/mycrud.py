from flask import Flask, render_template, request
from day11.mydao_emp import DaoEmp

app = Flask(__name__)

@app.route('/')
@app.route('/list')
def list():
    de = DaoEmp()
    mylist = de.myselect()
    return render_template('list.html',mylist=mylist)

@app.route('/select',methods=['GET','POST'])
def select():
    de = DaoEmp()
    e_id=request.args.get('e_id')
    myinfo = de.myselect2(e_id)
    return render_template('select.html',myinfo=myinfo)

@app.route('/insert2',methods=['GET','POST'])
def insert2():
    de = DaoEmp()
    e_id=request.form.get('e_id')
    e_name=request.form.get('e_name')
    birth=request.form.get('birth')
    
    cnt = de.myinsert(e_id, e_name, birth)
    mylist = de.myselect()
    return render_template('list.html',mylist=mylist)

@app.route('/insert',methods=['GET','POST'])
def insert():
  
    return render_template('insert.html')

@app.route('/update',methods=['GET','POST'])
def update():
    de = DaoEmp()
    e_id=request.args.get('e_id')
    myinfo = de.myselect2(e_id)
    return render_template('select.html',myinfo=myinfo)
if __name__ == '__main__':
    app.run(debug=True)