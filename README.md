InteriorHealth

InteriorHealth is a healthcare platform that provides affordable and accessible healthcare drugs to people living in remote and underserved regions. The platform offers a user-friendly interface for patients, health workers, and administrators, enabling drug searches, orders, delivery tracking, and payment integration.


---

Table of Contents

1. Overview


2. Features


3. Technologies Used


4. Installation


5. Usage


6. API Endpoints


7. Payment Integration


8. WebSocket Integration


9. Development Workflow


10. Contributing


11. License




---

Overview

InteriorHealth addresses healthcare challenges in interior regions by connecting patients and healthcare workers with affordable medication and delivery services. It also includes role-based access for users, ensuring streamlined operations for administrators, healthcare providers, and end-users.

Key Functionalities:

Patients: Drug search, order placement, delivery tracking, payment options.

Health Workers: Manage drug inventory and assist patients.

Admins: Manage users, drugs, and oversee transactions.



---

Features

Role-Based Access Control: Patients, Health Workers, and Admins.

Secure Authentication: Login, registration, and password reset via email.

Drug Search & Ordering: Browse a drug catalog, place orders, and track deliveries.

Payment Integration: Flutterwave and M-Pesa for seamless transactions.

WebSocket Communication: Real-time updates for drug inventory and order tracking.

Scalable Architecture: Backend powered by Django Rest Framework, frontend with React.



---

Technologies Used

Backend: Python, Django, Django Rest Framework (DRF)

Frontend: React.js, Tailwind CSS

Database: SQLite (for development), PostgreSQL (for production)

Real-Time Communication: Django Channels (WebSockets)

Payment Gateways: Flutterwave, M-Pesa

Hosting: Digital Ocean

DevOps: Docker, GitHub Actions, Nginx



---

Installation

To set up the project locally:

1. Clone the Repository:

git clone https://github.com/your-username/InteriorHealth.git
cd InteriorHealth


2. Set Up Backend:

Create a virtual environment:

python3 -m venv venv
source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Run database migrations:

python manage.py migrate

Start the development server:

python manage.py runserver



3. Set Up Frontend:

Navigate to the frontend directory:

cd frontend

Install dependencies:

npm install

Start the React development server:

npm start



4. Environment Variables:

Create a .env file in the root directory:

cp .env.example .env

Update the environment variables as needed.





---

Usage

Once the project is running, you can access it at:

Backend API: http://127.0.0.1:8000/api/

Frontend: http://localhost:3000


Login as a Patient, Health Worker, or Admin to test the role-specific features.


---

API Endpoints

Users

POST /api/users/register/ – Register a new user.

POST /api/users/login/ – Login a user.


Drugs

GET /api/drugs/ – View all available drugs.

POST /api/drugs/add/ – Add a new drug (Admin only).


Orders

GET /api/orders/ – View all orders (Admin/Health Worker).

POST /api/orders/ – Place a new order.


For a full list of endpoints, refer to the API Documentation.


---

Payment Integration

Flutterwave: Integrated for card payments and bank transfers.

M-Pesa: Provides mobile money transaction capabilities.


For configuration, update the .env file with your payment gateway credentials.


---

WebSocket Integration

Real-time updates are implemented using Django Channels for:

1. Drug inventory updates.


2. Order status notifications.



Ensure you configure your WebSocket server correctly in the production environment.


---

Development Workflow

Branching Strategy

Main: Production-ready code.

Develop: Active development branch.

Feature: New features under development.


Deployment

1. Build Docker images for production:

docker-compose -f docker-compose.prod.yml up --build


2. Deploy to Digital Ocean with Nginx for reverse proxying.




---

Contributing

We welcome contributions to InteriorHealth! Follow these steps to contribute:

1. Fork the repository.


2. Create a feature branch.


3. Commit your changes.


4. Submit a pull request for review.



For detailed guidelines, see CONTRIBUTING.md.


---

License

This project is licensed under the MIT License. See the LICENSE file for details.


