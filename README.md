🚀 CRM PRO Backend (Production Ready)

Professional, secure va production-level CRM Backend — Django, PostgreSQL, Gunicorn va Nginx asosida qurilgan.
Real serverda ishlaydi, HTTPS, admin security va real deployment bilan.

🌐 Live URL:
👉 https://reality-engine.duckdns.org

🧠 Project Overview

CRM PRO Backend — bu bizneslar uchun mo‘ljallangan kuchli CRM tizimi bo‘lib, quyidagilarni ta’minlaydi:

Mijozlarni (Clients) boshqarish

Lead’lar bilan ishlash

Deal / Sales pipeline

Xavfsiz admin panel

REST API orqali frontend bilan integratsiya

Loyiha real production serverda ishga tushirilgan va doimiy ishlashga tayyor.

🛠 Tech Stack
Layer	Technology
Backend	Django (Python)
Database	PostgreSQL
App Server	Gunicorn
Web Server	Nginx
Security	HTTPS (Let’s Encrypt)
OS	Ubuntu 24.04
Deployment	Systemd service
Version Control	Git + GitHub
📁 Project Structure
crm_pro/
├── apps/
│   ├── users/        # Custom User model
│   ├── clients/      # Clients management
│   ├── leads/        # Leads system
│   └── deals/        # Deals / Sales
│
├── config/
│   ├── settings.py   # Production settings
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── staticfiles/      # Collected static files
├── media/            # Media uploads
├── manage.py
├── requirements.txt
└── README.md

🔐 Security Features

✔ HTTPS (SSL)
✔ Admin panel IP-based restriction
✔ Admin URL protected
✔ Production settings (DEBUG = False)
✔ Secure headers via Nginx
✔ Gunicorn behind reverse proxy

/admin/ endpoint restricted va bruteforce’dan himoyalangan.

🔑 Admin Panel
https://reality-engine.duckdns.org/admin/


Custom User model

Clients / Leads / Deals CRUD

Secure production admin

🔌 API Base
Base URL: https://reality-engine.duckdns.org/api/


API frontend yoki mobile app bilan ulanish uchun tayyor.

⚙️ Local Development (Optional)
git clone https://github.com/Zafar077669/crm-pro-backend.git
cd crm-pro-backend

python -m venv venv
source venv/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

🚀 Production Deployment (Summary)

Gunicorn — systemd service

Nginx — reverse proxy

PostgreSQL — production DB

Certbot — SSL auto-renew

Server 24/7 doimiy ishlashga sozlangan.

🧪 Health Check
{
  "status": "OK",
  "service": "CRM_PRO Backend",
  "environment": "production",
  "https": true,
  "admin": "restricted"
}

📌 Use Cases

✔ Business CRM
✔ Startup backend
✔ Admin dashboard backend
✔ REST API for frontend
✔ Portfolio / Commercial project

👨‍💻 Author

Zafar Sharipov
Backend Developer (Django / Python)

GitHub:
👉 https://github.com/Zafar077669
