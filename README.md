# AI-First Full Stack Workflow Platform

A professional full-stack project built to demonstrate front-end, back-end, database, REST API, AI-first development, deployment, and CI/CD skills.

## Project Overview

This project is an AI-assisted workflow management platform where users can create tasks, manage project status, and generate AI-style priority recommendations. It demonstrates the ability to design, develop, maintain, test, containerize, and deploy a modern web application using clean architecture.

## Key Features

- Responsive React front-end with clean user interface
- FastAPI back-end with RESTful APIs
- PostgreSQL-ready database design using SQLAlchemy
- SQLite default for easy local execution
- Task creation, update, delete, and search APIs
- AI-style priority scoring logic for project tasks
- Dashboard cards for total, pending, in-progress, and completed work
- Docker support for local deployment
- GitHub Actions CI workflow
- Clean, maintainable, production-style code structure

## Tech Stack

### Front End
- React
- JavaScript
- HTML
- CSS
- Responsive design principles

### Back End
- Python
- FastAPI
- SQLAlchemy
- RESTful APIs

### Database
- SQLite for local development
- PostgreSQL-ready configuration

### DevOps
- Git
- Docker
- Docker Compose
- GitHub Actions CI/CD

## Project Structure

```text
skild-ai-fullstack-project/
├── backend/
│   ├── app/
│   │   ├── database.py
│   │   ├── main.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   └── services.py
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── api.js
│   │   └── styles.css
│   ├── Dockerfile
│   ├── index.html
│   ├── package.json
│   └── vite.config.js
├── docs/
│   └── PROJECT_EXPLANATION.md
├── .github/workflows/ci.yml
├── docker-compose.yml
└── README.md
```

## How to Run Locally

### 1. Run Back End

```bash
cd backend
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Back-end API will run at:

```text
http://127.0.0.1:8000
```

API documentation:

```text
http://127.0.0.1:8000/docs
```

### 2. Run Front End

```bash
cd frontend
npm install
npm run dev
```

Front-end application will run at:

```text
http://localhost:5173
```

## Run with Docker

```bash
docker-compose up --build
```

## Why This Project Is Professional

This project directly demonstrates:

- Front-end development using React, HTML, CSS, and JavaScript
- Responsive and adaptive UI design
- Back-end development using Python and FastAPI
- REST API design and integration
- Database modeling using SQLAlchemy
- Clean, maintainable code
- API-driven front-end/back-end communication
- Docker-based deployment
- CI/CD pipeline using GitHub Actions
- AI-first thinking through automated task scoring and recommendation logic

## Resume / Interview Explanation

I built an AI-first full-stack workflow platform using React, FastAPI, SQLAlchemy, and Docker. The system allows users to create, manage, and track project tasks through a responsive dashboard. I implemented RESTful APIs, database models, API integration, task analytics, and AI-style priority scoring. The project follows clean code practices, supports containerized deployment, and includes a CI/CD pipeline using GitHub Actions.
