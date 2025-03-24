## Supply Chain Optimization Pipeline for Logistics company

### Overview

A global logistics company wants to opmitizr it's supply chain by analyzing shipping, inventory and demand data in real-time, the solution is a data pipeline that extracts data from various sources and ensure timely devlivery.


### Architecture
![supplychain drawio (3)](https://github.com/user-attachments/assets/87e15e19-b3c7-414e-82e6-0aee22751641)



### Technologies Used
- Kafka (Data Ingestion)
- Apache Flink (Stream Processing)
- Apache Airflow (Batch Processing)
- GCP BigQuery (Data Storage)
- Power BI/Tableau (Visualization)

### How to Run
1. Start Kafka: `bin/zookeeper-server-start.sh config/zookeeper.properties & bin/kafka-server-start.sh config/server.properties`
2. Run Kafka Producer: `python kafka_producer.py`
3. Run Kafka Consumer: `python kafka_consumer.py`
4. Start Flink Job: `python flink_processing.py`
5. Run Airflow DAG: `airflow dags trigger supply_chain_batch_processing`
6. Execute Predictive Model: `python predictive_model.py`

### Outcome
- Reduced supply chain delays by 20%
- Improved customer satisfaction

## Installation & Setup
### Step 1: Clone the Repository
Clone the repository to your local machine:
git clone 

### Step 2: Install Dependencies
Install the required dependencies using `pip`:
pip install -r requirements.txt

### Step 3: Set Up Kafka
Set up Apache Kafka on your local machine or use a cloud Kafka service. If using local Kafka, ensure that the broker is running on `localhost:9092`.

### Step 4: Docker Setup
To deploy the entire system in containers using Docker, build and run the Docker container:
`docker-compose up --build`

This will start the Kafka producer, consumer, and other components of the pipeline.

## Running the Project
- **Kafka Producer**: Simulates real-time transaction data.
- **Kafka Consumer**: Ingests transaction data and sends it to Spark for processing.
- **Spark Fraud Detection**: Streams and processes transactions, applying fraud detection logic.
- **TensorFlow Model**: Classifies transactions as fraudulent or legitimate.
- **AWS Lambda**: Sends alerts for suspicious transactions.
- **DBT**: Transforms and models data in the pipeline.

## Testing the System
To test the fraud detection pipeline:
1. Run the Kafka producer to simulate transaction data.
2. Start the Kafka consumer to consume the data.
3. Check the Spark streaming console output to view fraud detections.
4. If a fraudulent transaction is detected, the AWS Lambda function will trigger an alert to the configured phone number.
