🌱 Agrisentinel – AI-Powered Smart Sprayer

Precision Agriculture using AI, IoT & Embedded Systems

📌 Overview

Agrisentinel is an AI-powered precision pesticide spraying system that detects plant infections in real time and applies pesticides only to affected regions. By combining computer vision, machine learning, embedded systems, and IoT, the system minimizes chemical usage, reduces environmental impact, and lowers operational costs for farmers.

The solution is designed to be affordable, scalable, and eco-friendly, suitable for small farms as well as large-scale agricultural deployments.

🎯 Problem Statement

Traditional pesticide spraying methods suffer from:

Indiscriminate chemical usage leading to environmental damage

High operational and labor costs

Health risks to farmers and consumers

Lack of real-time crop monitoring and decision support

💡 Proposed Solution

Agrisentinel addresses these challenges by:

Using AI-based image analysis to detect infection levels in crops

Performing precision spraying using servo-controlled nozzles

Running edge AI inference for offline field operation

Providing a real-time monitoring dashboard for farmers

🚀 Key Features

🎯 AI-driven selective spraying based on infection severity

📷 Real-time plant disease detection using computer vision

🌿 30–40% reduction in pesticide usage

🔋 Solar-powered, energy-efficient operation

📊 Live dashboard with infection analytics and spray logs

🔄 Scalable architecture (trolley → multi-unit → drone integration)

🧠 System Architecture

Image Capture – Camera acquires plant images in real time

AI Processing – TensorFlow Lite model classifies infection level

Decision Engine – Determines spray dosage and actuation timing

Actuation – Servo motors and solenoid valves perform precision spraying

Monitoring – IoT telemetry sent to dashboard for visualization

🧰 Technology Stack
AI & Computer Vision

Python

TensorFlow / TensorFlow Lite

OpenCV

Embedded & IoT

ESP32 Microcontroller

Sensors: Camera, FSR, Soil Moisture

Actuators: Servo Motors, Solenoid Valves

Communication: Wi-Fi, MQTT

Dashboard & Analytics

Streamlit / ThingsBoard / React Native

Real-time telemetry and alert system

Power & Mobility

Solar Panels

Li-ion Battery

DC Motors (trolley-based mobility)

⚙️ Hardware Components

ESP32 microcontroller

Camera module

Soil moisture and force sensors

Servo motors & solenoid valves

Solar panel + battery management system

📊 Feasibility & Challenges
Challenge	Mitigation
Variable lighting	Image normalization, IR filters
Spray precision	Calibrated nozzles & pulse control
Power reliability	Solar power + battery backup
Connectivity issues	Edge processing & offline storage
Sensor failures	Redundant sensing & calibration
🌍 Impact
Economic Impact

30–40% reduction in pesticide costs

Increased crop yield and quality

Environmental Impact

Reduced soil and water contamination

Protection of beneficial insects and biodiversity

Social Impact

Improved farmer safety

Affordable technology for small and marginal farmers

📈 Scalability

Small farms: Manual or trolley-based system

Medium farms: Multi-unit autonomous sprayers

Large farms: Drone- or robot-based deployment

🏆 Recognition

Developed for Smart India Hackathon (SIH) 2025

Theme: Agriculture, FoodTech & Rural Development

Category: Hardware

🔮 Future Enhancements

Drone-based spraying integration

Multi-crop disease classification models

Cloud-based predictive pest analytics

Government and agri-body data integration

👨‍💻 Author

Sundara Mahalingam M
Mechanical Engineering (Minor in CSE)
Interests: Smart Manufacturing, Digital Twin, AI-Driven Mechanical Systems

📜 License

This project is released for academic and research purposes.
Commercial usage requires prior permission.
