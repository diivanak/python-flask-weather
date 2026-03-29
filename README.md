Python Flask Weather App 🌤️

A simple web application built with Python and Flask that allows users to input a city and retrieve real-time weather data using the OpenWeatherMap API.

📦 How It Works

User inputs a city name into the web form.
The app calls the OpenWeatherMap Geocoding API to get latitude and longitude.
Using those coordinates, the app calls the Weather API to fetch current weather data.
The data is processed and rendered dynamically on the webpage.

🛠️ DevOps & CI/CD Workflow

This project has been extended beyond the tutorial to explore production-style development and DevOps workflows:

Containerization with Docker: The app is fully containerized for consistent builds and deployments.
Jenkins CI/CD pipeline: Declarative pipeline with four stages:
Checkout the code
Build the Docker image
Run automated tests with pytest
Deploy to Render (optional, controlled by branch and webhook triggers)
Automated builds with GitHub webhooks:
Pushing to the docker-jenkins branch triggers Jenkins to automatically build, test, and deploy the application.
Render deployment: The web app is hosted online via Render, automatically updated after successful pipeline execution.

📚 Project Background

The core Flask application was originally built following a tutorial to establish a baseline understanding of web development and API integration.

It has since been transformed into a full DevOps learning project, demonstrating how a simple Python web app can be extended into a robust, automated workflow for real-world deployment.

🚀 Next Steps / Learning Focus

Experiment with multi-branch Jenkins pipelines
Explore more advanced testing strategies (integration tests, API mocks)
Scale containerized deployments for multiple environments