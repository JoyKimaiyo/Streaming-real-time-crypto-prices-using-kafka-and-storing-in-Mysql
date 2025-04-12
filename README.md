# Streaming-real-time-crypto-prices-using-kafka-and-storing-in-Mysql
This project build a live crypto data pipeline using Kafka, CoinCap, and CoinGecko APIs
# 🔄 Real-Time Crypto Price Streaming with Apache Kafka & MySQL

Track and store live Bitcoin and Ethereum prices in real-time using Apache Kafka, CoinCap/CoinGecko APIs, and MySQL.

> 📖 This project is based on the tutorial:  
> [📚 Streaming Crypto Data to MySQL Using Apache Kafka](https://medium.com/@joy.kimaiyo)

---

## 🚀 Overview

This project sets up a **real-time data pipeline** that:

1. Fetches live prices from **CoinCap** or **CoinGecko**
2. Streams data to a Kafka **producer**
3. Stores streamed messages using a **Kafka consumer** into a **MySQL** database

---

## 🔧 Tech Stack

- **Apache Kafka** (real-time data streaming)
- **ZooKeeper** (Kafka coordination)
- **Python** (producers & consumers)
- **MySQL** (data storage)
- **CoinCap / CoinGecko APIs** (crypto data sources)


### 1. Clone the repo

```bash
git clone [Streaming-real-time-crypto-prices-using-kafka-and-storing-in-Mysql](https://github.com/JoyKimaiyo/Streaming-real-time-crypto-prices-using-kafka-and-storing-in-Mysql)

cd crypto-streaming



