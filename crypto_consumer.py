# crypto_consumer.py
from kafka import KafkaConsumer
import mysql.connector
import json
from datetime import datetime

consumer = KafkaConsumer(
    'crypto-data',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Timmy@2013',
    database='crypto_data'
)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS crypto_prices (
    id INT AUTO_INCREMENT PRIMARY KEY,
    coin VARCHAR(50),
    price_usd FLOAT,
    timestamp DATETIME
)
""")

for message in consumer:
    data = message.value
    now = datetime.now()
    for coin, info in data.items():
        price = info['usd']
        cursor.execute(
            "INSERT INTO crypto_prices (coin, price_usd, timestamp) VALUES (%s, %s, %s)",
            (coin, price, now)
        )
        conn.commit()
    print("Saved to DB:", data)
