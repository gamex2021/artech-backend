# AI Projects Portfolio

This project is a portfolio web application showcasing AI projects. It uses FastAPI for the backend and React for the frontend.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Backend Setup](#backend-setup)
3. [Frontend Setup](#frontend-setup)
4. [Running the Application](#running-the-application)
5. [Deployment](#deployment)

## Prerequisites

- Python 3.7+
- Node.js 12+
- npm


## Backend Setup

1. Navigate to the backend directory:
<pre> ```cd backend ``` </pre>

2. Create a virtual environment:
<pre> ```python -m venv venv ``` </pre>

3. Activate the virtual environment:

- On Windows:
  ```
  venv\Scripts\activate
  ```
- On macOS and Linux:
  ```
  source venv/bin/activate
  ```

4. Install the required packages:
<pre> ```pip install fastapi uvicorn``` </pre>

5. Create a `requirements.txt` file:
<pre> ```pip freeze > requirements.txt``` </pre>

## Frontend Setup

1. Navigate to the frontend directory:
<pre> ```cd frontend``` </pre>

2. Install the required packages:
<pre> ```npm install``` </pre>

3. Create a `.env` file in the frontend directory and add the backend URL:
<pre> ```REACT_APP_API_URL=[http://localhost:8000](http://localhost:8000)``` </pre>

## Running the Application

### Backend

1. From the backend directory, run:
<pre> ```uvicorn main:app --reload``` </pre>

The backend server will be running on `http://localhost:8000`.

### Frontend

1. From the frontend directory, run:
<pre> ```npm start``` </pre>

The frontend application will be running on `http://localhost:3000`.


