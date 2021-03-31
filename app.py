from flask import Flask,render_template,request,url_for,flash,redirect
from flask_mysqldb import MySQL

app=Flask(__name__)
app.secret_key="hi"

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='crud'

mysql=MySQL(app)

@app.route('/')
def Index():
    con=mysql.connection.cursor()
    con.execute("SELECT * FROM students")
    data=con.fetchall()
    con.close()
    return render_template('index.html',fetch=data)

@app.route('/insert',methods=['POST'])
def insert():
    if(request.method=="POST"):
        flash("Insert Successfull")
        name=request.form['name']
        cas=request.form['class']
        con=mysql.connection.cursor()
        con.execute("INSERT INTO students(name,class)VALUES(%s,%s)",(name,cas))
        mysql.connection.commit()
        return redirect(url_for('Index'))
    
@app.route('/delete/<string:id_data>',methods=['GET'])
def delete(id_data):
    flash("Delete Successfully")
    con=mysql.connection.cursor()
    con.execute("DELETE FROM students WHERE id=%s",(id_data))
    mysql.connection.commit()
    return redirect(url_for('Index')) 

@app.route('/update/<string:id_data>',methods=['POST','GET'])
def update(id_data):
    flash("Update Successfully")
    name=request.form['name']
    cas=request.form['class']
    con=mysql.connection.cursor()
    con.execute("UPDATE students SET name=%s,class=%s WHERE id=%s",(name,cas,id_data))
    mysql.connection.commit()
    return redirect(url_for('Index')) 
    

if __name__=="__main__":
    app.run(debug=True)
