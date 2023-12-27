from flask import Flask, render_template, request
import pandas as pd
import pickle
#Create App
app = Flask(__name__)

# Load the trained model and column transformer
def prediction_input_data(input_df):
    vc=pickle.load(open("model.pkl","rb"))

    ans=vc.predict(input_df)[0]

    if ans == 1:
        return "You may have heart disease. Please consult a healthcare professional. 😟"
    else:
        return "You may not have heart disease. Stay healthy! 🤓"

@app.route("/")
def display_form():
    return render_template("home.html")

@app.route("/predict",methods=["POST"])
def get_input_data():
    input_data = [
        float(request.form["Age"]),
        int(request.form["Gender"]),
        int(request.form["CP_Level"]),
        int(request.form["Trest_BPS_Level"]),
        int(request.form["Cholestrol_Level"]),
        int(request.form["FBS_Level"]),
        int(request.form["Resting_ECG_Levels"]),
        int(request.form["Thalach_Levels"]),
        int(request.form["Exang_Levels"]),
        float(request.form["Old_Peak_History_Recorded"]),
        int(request.form["Slope_Levels"]),
        int(request.form["CA_Levels"]),
        int(request.form["Thal_Levels"])
    ]

    inpu_df=pd.DataFrame(data=[input_data],
                         columns=['Age', 'Gender', 'CP Level', 'Trest BPS Level', 'Cholestrol Level', 'FBS Level','Resting ECG Levels', 'Thalach Levels', 'Exang Levels', 'Old Peak History Recorded','Slope Levels', 'CA Levels', 'Thal Levels'])

    ans=prediction_input_data(inpu_df)
    return render_template("display.html",data=ans)


# def predict_heart_disease(input_data, model):
#     input_df = pd.DataFrame(data=[[input_data]], columns=[
#         'Age', 'Gender', 'CP Level', 'Trest BPS Level', 'Cholestrol Level', 'FBS Level',
#         'Resting ECG Levels', 'Thalach Levels', 'Exang Levels', 'Old Peak History Recorded',
#         'Slope Levels', 'CA Levels', 'Thal Levels'
#     ])
#     # transformed_input = column_transformer.transform(input_df)
#     prediction = model.predict(input_df)[0]

#     if prediction == 1:
#         return "You may have heart disease. Please consult a healthcare professional."
#     else:
#         return "You may not have heart disease. Stay healthy!"

# @app.route("/")
# def display_form():
#     return render_template("home.html")

# @app.route("/predict", methods=["POST"])
# def get_input_data():
#     input_data = [
#         float(request.form["Age"]),
#         int(request.form["Gender"]),
#         int(request.form["CP_Level"]),
#         int(request.form["Trest_BPS_Level"]),
#         int(request.form["Cholestrol_Level"]),
#         int(request.form["FBS_Level"]),
#         int(request.form["Resting_ECG_Levels"]),
#         int(request.form["Thalach_Levels"]),
#         int(request.form["Exang_Levels"]),
#         float(request.form["Old_Peak_History_Recorded"]),
#         int(request.form["Slope_Levels"]),
#         int(request.form["CA_Levels"]),
#         int(request.form["Thal_Levels"])
#     ]

#     model= load_model()
#     result = predict_heart_disease(input_data, model)
#     print(result)
#     return render_template("display.html", data=result)

if __name__ == "__main__":
    app.run(debug=True)
