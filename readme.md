# Blog

A modern blogging website built with **Django** (backend), **Tailwind CSS** (styling), and **Supabase** (image storage & user authentication).

---

## 📚 Table of Contents

- [About](#-about)
- [Features](#-features)
- [Technologies Used](#-technologies-used)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🧠 About

A simple blogging platform where users can register, log in, upload profile avatars, and manage their profile information.

- **Frontend:** Tailwind CSS
- **Backend:** Django
- **Auth & Image Storage:** Supabase

---

## ✨ Features

- ✅ User registration and login with Supabase
- ✅ Upload & store avatars in Supabase Storage
- ✅ Responsive design with Tailwind CSS
- ✅ Profile management
- ✅ Clean, intuitive interface

---

## 🔧 Technologies Used

| Tech          | Description                           |
|---------------|---------------------------------------|
| Django        | Backend framework                     |
| Tailwind CSS  | Utility-first CSS framework           |
| Supabase      | Auth & image storage (BaaS)           |
| Font Awesome  | Icon set for UI                       |
| Cropper.js    | (Optional) Client-side image cropping |

---

## 🛠 Installation

1. **Clone the repo:**
    ```bash
    git clone https://github.com/yourusername/blog.git
    cd blog
    ```

2. **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install requirements:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run migrations:**
    ```bash
    python manage.py migrate
    ```

5. **Start the development server:**
    ```bash
    python manage.py runserver
    ```
    Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

---

## ⚙️ Configuration

### Supabase

1. Create a project at [Supabase](https://supabase.com)
2. Create a Storage Bucket (e.g., `avatar`)
3. Get your Supabase Project URL and API Key
4. Add these to Django settings or a `.env` file

**Environment Variables Example:**
```env
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
EMAIL_USE_TLS=True

GOOGLE_OAUTH_CLIENT_ID=
GOOGLE_OAUTH_CLIENT_SECRET=

DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=

SUPABASE_URL=
SUPABASE_KEY=
```

---

## 🚀 Usage

- Sign up or log in using the form.
- Upload a profile picture (avatar).
- Avatar is uploaded to Supabase and shown on the UI.
- Explore other user features.

---

## 📁 Project Structure

```
blog/
├── accounts/              # User management app
│   ├── templates/
│   ├── views.py
│   ├── forms.py
│   └── models.py
├── static/                # Static files
├── templates/             # HTML templates
├── blog/                  # Main Django project
├── manage.py
└── requirements.txt
```

---

## 🤝 Contributing

Feel free to fork the repo and submit pull requests. All kinds of contributions are welcome.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

