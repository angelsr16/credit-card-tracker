# 💳 Credit Card Tracker

A full-stack personal finance tracker to manage credit card usage, payments, and installments.  
This is a **work-in-progress** project developed for personal use, aiming to provide insights into monthly expenses and help avoid interest charges.

---

## 🛠️ Features (Planned)

- ✅ User authentication (JWT)
- ✅ Register credit cards with limits, due dates, and cutoff dates
- ✅ Record transactions with or without installments
- ✅ Track monthly installment payments
- ✅ Apply payments and update balances automatically
- 🔜 Visual dashboard with summaries per card and month
- 🔜 Monthly reminders for due payments
- 🔜 Spend categories and analytics
- 🔜 Mobile-friendly frontend

---

## 🚀 Backend Setup

### 1. Clone the repo

```bash
git clone https://github.com/your-username/finance-tracker.git
cd finance-tracker/backend
```
### 2.- Create and activate a virtual environment 

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3.- Install dependencies

```bash
pip install -r requirements.txt
```

### 4.- Create a .env file

In the backend/ folder, create a file named .env with the following content:

```bash
SECRET_KEY=your-secret-key
ALGORITHM=HS256
DATABASE_URL=mysql+pymysql://youruser:yourpassword@localhost:3306/finance_tracker_db
```

### 5.- Set up MySQL

Install MySQL and create a new database:

```bash
CREATE DATABASE finance_tracker_db;
```
You can use [MySQL Workbench](https://dev.mysql.com/downloads/workbench/)

### 6.- Run the backend

```bash
uvicorn main:app --reload
```
The backend will be available at https://localhost:8000

### 🌐 Frontend Setup (Coming Soon)
The frontend will be built with Angular, TailwindCSS, and PrimeNG.


---

# 💳 Credit Card Tracker

Credit Card Tracker es un proyecto **full-stack en desarrollo**, creado para uso personal. Su objetivo es llevar un control claro del uso de tarjetas de crédito, pagos mensuales y evitar intereses, además de entender mejor los hábitos de gasto.

---

## 🛠️ Funcionalidades planeadas

 - ✅ Autenticación de usuarios con JWT
 - ✅ Registro de tarjetas de crédito con límites, fechas de corte y de pago
 - ✅ Registro de transacciones con o sin meses sin intereses
 - ✅ Seguimiento de pagos mensuales de cada transacción
 - ✅ Aplicación de pagos y actualización de saldos automáticamente
 - 🔜 Dashboard con resumen por tarjeta y mes
 - 🔜 Recordatorios mensuales de pagos
 - 🔜 Categorías de gastos y análisis visual
 - 🔜 Frontend responsivo y adaptable a móviles

---

## 🚀 Cómo configurar el backend

### 1. Clona el repositorio

```bash
git clone https://github.com/your-username/finance-tracker.git
cd finance-tracker/backend
```
### 2.- Crea un entorno virtual

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3.- Instala las dependencias

```bash
pip install -r requirements.txt
```

### 4.- Crea el archivo .env

En la carpeta /backend, crea un archivo .env con el siguiente contenido:

```bash
SECRET_KEY=your-secret-key
ALGORITHM=HS256
DATABASE_URL=mysql+pymysql://youruser:yourpassword@localhost:3306/finance_tracker_db
```

### 5.- Set up MySQL

Instala MySQL y crea una nueva base de datos:

```bash
CREATE DATABASE finance_tracker_db;
```
Puedes usar [MySQL Workbench](https://dev.mysql.com/downloads/workbench/)

### 6.- Inicia el backend

```bash
uvicorn main:app --reload
```
El backend se correrá en la siguiente dirección https://localhost:8000

### 🌐 Frontend Setup (Coming Soon)
El frontend será programado con Angular, TailwindCSS, y PrimeNG.


## ⚠️ Disclaimer / Aviso
This project is for personal and educational use only. It is not a production-grade financial application.

Este proyecto es solo para uso personal y educativo. No es una aplicación financiera profesional.