#!/bin/bash

# Initialize the Airflow database
airflow db init

# Start the Airflow webserver and scheduler in the background
airflow webserver & 
airflow scheduler &
wait
