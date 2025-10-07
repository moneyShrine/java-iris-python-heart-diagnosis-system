🫀 Heart Disease Diagnosis System

An intelligent health application that predicts the likelihood of heart disease based on patient medical data.
This system integrates a Spring Boot backend, a Python-based machine learning model, and an InterSystems IRIS database, all running seamlessly via Docker Compose.

🧩 Architecture Overview
heart_diagnosis/
│
├── backend/                  # Spring Boot backend
│   ├── src/...
│   ├── pom.xml
│   └── Dockerfile
│
├── python-model/             # Python Flask microservice (ML model)
│   ├── app.py
│   ├── requirements.txt
│   ├── random_forest_hrt_diag
│   └── Dockerfile
│
├── docker-compose.yml        # Docker orchestration file
└── README.md

🚀 Features

Spring Boot Backend — exposes REST APIs for managing patients and medical records.

Machine Learning Microservice (Python) — predicts heart disease risk using a trained Random Forest model.

InterSystems IRIS Database — stores patient and medical records securely.

Dockerized Setup — one-command startup for all services.

Seamless Communication between backend and ML model through REST.

⚙️ Technologies Used
Component	Technology
Backend	Java 17, Spring Boot 3, Hibernate ORM
Database	InterSystems IRIS Community Edition
Machine Learning	Python 3.11, Flask, scikit-learn, joblib
Containerization	Docker, Docker Compose
Build Tool	Maven 3.9
Communication	RESTful APIs (JSON)
🧠 ML Model

The Random Forest Classifier was trained using clinical features (e.g., blood pressure, cholesterol, heart rate, etc.).
The model is serialized with joblib and served via Flask API:

Endpoint:

POST /predict


Request Example:

{
  "features": [63, 1, 145, 233, 1, 150, 0, 2.3, 0, 0, 1]
}


Response Example:

{
  "prediction": "Positive"
}

🐳 Docker Setup
Prerequisites

Docker Desktop

Docker Compose

Build and Run All Containers
docker-compose up --build

Access the Services
Service	URL	Description
Spring Boot API	http://localhost:8080
	Backend REST API
Python ML Model	http://localhost:5000
	Flask prediction API
InterSystems IRIS	http://localhost:52773/csp/sys/UtilHome.csp
	IRIS Management Portal
🧾 Environment Variables

You can modify database credentials and other environment variables inside docker-compose.yml:

environment:
  - IRIS_USERNAME=SuperUser
  - IRIS_PASSWORD=Joe+God=2much
  - IRIS_NAMESPACE=HEALTH_NS

📦 Building Individual Services

Backend (Spring Boot)

cd backend
docker build -t heart-backend:latest .
docker run -p 8080:8080 heart-backend


Python Model

cd python-model
docker build -t python-model:latest .
docker run -p 5000:5000 python-model

🧰 API Integration Flow

Frontend or Postman sends patient data to the Spring Boot API.

The backend stores the data in IRIS Database.

The backend then calls the Python Flask model to predict heart disease.

The prediction is returned and stored in the patient’s record.

🧑‍💻 Author

Joseph Martins
Software Developer | AI Researcher | Project Management Expert
📧 Email: joeyekpe@gmail.com

🌍 GitHub