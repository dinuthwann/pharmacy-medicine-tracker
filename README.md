# 💊 Medicine Reminder & Pharmacy Matcher API

A clean, modular RESTful API built with **Python**, **FastAPI**, and **SQLite**. This system allows users to search for medicines across multiple registered pharmacies, check live stock availability, and view pricing using relational database logic.

---

## 🚀 Key Features

* **Relational Database Model**: Leverages SQLite with foreign keys connecting `pharmacies` and `medicines`.
* **Optimized SQL Queries**: Uses explicit `JOIN` operations for cross-pharmacy medicine search.
* **REST API Architecture**: Implements HTTP endpoints using FastAPI with full request/response typing.
* **Interactive API Docs**: Built-in Swagger UI and ReDoc for live API testing and specification.
* **Clean Code & OOP Structure**: Adheres to Object-Oriented Programming and Clean Architecture principles.

---

## 🛠️ Tech Stack

* **Language**: Python 3.12+
* **Framework**: FastAPI
* **Database**: SQLite3
* **Server**: Uvicorn
* **Version Control**: Git (Git Flow Branching Strategy)

---

## 📂 Project Structure

```text
pharmacy-medicine-tracker/
├── app.py              # CLI testing application
├── database.py         # Database initialization & seed data logic
├── main.py             # FastAPI REST endpoints
├── pharmacy.db         # Local SQLite database
├── .gitignore          # Git exclusion config
└── README.md           # Project documentation
