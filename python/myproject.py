from flask import Flask,render_template,request,redirect
from flask_mysql_connector import MySQL


app= Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] ='root'
app.config['MYSQL_PASSWORD'] ='*****'
app.config['MYSQL_DB'] ='flaskdb'

mysql = MySQL(app)


@app.route('/')
def fn():
    return render_template('pmain.html')

@app.route('/Thanks')
def thanks():
    return render_template('thanks.html')

@app.route('/Sign_up',methods=['GET','POST'])
def psignup():
    if request.method == 'POST':
        userdetails = request.form
        name = userdetails('username')
        name1 = userdetails('lastname')
        email = userdetails('email')
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO details(username,lastname,email) VALUES(%s,%s,%s)",(name,name1,email))
        mysql.connection.commit()
        cur.close()
        return 'success'

    return render_template('psignup.html')

@app.route('/Login')
def plogin():
    return render_template('plogin.html')

@app.route('/About')
def pabout():
    return render_template('pabout.html')

@app.route('/Cart')
def pcart():
    return render_template('pcart.html')

@app.route('/Contact')
def pcontactus():
    return render_template('pcontact.html')

@app.route('/Wishlist')
def pwishlist():
    return render_template('pwishlist.html')


if __name__=='__main__':
    app.run(debug=True)