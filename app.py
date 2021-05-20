#import Flask
from flask import Flask, render_template,request
import pickle
import catboost
#create an instance of Flask
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict/', methods=['GET','POST'])
def predict():
    
    if request.method == "POST":
        
        #get form data
        temperature = request.form.get('temperature')
        vaccum = request.form.get('vaccum')
        pressure = request.form.get('pressure')
        humidity = request.form.get('humidity')
        result = predict_energy(temperature,vaccum,pressure,humidity)
        
        
        return render_template('prediction.html',prediction = result)
    pass


def predict_energy(temperature,vaccum,pressure,humidity):
    loaded_model = pickle.load(open('model.pkl', 'rb'))
    result = loaded_model.predict([[temperature,vaccum,pressure,humidity]])
    return result

if __name__ == '__main__':
    app.run(debug=True)