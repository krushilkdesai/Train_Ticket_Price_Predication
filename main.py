from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open('random_forest_regression_model.pkl', 'rb'))

@app.route('/', methods=['GET'])
def Home():
    return render_template('index.html')


@app.route("/predict", methods=['POST'])
def predict():
    # Train categories
    Train_Garib_Rath = Train_Humsafar_Express = Train_Jan_Shatabdi_Express = Train_Mahamana_Express = 0
    Train_Rajdhani_Express = Train_Sampark_Kranti_Express = 0
    Train_Shatabdi_Express = Train_Tejas_Express = Train_Uday_Express = 0
    Train_Vande_Bharat_Express = Train_Yuva_Express = 0

    # Source categories
    Source_Banglore = Source_Chennai = Source_Delhi = Source_Kolkata = Source_Mumbai = 0

    # Destination categories
    Destination_Banglore = Destination_Cochin = Destination_Delhi = Destination_Hyderabad = 0
    Destination_Kolkata = Destination_New_Delhi = 0

    if request.method == 'POST':
        Train = request.form['train']
        Source = request.form['source']
        Destination = request.form['destination']

        # **Check if Source and Destination are the same**
        if Source.replace("Source_", "") == Destination.replace("Destination_", ""):
            return render_template('index.html', error="Source and destination cannot be the same.")

        # Train Selection
        if Train == 'Train_Humsafar_Express':
            Train_Humsafar_Express = 1
        elif Train == 'Train_Jan_Shatabdi_Express':
            Train_Jan_Shatabdi_Express = 1
        elif Train == 'Train_Garib_Rath':
            Train_Garib_Rath = 1
        elif Train == 'Train_Mahamana_Express':
            Train_Mahamana_Express = 1
        elif Train == 'Train_Rajdhani_Express':
            Train_Rajdhani_Express = 1
        elif Train == 'Train_Sampark_Kranti_Express':
            Train_Sampark_Kranti_Express = 1
        elif Train == 'Train_Shatabdi_Express':
            Train_Shatabdi_Express = 1
        elif Train == 'Train_Tejas_Express':
            Train_Tejas_Express = 1
        elif Train == 'Train_Uday_Express':
            Train_Uday_Express = 1
        elif Train == 'Train_Vande_Bharat_Express':
            Train_Vande_Bharat_Express = 1
        elif Train == 'Train_Yuva_Express':
            Train_Yuva_Express = 1

        # Source Selection
        if Source == 'Source_Banglore':
            Source_Banglore = 1
        elif Source == 'Source_Chennai':
            Source_Chennai = 1
        elif Source == 'Source_Delhi':
            Source_Delhi = 1
        elif Source == 'Source_Kolkata':
            Source_Kolkata = 1
        elif Source == 'Source_Mumbai':
            Source_Mumbai = 1

        # Destination Selection
        if Destination == 'Destination_Banglore':
            Destination_Banglore = 1
        elif Destination == 'Destination_Cochin':
            Destination_Cochin = 1
        elif Destination == 'Destination_Delhi':
            Destination_Delhi = 1
        elif Destination == 'Destination_Hyderabad':
            Destination_Hyderabad = 1
        elif Destination == 'Destination_Kolkata':
            Destination_Kolkata = 1
        elif Destination == 'Destination_New_Delhi':
            Destination_New_Delhi = 1

        # Prediction
        prediction = model.predict([[Train_Garib_Rath, Train_Humsafar_Express, Train_Jan_Shatabdi_Express, Train_Mahamana_Express,
                                     Train_Rajdhani_Express, Train_Sampark_Kranti_Express,
                                     Train_Shatabdi_Express, Train_Tejas_Express, Train_Uday_Express,
                                     Train_Vande_Bharat_Express, Train_Yuva_Express, Source_Banglore, Source_Chennai,
                                     Source_Delhi, Source_Kolkata, Source_Mumbai, Destination_Banglore, Destination_Cochin,
                                     Destination_Delhi, Destination_Hyderabad, Destination_Kolkata,
                                     Destination_New_Delhi]])
        output = round(prediction[0], 2)

        if output < 0:
            return render_template('index.html', pred="Sorry ...")
        else:
            return render_template('index.html', pred=f"Train Ticket Price: ₹{output}")

    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
