from flask import Flask,request,render_template,jsonify
import pickle
import pandas as pd
from utils import predict as pre


app= Flask(__name__)

@app.route('/')

def homePage():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method=="POST":
        rate_marriage= float(request.form['rate_marriage'])
        age= float(request.form['age'])
        yrs_married= float(request.form['yrs_married'])
        children= float(request.form['children'])
        religious= float(request.form['religious'])
        educ= float(request.form['educ'])
        occupation= float(request.form['occupation'])
        occupation_husb= float(request.form['occupation_husb'])

        df= pd.DataFrame({
            'rate_marriage': [rate_marriage],
            'age': [age], 
            'yrs_married': [yrs_married], 
            'children': [children], 
            'religious': [religious],
            'educ': [educ],
            'occupation': [occupation],
            'occupation_husb': [occupation_husb]
        })
        predict= pre(df)


    return render_template('results.html', prediction=predict)

if __name__ == '__main__':
    app.run(debug=True)
