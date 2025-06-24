# 🧠 PythonEDU - Backend API

This is the **backend API** for the PythonEDU online bootcamp platform.  
Built using **Django REST Framework**, the system follows a **layered architecture** and provides all endpoints required by the frontend.

Designed to scale on **AWS**, this backend is robust, well-structured, and ready for production.

---

## 🚀 Tech Stack

- 🐍 Python 3.x
- 🌐 Django & Django REST Framework
- 🧱 Layered Architecture (Views, Services, Serializers, Models)
- 🗄️ PostgreSQL for production / SQLite for development
- 🧪 Django Tests
- ☁️ AWS (planned for deployment)

---

## 📁 Project Structure (Simplified)

pythonedu_backend/
├── api/ # Application logic (views, serializers, etc.)
├── core/ # Models and utilities
├── config/ # Settings and URL configurations
├── tests/ # Unit and integration tests
└── manage.py

yaml
Copiar
Editar

---

## 📌 UML Diagrams

📎 UML class and architecture diagrams are used to visualize the structure of the project.

👉 **Place your diagram image(s) below:**

> ![UML Class Diagram](./docs/uml_class_diagram.png)  
> _Diagram: Core models and relationships._

> ![Layered Architecture](./docs/layered_architecture.png)  
> _Diagram: Architectural structure and flow._

---

## 📦 Getting Started

1. **Clone the repository**

```bash
git clone https://github.com/YOUR-USERNAME/pythonedu-backend.git
cd pythonedu-backend
Create virtual environment and install dependencies

bash
Copiar
Editar
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
Apply migrations and run the dev server

bash
Copiar
Editar
python manage.py migrate
python manage.py runserver
🔐 Environment Variables
Create a .env file with the following variables (example):

env
Copiar
Editar
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///db.sqlite3
For production, configure PostgreSQL and disable DEBUG.

🧪 Running Tests
bash
Copiar
Editar
python manage.py test
🤝 Contributing
Fork the repo

Create a new branch:

bash
Copiar
Editar
git checkout -b feature/your-feature-name
Make your changes and commit

Push and open a Pull Request to develop

📃 License
This project is licensed under the MIT License

🙋‍♂️ About the Author
Hi! I'm Samuel — a full-stack developer in training, passionate about education, technology, and real-world solutions.
PythonEDU is part of my journey to build useful tools while learning scalable development practices.


---

