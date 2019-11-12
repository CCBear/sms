from flask import Flask, render_template, redirect, url_for, request
import calendar
import os

app = Flask(__name__)

@app.route('/')

@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    return render_template('index.html', title='Home', user=user)

@app.route('/scheduleapp')
def scheduleapp():
   # user = {'username': 'Miguel'}
    return render_template('scheduleapp.html') #, title='Home', user=user)

@app.route('/mission')   
def mission():
    return render_template('mission.html')

@app.route('/about')
def about():
    return render_template('about.html')
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return render_template('mission.html')
    return render_template('login.html', error=error)

@app.route('/calenderDay')
def calenderDay():
    
    #Python is amazing
#Create ASCII-Char HTML Table
 
    strTable = "<html><table><tr><th>Char</th><th>ASCII</th></tr>"
 
    for num in range(33,48):
        symb = chr(num)
        strRW = "<tr><td>"+str(symb)+ "</td><td>"+str(num)+"</td></tr>"
        strTable = strTable+strRW
 
    strTable = strTable+"</table></html>"
 
       # hs = open("calenderDay.html", 'w')
       # hs.write(strTable)
 
       # print strTable
    return render_template('calenderDay.html')


if __name__ == '__main__':
    app.run(debug=True)

# Route for handling the login page logic

