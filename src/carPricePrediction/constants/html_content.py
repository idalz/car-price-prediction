index_dict = {
    "title": "Home",
    "quote_h2": "Choose <span>Features</span><br> Get <span>Estimates</span>",
    "quote_p": "Effortlessly predict car prices by selecting features and receiving instant estimates using our trained neural network.",
    "quote_button": "Make a Prediction"
}

predict_dict = {
    "title": "Car Information Form",
    "form_title": "Car Information Form",
    "form_button": "Predict Price"
}

about_dict = {
    "title": "About this Project",
    ### About the project
    "project_title": "About the Project",
    "project_descr": """
    In the automotive market, determining the fair price of a car can be challenging for both buyers and sellers.
    Prices can vary significantly based on factors such as make, model, year, mileage, and additional features. 
    With such complexity, buyers often struggle to assess whether they are getting a good deal, while sellers may have difficulty setting competitive prices. 
    This lack of transparency can lead to frustration and uncertainty in the car-buying process. <br> <br>  

    Our <strong>main goal</strong> is to harness the power of PyTorch neural networks to develop a regression model capable of accurately <strong>predicting car prices</strong>. 
    By leveraging machine learning techniques and a comprehensive dataset, our objective is to create a tool that empowers both buyers and sellers with reliable price estimates. 
    """,
    ### About the model
    "model_title": "About the Model",
    "model_descr": """
    Our model utilizes a simple <strong> neural network architecture implemented using PyTorch</strong>, trained on a comprehensive dataset from Kaggle.
    With input, hidden, and output layers, the model employs fully connected linear units and activation functions to capture intricate data patterns.
    Through iterative training using techniques like gradient descent, it minimizes prediction errors. During training, features are preprocessed, scaled, and encoded for optimal performance.
    Leveraging PyTorch's efficiency, the model iteratively learns from the data. 
    With a <strong>Mean Root Squared Error (MRSE) of 8145</strong>, our model showcases a good accuracy in predicting car prices, 
    underscoring its effectiveness in capturing the nuanced relationships between car features and prices.
    """,
    ### About the data
    "data_title": "About the Data",
    "data_descr": """
    <p>The dataset used in this project was sourced from Kaggle's <a href="https://www.kaggle.com/datasets/deepcontractor/car-price-prediction-challenge" style="color: var(--primary-color-1)";>
    Car Price Prediction Challenge</a>. 
    It comprises a collection of car listings along with various features used for predicting car prices.</p>

    <p><strong>Price:</strong> The price of the car (target variable).<br>
    <strong>Manufacturer:</strong> The manufacturer of the car.<br>
    <strong>Category:</strong> The category of the car.<br>
    <strong>Leather interior:</strong> Indicates whether the car has leather interior or not.<br>
    <strong>Fuel type:</strong> The type of fuel used by the car.<br>
    <strong>Cylinders:</strong> The number of cylinders in the car's engine.<br>
    <strong>Gear box type:</strong> The type of gear box used in the car.<br>
    <strong>Drive wheels:</strong> The type of drive wheels in the car (e.g., front-wheel drive, rear-wheel drive).<br>
    <strong>Doors:</strong> The number of doors in the car.<br>
    <strong>Wheel:</strong> The type of wheel used in the car.<br>
    <strong>Color:</strong> The color of the car.<br>
    <strong>Airbags:</strong> The number of airbags in the car.<br>
    <strong>EngineVolume:</strong> The volume of the car's engine.<br>
    <strong>Mileage:</strong> The mileage of the car in kilometers.<br>
    <strong>Prod. year:</strong> Year the car was produced.</p>
    """,
}