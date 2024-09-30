# amadeus_flights_server

This web application that interacts with the Amadeus Travel API to fetch flight prices for a specific route.
Implemented using local caching with Redis and also manages the Amadeus API access token automatically. 

## Prerequisites

- Docker server should be running
- Create a .env file inside folder ```amadeus_flights_server```. All the token related configs will be inside this file.

## Installation Instructions

- **Local:** This enviornment consist of django web app and redis configuration.
1. Pull or unzip the project.
2. Go to 
   ```
        cd amadeus_flights_server
   ```
3. Run the command to dockerize and start the app
    ```
        docker-compose up
    ```
## APIs
1. To test the ping endpoint
    ```
    curl http://localhost:8005/flights/ping
    ```
2. To fetch flight price (with caching)
    ```
    curl http://localhost:8005/flights/price?origin=JFK&destination=LAX&date=2024-12-01
    ```
 3. To fetch live flight price (without caching)
     ```
     curl http://localhost:8005/flights/price?origin=JFK&destination=LAX&date=2024-12-01&nocache=1
     ```
