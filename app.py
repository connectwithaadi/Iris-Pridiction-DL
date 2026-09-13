import streamlit as st
import numpy as np
import tensorflow as tf
import joblib

# Load model and scaler
model = tf.keras.models.load_model("iris_model.h5")
scaler = joblib.load("scaler.pkl")


# Page configuration
st.set_page_config(
    page_title="Iris Flower Prediction",
    page_icon="🌸"
)

st.title("🌸 Iris Flower Prediction")

st.write("Enter the flower measurements below:")


# Input fields
sepal_length = st.number_input(
    "Sepal Length (cm)",
    min_value=0.0,
    max_value=10.0,
    value=5.1
)

sepal_width = st.number_input(
    "Sepal Width (cm)",
    min_value=0.0,
    max_value=10.0,
    value=3.5
)

petal_length = st.number_input(
    "Petal Length (cm)",
    min_value=0.0,
    max_value=10.0,
    value=1.4
)

petal_width = st.number_input(
    "Petal Width (cm)",
    min_value=0.0,
    max_value=10.0,
    value=0.2
)


# Prediction button
if st.button("Predict"):

    # Create input array
    input_data = np.array([
        [sepal_length,
         sepal_width,
         petal_length,
         petal_width]
    ])

    # Scale input
    input_scaled = scaler.transform(input_data)

    # Prediction
    prediction = model.predict(input_scaled)

    # Get class
    predicted_class = np.argmax(prediction, axis=1)[0]

    # Class names
    classes = [
        "Iris-setosa",
        "Iris-versicolor",
        "Iris-virginica"
    ]

    result = classes[predicted_class]

    st.success(f"🌸 Prediction: **{result}**")

    # Probability
    st.write("Prediction probabilities:")

    for i, probability in enumerate(prediction[0]):
        st.write(
            f"{classes[i]}: {probability * 100:.2f}%"
        )
