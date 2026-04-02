# 💰 Finance Data Processing & Access Control Backend

A backend system for managing financial records with role-based access control and dashboard analytics.

---

## 🚀 Overview

This project implements a finance dashboard backend where different users interact with financial data based on their roles.

The system supports:

* User authentication (JWT-based)
* Role-based access control
* Financial record management (CRUD)
* Aggregated dashboard insights

---

## 🧠 Design Approach

The system is designed around three core entities:

* **User** → Has roles (viewer, analyst, admin)
* **FinancialRecord** → Belongs to a user
* **Dashboard** → Aggregated insights from records

### 🔑 Key Design Decisions

* Every financial record is **owned by a user**
* Role-based permissions are enforced at the API level
* Sensitive fields like `role` are controlled server-side
* Clean separation between authentication, business logic, and data access

---

## 👥 Roles & Permissions

| Role    | Create | View Own | View All | Update | Delete | Analytics |
| ------- | ------ | -------- | -------- | ------ | ------ | --------- |
| Viewer  | ✅      | ✅        | ❌        | ❌      | ❌      | ✅ (own)   |
| Analyst | ❌      | ✅        | ✅        | ❌      | ❌      | ✅         |
| Admin   | ✅      | ✅        | ✅        | ✅      | ✅      | ✅         |

---

## 🔐 Authentication

* JWT-based authentication using access and refresh tokens
* Users must authenticate to access protected endpoints

---

## 📦 API Endpoints

### 👤 Auth

#### Register

```
POST /api/users/register/
```

#### Login

```
POST /api/users/login/
```

Response:

```json
{
  "access": "token",
  "refresh": "token"
}
```

---

### 👥 User Management

#### Update User Role (Admin Only)

```
PATCH /api/users/{id}/role/
```

---

### 💰 Financial Records

#### Create Record

```
POST /api/records/
```

#### Get Records

```
GET /api/records/
```

#### Get Single Record

```
GET /api/records/{id}/
```

#### Update Record (Admin Only)

```
PUT /api/records/{id}/
```

#### Delete Record (Admin Only)

```
DELETE /api/records/{id}/
```

---

### 📊 Dashboard

#### Summary

```
GET /api/dashboard/summary/
```

Returns:

* Total income
* Total expense
* Net balance
* Category-wise breakdown
* Recent transactions

---

## 🗄️ Data Models

### User

* username
* email
* role (viewer / analyst / admin)
* is_active

### FinancialRecord

* user (FK)
* amount
* type (income / expense)
* category
* date
* notes

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```bash
git clone <repo-url>
cd finance_backend
```

### 2. Create Virtual Environment

```bash
python -m venv myenv
source myenv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser

```bash
python manage.py createsuperuser
```

### 6. Run Server

```bash
python manage.py runserver
```

---

## 🧪 Testing

Use tools like:

* Postman
* curl

Make sure to include JWT token in headers:

```
Authorization: Bearer <access_token>
```

---

## ⚠️ Assumptions

* Email is used as unique identifier for login
* Default role for new users is `viewer`
* Only admins can modify roles and manage records globally
* SQLite is used for simplicity

---

## ✨ Optional Enhancements (Future Work)

* Pagination for records
* Advanced filtering (date range, category)
* Search functionality
* Rate limiting
* Unit & integration tests
* API documentation (Swagger)

---

## 🎯 Evaluation Focus

This project emphasizes:

* Clean backend architecture
* Role-based access control
* Proper data modeling
* Logical API design
* Maintainable and readable code

---

## 👨‍💻 Author

Abrar ul Riyaz
