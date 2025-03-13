import streamlit as st
import base64
import pickle
import numpy as np
import pandas as pd

st.set_page_config(page_title="Crop Details", layout="wide")

# Function to set background image
def set_bg(image_file):
    with open(image_file, "rb") as img:
        encoded_string = base64.b64encode(img.read()).decode()
    bg_image = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpeg;base64,{encoded_string}");
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
    }}

    /* Title Styling */
    .title-container {{
        text-align: center;
        font-size: 45px !important;
        font-weight: bold;
        color: #FFD700 !important; /* Gold */
        text-shadow: 3px 3px 6px black !important;
        margin-bottom: 20px; /* Add margin below the title */
    }}

    /* Input field styling */
    label {{
        font-size: 20px !important;
        font-weight: bold;
        color: white !important;
        text-shadow: 2px 2px 4px black;
        margin-bottom: 5px; /* Add margin below labels */
    }}

    /* Customizing Streamlit input fields */
    .stTextInput, .stNumberInput, .stSelectbox {{
        background: rgba(255, 255, 255, 0.2) !important;
        color: white !important;
        border: 1px solid rgba(255, 255, 255, 0.5) !important;
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 10px; /* Add margin below input fields */
    }}

    /* Submit Button */
    .stButton>button {{
        background: rgba(255, 255, 255, 0.2);
        backdrop-filter: blur(8px);
        color: white;
        font-size: 22px;
        padding: 12px 30px;
        border: 1px solid rgba(251, 255, 21, 0.3);
        border-radius: 12px;
        cursor: pointer;
        box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.3);
        transition: 0.3s;
         /* width: 100%;  Make the button wider */
          /* margin-top: 20px; Add margin above the button */
        width: auto; /* Adjust width as needed */
        margin: 20px auto; /* Center horizontally */
        display: block; /* Required for centering */
        transition: transform 0.2s ease, box-shadow 0.2s ease; /* Smooth transitions */
    }}
    .stButton>button:hover {{
        background-color: rgba(255, 255, 255, 0.3); /* Slightly darker on hover */
        transform: scale(1.05); /* Slightly smaller scale on hover */
        color:white; /* Text color on hover */
    }}
   
    /* Sidebar - Glassmorphism */
    section[data-testid="stSidebar"] {{
        background: rgba(255, 255, 255, 0.3); /* Semi-transparent white */
        backdrop-filter: blur(10px); /* Blur effect */
        border-radius: 15px;
        padding: 20px;
        color: white !important; 
    }}
    
    /* Output Styling */
    .output-container {{
        text-align: center;
        margin-top: 30px; /* Add margin above the output */
    }}
    .output-text {{
        font-size: 24px;
        font-weight: bold;
        color: white; /* Light Green */
        text-shadow: 2px 2px 4px black;
    }}
        /* Hide Streamlit menu */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}
    </style>
    """
    st.markdown(bg_image, unsafe_allow_html=True)

# ... (rest of the code for loading models and scalers)
# Set background image
set_bg("crop4.jpg")  # Ensure this image exists in your project folder

# Page title
st.markdown("<div class='title-container'>Enter Crop Details</div>", unsafe_allow_html=True)

# Layout for inputs
col1, col2 = st.columns(2)


with col1:
    rainfall = st.number_input("Rainfall (mm)",format="%.6f", min_value=0.00000, placeholder="Enter a value")
    temperature = st.number_input("Temperature (°C)",format="%.6f",placeholder="Enter a value")
    days_to_harvest = st.number_input("Days to Harvest", min_value=1, step=1,placeholder="Enter a value")
    fertilizer_used = st.selectbox("Fertilizer Used", ["Yes","No"],placeholder="Please choose an option")
    irrigation_used = st.selectbox("Irrigation Used", ["Yes","No"],placeholder="Please choose an option")


with col2:
    region = st.selectbox("Region", ["North", "South", "East", "West"],placeholder="Please choose an option")
    crop = st.selectbox("Crop", ["Cotton", "Rice", "Barley", "Soybean", "Wheat", "Maize"],placeholder="Please choose an option")
    weather = st.selectbox("Weather Condition", ["Cloudy", "Rainy", "Sunny"],placeholder="Please choose an option")
    soil_type = st.selectbox("Soil Type", ["Sandy", "Clay", "Loam", "Silt", "Peaty", "Chalky"],placeholder="Please choose an option")


model_rf = pickle.load(open('model_rf.sav','rb'))     # Load the trained model from the saved file
model_lr = pickle.load(open('model_lr.sav','rb'))
model_svm = pickle.load(open('model_svm.sav','rb'))

scaler = pickle.load(open('scaler.sav','rb'))
encod_crop = pickle.load(open('encodcrop.sav','rb'))
encod_reg = pickle.load(open('encodreg.sav','rb'))
encod_soil = pickle.load(open('encodsoil.sav','rb'))
encod_weath = pickle.load(open('encodweath.sav','rb'))

encod_fert = pickle.load(open('encodfert.sav','rb'))
encod_irr = pickle.load(open('encodirr.sav','rb'))


df = pd.read_csv('crop_yield.csv')

def suggest_features(df, crop, region):
    """Suggests feature values for potentially higher yield."""
    
    filtered_df = df[(df['Crop'] == crop) & (df['Region'] == region)]

    if filtered_df.empty:
        return "No data available for this crop and region."
    
    max_yield_row = filtered_df.loc[filtered_df['Yield_tons_per_hectare'].idxmax()]

    suggestions = {
        "Baseline (Existing Max)": {
            "Rainfall(mm)": max_yield_row['Rainfall_mm'],
            "Soil Type": max_yield_row['Soil_Type'],
            "Temperature(Celsius)": max_yield_row['Temperature_Celsius'],
            "Weather Condition" : max_yield_row['Weather_Condition']
        }
    }
    return suggestions


if st.button("Submit"):
    # ... (data preprocessing code)
    st.success("Details Submitted Successfully!")
    
    #To note: FEATURES NAMES SHOULD MATCH THOSE THAT WERE PASSED DURING THE FIT.
    dataset = pd.DataFrame({'Region':[region], 'Soil_Type':[soil_type], 'Crop':[crop], 'Rainfall_mm':[rainfall],
     'Temperature_Celsius':[temperature],
       'Fertilizer_Used':[fertilizer_used], 'Irrigation_Used':[irrigation_used], 'Weather_Condition':[weather],
       'Days_to_Harvest':[days_to_harvest]})

    #To note: ENCOD AND CONCAT FEATURE IN THE SAME ORDER AS DONE WITH THE TRAINING DATA
    #Correct Boolean Conversion for Label Encoding(dataset['Fertilizer_Used'] is a pandas Series, and == cannot be applied )
    dataset['Fertilizer_Used'] = dataset['Fertilizer_Used'].apply(lambda x: 1 if x == "Yes" else 0)
    dataset['Irrigation_Used'] = dataset['Irrigation_Used'].apply(lambda x: 1 if x == "Yes" else 0)


    #Label Encoding   
    dataset['Fertilizer_Used'] = encod_fert.transform(dataset['Fertilizer_Used'])
    dataset['Irrigation_Used'] = encod_irr.transform(dataset['Irrigation_Used'])
    

    # OneHot Encoding 
    reg_out = encod_reg.transform(dataset[['Region']])
    soil_out = encod_soil.transform(dataset[['Soil_Type']])
    crop_out = encod_crop.transform(dataset[['Crop']])
    weath_out = encod_weath.transform(dataset[['Weather_Condition']])

    #Concat feature names with the dataset
    #To note: ENCOD AND CONCAT FEATURE IN THE SAME ORDER AS DONE WITH THE TRAINING DATA
    in_reg = pd.DataFrame(reg_out,columns=encod_reg.get_feature_names_out())
    dataset = pd.concat([dataset,in_reg],axis=1)
    dataset.drop('Region',axis=1,inplace=True)

    in_soil = pd.DataFrame(soil_out,columns=encod_soil.get_feature_names_out())
    dataset = pd.concat([dataset,in_soil],axis=1)
    dataset.drop('Soil_Type',axis=1,inplace=True)

    in_crop = pd.DataFrame(crop_out,columns=encod_crop.get_feature_names_out())
    dataset = pd.concat([dataset,in_crop],axis=1)
    dataset.drop('Crop',axis=1,inplace=True)

    in_weath = pd.DataFrame(weath_out,columns=encod_weath.get_feature_names_out())
    dataset = pd.concat([dataset,in_weath],axis=1)
    dataset.drop('Weather_Condition',axis=1,inplace=True)

    # Apply Scaling 
    scaled_data = scaler.transform(dataset)


    # Make Prediction
    output_lr = model_lr.predict(scaled_data)
    predicted_yield = output_lr[0]  # Get the actual predicted value

    st.markdown("<div class='output-container'>", unsafe_allow_html=True)
    st.markdown(f"<div class='output-text'>Predicted Crop Yield is: {predicted_yield:.5f} tons/hectare</div>", unsafe_allow_html=True)  # Format to 2 decimal places
    st.markdown("</div>", unsafe_allow_html=True)

    suggestions = suggest_features(df, crop, region)

    st.sidebar.subheader(f"Feature Suggestions for Potentially Higher Yield for {crop} (in {region} region)")
    for suggestion_type, feature_values in suggestions.items():
        st.sidebar.write(f"**{suggestion_type}**")
        for feature, value in feature_values.items():
            if isinstance(value, float):  # Check if the value is a float
               st.sidebar.write(f"- {feature}: {value:.4f}")  # Format to 2 decimal places
            else:  # If it's not a float (e.g., string, int), display it as is
               st.sidebar.write(f"- {feature}: {value}")
        st.sidebar.write("---")  # Separator