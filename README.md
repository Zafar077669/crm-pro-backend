# 🚀 CRM PRO Backend — Production Ready

Enterprise-level CRM backend built with **Django** and deployed using **Gunicorn + Nginx** with full **HTTPS** and security hardening.

---

## 🌐 Live Environment

- **Base URL:**  
  https://reality-engine.duckdns.org

- **Status Endpoint:**  
GET /

Returns:
```json
{
  "status": "OK",
  "service": "CRM_PRO Backend",
  "environment": "production",
  "https": true
}
🔐 Security Overview
✅ HTTPS (Let’s Encrypt)

✅ Admin panel IP restricted

✅ Admin URL protected

✅ Production mode (DEBUG=False)

✅ Secrets stored in .env (never committed)

✅ Reverse proxy via Nginx

✅ Gunicorn systemd service (auto-restart)

🧩 Tech Stack
Layer	Technology
Language	Python 3.12
Framework	Django
API	Django REST Framework
Database	PostgreSQL
Web Server	Nginx
WSGI	Gunicorn
SSL	Let’s Encrypt
OS	Ubuntu 24.04 LTS
📁 Project Structure
crm_pro/
├── apps/
│   ├── clients/
│   ├── deals/
│   ├── leads/
│   └── users/
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── staticfiles/
├── media/
├── manage.py
├── requirements.txt
├── .env.example
└── README.md
⚙️ Environment Variables
All sensitive configuration is loaded from .env.

Example:

DEBUG=False
SECRET_KEY=change-me

ALLOWED_HOSTS=reality-engine.duckdns.org

DB_NAME=crm_pro_db
DB_USER=crm_pro_user
DB_PASSWORD=change-me
DB_HOST=localhost
DB_PORT=5432
⚠️ Never commit .env to GitHub

🛠 Local Development Setup
git clone https://github.com/USERNAME/crm-pro-backend.git
cd crm-pro-backend

python -m venv venv
source venv/bin/activate

pip install -r requirements.txt
cp .env.example .env

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
🧪 Health Check
curl https://reality-engine.duckdns.org
Expected response:

{
  "status": "OK",
  "service": "CRM_PRO Backend"
}
🔑 Admin Panel
URL:

/admin/
Access:

Restricted by IP

HTTPS only

Authentication:

Django Admin (Superuser)

🚀 Production Deployment
Gunicorn managed via systemd

Nginx reverse proxy

Automatic restart on failure

SSL auto-renew via Certbot

Service status:

systemctl status crm_pro
📦 API Usage (for Frontend)
Base API path:

/api/
JSON only

RESTful endpoints

Auth ready (JWT / Token can be added)

🧠 Best Practices Applied
Clean architecture

Environment isolation

Production-grade server setup

Security first approach

Ready for scaling

👤 Author
Zafar Sharipov
Backend Engineer / Full-Stack Developer

📜 License
Private / Internal use
All rights reserved.
