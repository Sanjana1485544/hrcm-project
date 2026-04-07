# hrcm-project


🏥 Healthcare Revenue Cycle Management (HRCM) System
📌 Overview

The Healthcare Revenue Cycle Management (HRCM) system is an end-to-end data-driven platform designed to manage and optimize the financial processes of healthcare providers.

This project integrates data engineering, real-time streaming, and machine learning to automate workflows such as patient management, billing, insurance claims, and payment tracking.

🚀 Key Features
🧾 Patient & Appointment Management
💳 Billing & Payment Processing
📄 Insurance Claim Handling
📊 Real-time Data Streaming with Kafka
⚡ Big Data Processing using PySpark
🤖 Machine Learning for Claim Prediction
📈 Dashboard Visualization (Metabase / Power BI)
🏗️ Tech Stack


Backend
Django (REST APIs & Models)
Python
Data Engineering
Apache Kafka (Real-time streaming)
PySpark (Batch + Streaming processing)
Machine Learning
PySpark MLlib
Models for:
Insurance Claim Approval Prediction
Anomaly Detection (planned/extendable)
Database
SQLite / PostgreSQL (Django ORM)
Visualization
Metabase / Power BI


📂 Project Architecture
Django (Backend APIs + Models)
        │
        ├── Kafka Producers (Django Signals)
        │
Apache Kafka (Streaming Layer)
        │
        ├── PySpark Streaming Jobs
        │         │
        │         ├── Data Processing
        │         ├── Feature Engineering
        │         └── ML Predictions
        │
        └── Django DB (Storage)
        
Dashboard (Metabase / Power BI)
🧠 Machine Learning Use Cases
📌 Insurance Claim Approval Prediction
Predict whether a claim will be approved or rejected
📌 Anomaly Detection
Detect unusual billing or patient activity
📌 Future Scope
Fraud detection
Cost optimization models
🗂️ Data Models
Patient
Appointment
MedicalHistory
InsuranceClaim
MedicalProvider
Billing
Medication
MedicalTest
Payment


🔄 Data Pipeline Flow
Data generated from Django models
Kafka Producers send events (Patient, Billing, Appointment)
Kafka streams data in real-time
PySpark consumes and processes data
Machine Learning models make predictions
Processed data stored back into database
Dashboards visualize insights
⚙️ Setup Instructions


1️⃣ Clone Repository
git clone <your-repo-link>
cd hrcm-project

2️⃣ Backend Setup
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

3️⃣ Kafka Setup
# Start Zookeeper
zookeeper-server-start.sh config/zookeeper.properties

# Start Kafka
kafka-server-start.sh config/server.properties
4️⃣ Run PySpark Jobs
spark-submit streaming_job.py
📊 Sample Data
1000+ synthetic Indian-style records per model
Generated using Django management scripts
🎯 Project Highlights
Real-world healthcare financial workflow simulation
Integration of ML + Big Data + Web Backend
Scalable architecture using Kafka + Spark
Industry-relevant use case for data engineering roles
🔮 Future Enhancements
Real-time alert system
Advanced fraud detection models
Frontend dashboard (React.js optional)
Cloud deployment (AWS/Azure)
👩‍💻 Author

Sanjana Reddy
