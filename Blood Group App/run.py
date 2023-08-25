
#Dependencies
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from plyer import notification


app = Flask(__name__)
app.secret_key="Hello"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy()

#creation of database
db = SQLAlchemy(app)
with app.app_context():
    db.create_all()
    
        
#Creating SQLlite table using Model in sqlalchemy   
class Response(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    blood_group = db.Column(db.String(5))
    quantity = db.Column(db.Integer)


#Global Variable
blood_groups = ['A+', 'A-', 'B+', 'B-', 'O+', 'O-', 'AB+', 'AB-']


#Route to http://127.0.0.1:5000/
@app.route('/', methods=['GET', 'POST'])
def home():  
    db.create_all()
    if request.method == "POST" and 'submit' in request.form:
        
        #Retrieving values from HTML "POST" method
        blood_group = request.form['blood_group']
        Name=request.form['Name']
        Age= int(request.form['Age'])
        Quantity= int(request.form['Quantity'])
        
        if Age<18:
            return redirect('/')     
        else:
            
            #creation of object of class Response
            response = Response(blood_group=blood_group, name=Name, age=Age, quantity=Quantity)
            
            db.session.add(response)
            db.session.commit()
            
            #plyer notification
            notification.notify(
                title='Entry Added',
                message='Respond Successfully Addded',
                app_name='Blood Donation Survey',
            )          
            return redirect('/') 
        
    #rendering template home.html and passing values to html file     
    return render_template('home.html', blood_groups=blood_groups)

if __name__ == '__main__':
    app.run(debug=True)
