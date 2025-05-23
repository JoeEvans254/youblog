
---


# 📝 YouBlog

**Your Voice, Your Story – Share It on YouBlog!**

YouBlog is a modern, responsive Django-based blogging platform for users to create, share, and manage blog posts with ease. It features animated image previews, comment functionality, categorized content, and a sleek blue-to-teal UI design.

---

## 🚀 Features

- **Post Creation and Management**  
  Create, edit, and delete blog posts with rich text and image uploads.

- **Image Preview with Animation**  
  Uploaded images show a smooth fade-in and scale animation before submission.

- **Responsive Design**  
  Works seamlessly across desktop and mobile devices.

- **User Authentication**  
  Secure user registration, login, and logout capabilities.

- **Categories**  
  Posts can be organized into categories for easier navigation and filtering.

- **Post Comments**  
  Users can leave comments under blog posts.

- **Modern UI**  
  Aesthetic gradient (`#1E3A8A` → `#2DD4BF`) and Heroicons for an elegant user interface.

---

## 🛠️ Tech Stack

- **Backend:** Django 5.2.1, Python 3.13.3  
- **Frontend:** Tailwind CSS, Heroicons, Vanilla JS  
- **Database:** SQLite (can be switched to PostgreSQL/MySQL)  
- **Media & Image Handling:** Pillow  
- **Static Files:** Tailwind, JS (e.g., `image-preview.js`), custom animations

---

## 📋 Prerequisites

- Python 3.13.3 or higher  
- Git  
- A modern web browser (e.g., Chrome, Firefox)

---

## ⚙️ Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/JoeEvans254/youblog.git
   cd youblog


2. **Create and Activate Virtual Environment**

   ```bash
   python -m venv venv
   venv\Scripts\activate   # On Windows
   # source venv/bin/activate  # On macOS/Linux
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Make Migrations & Apply**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a Superuser (Admin Panel Access)**

   ```bash
   python manage.py createsuperuser
   ```

6. **Collect Static Files**

   ```bash
   python manage.py collectstatic
   ```

7. **Run the Development Server**

   ```bash
   python manage.py runserver
   ```

---

## 🧭 Usage Guide

### 🏠 Home Page

View all published posts:
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

### ✍️ Create Blog Post (Login Required)

URL:
[http://127.0.0.1:8000/create/](http://127.0.0.1:8000/create/)
Upload an image and see the animated preview.

### 📂 Add Categories (Admin Panel)

Visit:
[http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
Log in using your superuser credentials.
Click on **Categories** and add new categories.

### 💬 Comment on Posts

Comments section appears at the bottom of each blog post.
Only logged-in users can comment (optional moderation toggle).

### 🔐 Register/Login

* **Register:** [http://127.0.0.1:8000/accounts/register/](http://127.0.0.1:8000/accounts/register/)
* **Login:** [http://127.0.0.1:8000/accounts/login/](http://127.0.0.1:8000/accounts/login/)
* **Logout:** [http://127.0.0.1:8000/accounts/logout/](http://127.0.0.1:8000/accounts/logout/)

---



## 🙌 Acknowledgments

* [Django](https://www.djangoproject.com/)
* [Tailwind CSS](https://tailwindcss.com/)
* [Heroicons](https://heroicons.com/)
* [Pillow](https://python-pillow.org/)

---

**Happy Blogging with YouBlog! 💙**




