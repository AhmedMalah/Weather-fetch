# Weather App on AWS ECS

This project fetches weather data from OpenWeather API and prints it in CloudWatch Logs.

## Steps
1. Add your OpenWeather API key as an environment variable in ECS Task Definition.
2. GitHub Actions builds and pushes the Docker image to AWS ECR.
3. Deploy the image manually to ECS.

## Environment Variables
- `OPENWEATHER_API_KEY`: Your API key from https://openweathermap.org/api
- `CITY`: City name (default: Cairo)
