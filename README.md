# Car Price Prediction

An end-to-end project utilizing PyTorch, Flask, DVC, Docker, and GitHub Actions for CI/CD deployment on AWS.

---
## Contents

- [Project Overview](#project-overview)
- [Core Technologies](#core-technologies)
- [Get the Code and Set Up Locally](#get-the-code-and-set-up-locally)
- [Project Workflow](#project-workflow)
- [Web Application](#web-application)
- [Deploy and Run the Application with Docker](#deploy-and-run-the-application-with-docker)
- [AWS CI/CD Deployment with GitHub Actions](#aws-cicd-deployment-with-github-actions)
- [License](#license)
 
---
## Project Overview

This project aims to predict car prices based on their features using a neural network model. The workflow involves the following steps:

1. **Data Collection**: Data is obtained from Kaggle's [Car Price Prediction Challenge](https://www.kaggle.com/datasets/deepcontractor/car-price-prediction-challenge) using the Kaggle API. This dataset includes various car features such as mileage, engine size, and year of manufacture.
2. **Data Preprocessing**: The collected data undergoes preprocessing to clean, transform, and prepare it for model training.
3. **Model Training**: A neural network model is trained using the preprocessed data. The model learns to predict car prices based on their features.
4. **Model Evaluation**: The trained neural network model is evaluated using test data.
5. **Web Application**: A user-friendly web application is developed to allow users to input car features and receive real-time price predictions.

By combining data collection, preprocessing, model training, model evaluation, and web development techniques, this project offers a comprehensive solution for car price prediction that is easily accessible and usable by users.

To explore the detailed research and analysis conducted for the project, refer to the project's [Research Notebook](https://github.com/idalz/car-price-prediction/blob/main/research/00_idalz_research-notebook.ipynb).

---
## Core Technologies

- numpy
- pandas
- matplotlib
- seaborn
- scikit-learn
- torch
- Flask
- Flask-Cors
- gunicorn
- dvc

---
## Get the Code and Set Up Locally

### Cloning the Repository and Setting Up Environment

To run the application on your local machine, follow these steps:

1. **Clone the Repository**:

Start by cloning the project repository from GitHub. Open your terminal and run the following command:

```bash
git clone https://github.com/idalz/car-price-prediction.git
```

2. **Set Up Kaggle API Key**

To access the dataset used in this project from Kaggle, you need to create a Kaggle API key. Follow the instructions [here](https://www.kaggle.com/docs/api) to create an API key.

3. **Create a Conda Environment**

Set up a Conda environment to isolate the project dependencies. Run the following commands in your terminal:

```bash
conda create -n <environment_name> python=3.8 -y
```

```bash 
conda activate <environment_name> 
```

\* Replace `<environment_name>` with the desired name for your Conda environment. 

4. **Install Requirements**

Install the project dependencies by executing the following command:

```bash
pip install -r requirements.txt
```

### Executing the Training Pipeline

To prepare the application for use, you'll need to execute the training pipeline. You can accomplish this by running the `main.py` or using DVC (Data Version Control).

- **Using  `main.py`** 

Using main\.py directly executes the training pipeline in a sequential manner, performing data ingestion, preprocessing, model training and evaluation all within the same script.

```bash
python main.py
```

- **Using DVC**

Using DVC not only executes the training pipeline like `main.py` but also systematically documents each step of the process.

Initialize DVC in your project directory by running:

```bash
dvc init
```

Reproduce the training pipeline with the following command:

```bash
dvc repro
```

 You can visualize the dependency graph to understand the pipeline's structure:

```bash
dvc dag
```

By following these steps, you'll prepare the application for use and ensure that the model is trained and ready for predictions.

### Running the Application

There are two options to run the application:

- **Using Python**

You can run the app using Python with the following command:
   
```bash
python app.py
```

- **Using Gunicorn (WSGI)**

Alternatively, you can run the app using Gunicorn with the following command:

```bash
gunicorn -w 4 -b 0.0.0.0:8080 app:app
```

Once the application is running, you can open your web browser and navigate to `localhost:8080` to access the application and try some predictions!

---
## Project Workflow

1. Update config.yaml
2. Update params.yaml
3. Update entity
4. Update the configuration manager in src/config
5. Update the components
6. Update the pipeline
7. Update main\.py
8. Update the dvc.yaml

---
## Web Application

The web application comprises three main pages:

#### Home Page

The home page serves as the primary interface for users and provides an overview of the application's functionality along with navigation options to access other pages.

![Home Page](static/images/home_page_img.png)
*Figure 1: Home Page*

#### Form Page

The form page enables users to input various car features. Upon submission, the form triggers a POST request to the server to generate price predictions based on the provided features.

![Form Page](static/images/form_page_img.png)
*Figure 2: Form Page*

#### About Page

The about page offers detailed information about the project, including its purpose, the underlying neural network model used for prediction, and a description of the dataset utilized for training the model.

![About Page](static/images/about_page_img.png)
*Figure 3: About Page*

These pages collectively provide users with an intuitive and interactive experience, facilitating easy exploration of the application's capabilities and insights into car price predictions.


---
## Deploy and Run the Application with Docker

1. **Download the Docker Image**:

Pull the Docker image from Docker Hub with the following command:
``` bash
docker pull idalz/car-price-prediction:latest
```

2. **Run a Docker Container**:

Launch a Docker container based on the downloaded image, specifying port mappings to expose port 8080:

```bash
docker run -p 8080:8080 -e PORT=8080 idalz/car-price-prediction:latest
```

Ensure the container is running by opening your browser and navigating to `localhost:8080`. You can now use the application to make predictions!

---
## AWS CI/CD Deployment with GitHub Actions

**Specific Access**

- EC2 Access: Virtual machine access.
- ECR: Elastic Container Registry to store Docker images in AWS.

**Description: Deployment Process**

1. Build Docker image from the source code.
2. Push the Docker image to ECR.
3. Launch your EC2 instance.
4. Pull the image from ECR to EC2.
5. Run the Docker image on EC2.

**Policies**

- AmazonEC2ContainerRegistryFullAccess
- AmazonEC2FullAccess

### 1. Login to AWS Console

### 2. Create IAM User for Deployment

1. **Create a user**: Assign a username.
2. **Attach Policies**: Attach the aforementioned policies.
3. **Provide User Credentials**: Generate a CLI access key and store it securely.

### 3. Create ECR Repository

1. **Create a Repository**: Name the repository and store its URI.

### 4. Create EC2 machine (Ubuntu)

1. **Name and Tags**: Assign a name to the instance.
2. **Application and OS Images**: Choose Ubuntu.
3. **Instance Type**: Select based on requirements.
4. **Key Pair**: Create and store the key.
5. **Network Settings**: Allow HTTPS and HTTP traffic.
6. **Configure Storage**: Adjust size based on needs.
7. **Launch the Instance**

### 5. Install Docker on EC2 Instance

Click on instance ID and then on connect button to launch the machine's terminal.
Then, excecute the commands one by one:

- **Optional Updates**

```bash
sudo apt-get update -y
```

```bash
sudo apt-get upgrade
```

- **Required Installation**

Install Docker on the machine:
```bash
curl -fsSL https://get.docker.com -o get-docker.sh
```

```bash
sudo sh get-docker.sh
```

```bash
sudo usermod -aG docker ubuntu
```

```bash
newgrp docker
```

Verify Docker installation:
```bash
docker --version
```

### 6. Configure EC2 as Self-hosted Runner

Navigate to your GitHub repository settings -> Actions -> Runner -> New self-hosted runner. 
Choose Linux as a Runner image and execute the provided commands. Verify runner connection. It should be on Idle mode.

### 7. Setup GitHub Secrets

Navigate to your GitHub repository settings -> Secrets and variables -> Actions.
Add you repository secrets:

- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY
- AWS_REGION
- AWS_ECR_LOGIN_URI
- ECR_REPOSITORY_NAME

Now, whenever you push changes to your GitHub repository, GitHub Actions will trigger a workflow that handles those changes and deploys them to your AWS EC2 instance.

### 8. Edit Inbound Rule

In the EC2 instance security tab, click on edit inbound rules and add a rule to allow Custom TCP with the app host (0.0.0.0) on port (8080).

Now, the app is deployed and ready for use!

---
## License

This project is licensed under the [MIT License](LICENSE).
