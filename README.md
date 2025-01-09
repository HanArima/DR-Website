# Automated Diabetic Retinopathy Detection Web Application
### Overview

This Flask application provides a platform for detecting Diabetic Retinopathy from uploaded retinal images. Users can upload images, input personal details, and receive a diagnosis indicating the presence and severity of Diabetic Retinopathy. All data, including patient details and images, are stored securely on AWS services.

### Features

User-Friendly Interface: Simple and intuitive interface for uploading images and inputting patient details.
Image Processing & Prediction: Utilizes a pre-trained deep learning model to analyze images and predict Diabetic Retinopathy.
Data Storage: Patient details and images are securely stored on AWS S3 and AWS RDS.
Data Retrieval: Allows for future retrieval and review of patient records.

### Technologies Used

Flask: Backend framework to handle application logic.
AWS S3: For storing uploaded images.
AWS RDS (MySQL): For storing patient details and diagnosis records.
TensorFlow/Keras: For the deep learning model used in predictions.
MySQL Workbench: For managing the RDS database.
