 📁 File Upload & Download System using Django

A web-based file management application built using **Python and Django** that allows users to upload, store, and download files efficiently.

🚀 Features

- Upload files using Django forms
- Store uploaded files using Django Media Storage
- View uploaded file details
- Download files easily
- Supports multiple file formats

 🛠️ Technologies Used

- Python
- Django
- HTML
- CSS
- Bootstrap
- MySQL

 ⚙️ Django Concepts Used

- Django MVT Architecture
- Models & Database Integration
- FileField for file handling
- Media files configuration (`MEDIA_URL`, `MEDIA_ROOT`)
- Handling uploaded files using `request.FILES`
- File download using `FileResponse`

🔧 Setup Instructions

```bash
git clone <repository-url>
cd project-folder
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
