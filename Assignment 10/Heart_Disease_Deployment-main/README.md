# Heart Disease Prediction Deployment

This repository contains an end-to-end machine learning project that predicts whether a patient is at risk of heart disease based on clinical parameters. It includes the model training pipeline, a Flask REST API, and the configuration files required for cloud deployment.

## Live Application URL
**Render Deployment URL:** `https://heart-disease-deployment-fmhy.onrender.com`

## Conclusion
The deployment of this heart disease prediction model successfully demonstrated the end-to-end machine learning lifecycle. Regarding model performance, the classification model achieved strong accuracy during testing, reliably identifying high-risk clinical patterns while minimizing false negatives, which is critical for healthcare applications. During deployment, the primary challenge involved configuring the production environment on Render. Specifically, I encountered a missing web server dependency error because gunicorn was initially omitted from the build process, which caused the application to fail upon startup. Resolving this required carefully aligning the local requirements with the cloud deployment build commands. This project underscores the importance of MLOps in machine learning projects. MLOps bridges the gap between static, local model training and live, accessible web services. By implementing proper version control, standardized dependency packaging, and cloud serving, MLOps ensures that predictive models deliver real-world value reliably and sustainably.

## Project Developer
I approached this deployment utilizing my background as an AI Recommendation Engine Architect to ensure the model serving architecture was robust and scalable. The entire pipeline, from data preprocessing and model serialization to the final Flask API routing and Render cloud configuration, was individually built to maintain high availability and seamless data ingestion for real-time predictive health analytics.
