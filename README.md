# ComplianceLLM

ComplianceLLM is a project that provides a compliance checking service using Docker and Docker Compose. This service allows you to input a webpage and verify its content against a compliance policy.

## Prerequisites

- [Docker](https://www.docker.com/products/docker-desktop)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Getting Started

To set up and run the ComplianceLLM server, follow these steps:

### 1. Clone the Repository

```console
git clone https://github.com/nishant-singh13/complianceLLM.git
cd complianceLLM 
```
## 2. ADD .env file on you local machine 
```console
OPENAI_API_KEY=your open API key
COMPLIANCE_URL= compliance policy url ... exp : https://stripe.com/docs/treasury/marketing-treasury
```

## 3. Build and Run with Docker Compose
Ensure Docker and Docker Compose are installed and running on your system. Then, use Docker Compose to build and start the services:


```console
docker-compose up --build
```

## 4. Access the Application
Once the containers are up, you can access the application at http://localhost:8000 (or whichever port is specified in your docker-compose.yml file).
Here is swagger link : http://0.0.0.0:8000/docs

## 5. API Usage
You can interact with the compliance checking API as follows:
```console

Endpoint: /compliance/check
Method: POST
BODY: 
{
  "url": "https://mercury.com/"
}

Response:
json
Copy code
{
  {
    "findings": {
        "HEADING": " RESULT ",
    }
}
}
```

## 6 . Stopping the Server
To stop the running Docker containers, use:


```console
docker-compose down
```

