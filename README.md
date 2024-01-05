# Pokemon Berries Statistics Calculator

This project calculates statistics for a list of Pokemon berries by fetching data from the PokeAPI. It's built using Python 3, pytest for testing, Chalice as an AWS Lambda framework, and AWS API Gateway to expose the Lambda function through a REST endpoint.

## Endpoints
- **GET /allBerryStats**: Returns the stats for all the berries' growth times, including metrics like min, max, median. etc.
- **GET /allBerryStats/histogram**: Returns a histogram with the growth times and their frequency.

## Dependencies
- Python 3.11
- Pytest
- Chalice
- AWS lambda
- AWS api gateway

## Installing
1. **Setup Python Environment:**
   - Ensure Python 3.11 is installed on your system.
   - Create and activate a virtual environment:
     ```
     python3 -m venv venv
     source venv/bin/activate   # For Unix or MacOS
     # or
     venv\Scripts\activate      # For Windows
     ```

2. **Install Requirements:**
   - Install project dependencies using pip:
     ```
     pip install -r requirements.txt
     ```

3. **Configure AWS Credentials:**
   - Create or update your AWS credentials file located at `~/.aws/credentials` with the necessary access keys:
     ```
     [default]
     aws_access_key_id = YOUR_ACCESS_KEY_ID
     aws_secret_access_key = YOUR_SECRET_ACCESS_KEY
     ```

## Commands
- `pytest`: Run tests to ensure the project functions correctly.
- `chalice local`: Test the endpoint locally to simulate AWS Lambda functionality.
- `chalice deploy`: Deploy the application to AWS using Chalice.

**Note:** Before deploying, ensure your AWS credentials are properly set up and you have the necessary permissions to create Lambda functions and API Gateway endpoints.

## Possible Improvements
- **Create a Periodic Lambda Function:** Develop a Lambda function that runs periodically to process data and store it in a cache or a database. Like:
```python
from chalice import Chalice, Rate

app = Chalice(app_name="helloworld")

# Automatically runs every 5 minutes
@app.schedule(Rate(5, unit=Rate.MINUTES))
def periodic_task(event):
    ...
```
- **Implement Cache/Database Retrieval:** Modify the API endpoint to first attempt to retrieve information from the cache or database before fetching it from the PokeAPI. This could improve response times and reduce the number of requests made to external APIs.
- **Enhance Histogram Endpoint:** Allow the histogram endpoint (`GET /allBerryStats/histogram`) to accept parameters defining the range for the histogram. This enhancement would provide flexibility in generating histograms based on different ranges, improving the granularity of the data visualization.