import streamlit as st
import pandas as pd
import joblib

# -------------------------
# Load Model
# -------------------------
model = joblib.load("car_price_prediction.pkl")

brand_name = ["Toyota", "Hyundi", "Ford", "BMW", "Audi","Skoda","Merc","vauxhall","volkswagen"]


ford_model_num = [' Mondeo', ' Puma', ' Grand C-MAX', ' Escort', ' B-MAX', ' Ka+', ' Galaxy', ' KA', 
                  ' Tourneo Connect', ' Focus', ' Mustang', ' Transit Tourneo', ' Fusion', ' C-MAX', 
                  ' Edge', ' Tourneo Custom', ' S-MAX', ' Kuga', ' EcoSport', ' Streetka', ' Fiesta', 
                  ' Ranger', ' Grand Tourneo Connect']


volk_model_num = [' Amarok', ' Arteon', ' Beetle', ' CC', ' Caddy', ' Caddy Life', ' Caddy Maxi',
                   ' Caddy Maxi Life', ' California', ' Caravelle', ' Eos', ' Fox', ' Golf', 
                   ' Golf SV', ' Jetta', ' Passat', ' Polo', ' Scirocco', ' Sharan', ' Shuttle', 
                   ' T-Cross', ' T-Roc', ' Tiguan', ' Tiguan Allspace', ' Touareg', ' Touran', ' Up']

vauxhall_model_num = [' Adam', ' Agila', ' Ampera', ' Antara', ' Astra', ' Cascada', ' Combo Life',
                       ' Corsa', ' Crossland X', ' GTC', ' Grandland X', ' Insignia', ' Kadjar', 
                       ' Meriva', ' Mokka', ' Mokka X', ' Tigra', ' Vectra', ' Viva', ' Vivaro', 
                       ' Zafira', ' Zafira Tourer']


merc_model_num = [' A Class', ' B Class', ' C Class', ' CL Class', ' CLA Class', ' CLC Class', 
                  ' CLK', ' CLS Class', ' E Class', ' G Class', ' GL Class', ' GLA Class', 
                  ' GLB Class', ' GLC Class', ' GLE Class', ' GLS Class', ' M Class', ' R Class',
                    ' S Class', ' SL CLASS', ' SLK', ' V Class', ' X-CLASS', '180', '200', '220', '230']


bmw_model_num = [' 1 Series',' 2 Series',' 3 Series',' 4 Series',' 5 Series',' 6 Series',
                ' 7 Series',' 8 Series',' M2',' M3',' M4',' M5',' M6',' X1',' X2',
                        ' X3',' X4',' X5',' X6',' X7',' Z3',' Z4',' i3',' i8']

audi_model_num = [' A1',' A2',' A3',' A4',' A5',' A6',' A7',' A8',' Q2',' Q3',' Q5',' Q7',' Q8',
                ' R8',' RS3',' RS4',' RS5',' RS6',' RS7',' S3',' S4',' S5',' S8',' SQ5',' SQ7',' TT']

Toyota_model_num = [' Auris',' Avensis',' Aygo',' C-HR',' Camry',' Corolla',' GT86',' Hilux',' IQ',
 ' Land Cruiser',' PROACE VERSO',' Prius',' RAV4',' Supra',' Urban Cruiser',' Verso',' Verso-S',' Yaris']

skoda_model_num = [' Citigo',' Fabia',' Kamiq',' Karoq',' Kodiaq',' Octavia',' Rapid',
         ' Roomster',' Scala',' Superb',' Yeti',' Yeti Outdoor']

hundai_model_num = [' Accent',' Amica', ' Getz','I10',' I20',' I30',' I40',
 ' I800',' IX20',' IX35',' Ioniq',' Kona',' Santa Fe',' Terracan',' Tucson',' Veloster']

st.set_page_config(
    page_title="Car Price Prediction",
    page_icon="🚗",
    layout="centered"
)

st.title("🚗 Car Price Prediction")
st.write("Fill the car details to estimate its price.")

# -------------------------
# User Inputs
# -------------------------

brand = st.selectbox(
    "Brand",
    brand_name
)

if brand == "BMW":
    model_name = st.selectbox(
        "Model",
        bmw_model_num
    )

if brand == "Toyota":
    model_name = st.selectbox(
        "Model",
        Toyota_model_num
    )

if brand == "Hyundi":
    model_name = st.selectbox(
        "Model",
        hundai_model_num
    )

if brand == "Ford":
    model_name = st.selectbox(
        "Model",
        ford_model_num
    )

if brand == "Audi":
    model_name = st.selectbox(
        "Model",
        audi_model_num
    )

if brand == "Skoda":
    model_name = st.selectbox(
        "Model",
        skoda_model_num
    )

if brand == "vauxhall":
    model_name = st.selectbox(
        "Model",
        vauxhall_model_num
    )

if brand == "volkswagen":
    model_name = st.selectbox(
        "Model",
        volk_model_num
    )

year = st.number_input(
    "Year",
    2000,
    2025,
    2020
)

engine_size = st.number_input(
    "Engine Size (L)",
    0.8,
    6.0,
    1.5
)

fuel = st.selectbox(
    "Fuel Type",
    ["Petrol", "Diesel", "CNG", "Electric"]
)

transmission = st.selectbox(
    "Transmission",
    ["Manual", "Automatic","Semi-Auto"]
)

mileage = st.number_input(
    "Mileage (km)",
    0,
    500000,
    30000
)

mpg = st.number_input(
    "MPG",
    0.3,
    400.0,
    200.0,
)

tax = st.number_input(
    "Tax",
    0,
    600,
    200
)

# -------------------------
# Prediction
# -------------------------

if st.button("Predict Price"):

    input_df = pd.DataFrame({

    'mileage' :[mileage],
    'tax' : [tax],
    'transmission' : [transmission],
    'mpg' : [mpg],
    'Manufacturer' : [brand],
    'engineSize' : [engine_size],
    'year' : [year],
    'fuelType' : [fuel],
    'model' : [model_name]

    })

    prediction = model.predict(input_df)[0]

    st.success(f"Estimated Car Price : ₹ {96*prediction:,.2f}")