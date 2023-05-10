from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

# Load regression pickle files
regression_model_1 = pickle.load(open('models/Cooling_model.pkl', 'rb'))
regression_model_2 = pickle.load(open('models/Heating_model.pkl', 'rb'))

# Load classification pickle file
classification_model = pickle.load(open('models/Classification_model.pkl', 'rb'))


@app.route('/')
def home_page():
    return 'Welcome to Energy_Efficiency Regression and classification model'


@app.route('/predict/Cooling', methods=['GET', 'POST'])
def predict_cooling():
    if request.method == 'POST':
        Surface_Area = float(request.form['Surface Area'])
        Wall_Area = float(request.form['Wall Area'])
        Overall_Height = float(request.form['Overall Height'])
        Orientation = float(request.form['Orientation'])
        Glazing_Area = float(request.form['Glazing Area'])
        Glazing_Area_Distribution = float(request.form['Glazing Area Distribution'])

        prediction = regression_model_1.predict([[Surface_Area, Wall_Area, Overall_Height, Orientation, Glazing_Area, Glazing_Area_Distribution]])
        return render_template('index.html', prediction=prediction[0])

    return render_template('index.html')



@app.route('/predict/Heating', methods=['GET', 'POST'])
def predict_heating():
    if request.method == 'POST':
        Surface_Area = float(request.form['Surface Area'])
        Wall_Area = float(request.form['Wall Area'])
        Overall_Height = float(request.form['Overall Height'])
        Orientation = float(request.form['Orientation'])
        Glazing_Area = float(request.form['Glazing Area'])
        Glazing_Area_Distribution = float(request.form['Glazing Area Distribution'])

        prediction = regression_model_2.predict([[Surface_Area, Wall_Area, Overall_Height, Orientation, Glazing_Area, Glazing_Area_Distribution]])
        result = "Your cooling load is: " + str(prediction[0])
        
        return render_template('index.html', result=result)

    return render_template('index.html')

@app.route('/predict/Classification', methods=['GET', 'POST'])
def predict_classification():
    if request.method == 'POST':
        Surface_Area = float(request.form['Surface Area'])
        Wall_Area = float(request.form['Wall Area'])
        Overall_Height = float(request.form['Overall Height'])
        Orientation = float(request.form['Orientation'])
        Glazing_Area = float(request.form['Glazing Area'])
        Glazing_Area_Distribution = float(request.form['Glazing Area Distribution'])

        prediction = classification_model.predict([[Surface_Area, Wall_Area, Overall_Height, Orientation, Glazing_Area, Glazing_Area_Distribution]])
        return render_template('index.html', prediction=prediction[0])

    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)
