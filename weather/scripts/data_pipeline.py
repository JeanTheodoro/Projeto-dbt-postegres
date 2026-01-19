import requests
import os

import psycopg2
from dotenv import load_dotenv

# Load Envirioment
load_dotenv()

from http_request import HttpRequestsrequestser

# setup logging
from config_logging import LoggerHandler
logger = LoggerHandler().instace_logging()

from connection_database import PostgresSingleton

def connect_to_database():

    try:
        connection = PostgresSingleton()
        logger.info("Successfully connect to the PostgreSQL database.")
        return connection.get_connection()
    except psycopg2.Error as error:
        logger.exception(f"Error: {str(error)}")


def create_schema_and_table():
    
    conn = connect_to_database()

    if conn is None:
        logger.info("Connection don't exists")
        return None

    try:
        with conn.cursor() as cursor:
            cursor.execute("CREATE SCHEMA IF NOT EXISTS weather_data;")
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS weather_data.city_weather (
                id SERIAL PRIMARY KEY,
                city TEXT,
                temperature FLOAT,
                weather_description TEXT,
                wind_speed FLOAT,
                time TIMESTAMP,
                inserted_at TIMESTAMP DEFAULT NOW(),
                timezone TEXT
            );    
        """)
        conn.commit()
        logger.info("Schema and table created successfully.")
    except psycopg2.Error as e:
        logger.error(f"Error creating schema and table: {e}")
        return None

    finally:
        conn.close()

def insert_data(weather_data:dict):
    
    conn = connect_to_database()

    if conn is None:
        logger.info("Connection don't exists")
        return None

    if weather_data is None:
        logger.info("Data weather empty")
        return None

    try:
        with conn.cursor() as cursor:
            cursor.execute("""
                INSERT INTO weather_data.city_weather (
                            city,
                            temperature,
                            weather_description,
                            wind_speed,
                            time,
                            inserted_at,
                            timezone
                ) VALUES (%s, %s, %s, %s, to_timestamp(%s), NOW(), %s);        
            """, (
                weather_data['name'],
                weather_data['main']['temp'],
                weather_data['weather'][0]['description'],
                weather_data['wind']['speed'],
                weather_data['dt'],
                weather_data['timezone']
            ))
            conn.commit()
            logger.info(f"Weather data for {weather_data['name']} inserted successfully.")
    except psycopg2.Error as e:
        logger.error(f"Error creating schema and table: {e}")
        return None


def get_weather_data(city:str):

    api_key = os.getenv("OPENWEATHER_API_KEY")
    
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    http = HttpRequestsrequestser(params)
    
    try:
        logger.info("Succes")
        return http.fetch()
    except requests.exceptions.RequestException as error:
        logger.exception(str(error))

if __name__ == '__main__':
    
    res = get_weather_data("Araraquara")
    insert_data(res)