# 🎓 AI-Based Learning Style Detection & Adaptive Tutor Matching

## 📌 Project Overview

This project is a **Django-based intelligent peer tutoring platform** that matches learners with tutors based on:

* Subject requirements
* Learning style preferences
* Teaching style compatibility

The system improves learning outcomes by ensuring that students are paired with tutors who teach in a way that suits them best.

---

## 🚀 Key Features

### 👤 User Roles

* Learner
* Tutor

### 🧠 Learning Style Detection

* Questionnaire-based classification:

  * Visual
  * Practical
  * Conceptual
  * Discussion-based

### 🎯 Smart Tutor Matching

* Matches learners with tutors based on:

  * Subject
  * Teaching style
  * Availability
  * Mode (Online/Offline)

### 📅 Session Booking System

* Learners can request sessions
* Tutors can:

  * Accept ✅
  * Reject ❌

### 📊 Feedback System

* Learners can rate tutors after sessions
* Feedback includes:

  * Rating (1–5)
  * Comments

### 📞 Contact Sharing

* After acceptance:

  * Tutor contact (Email & Phone) is shown to learner

---

## 🛠️ Tech Stack

* **Backend:** Django
* **Frontend:** HTML, CSS, Bootstrap
* **Database:** SQLite
* **Language:** Python

---

## 📁 Project Structure

```
adaptive_tutor_platform/
│
├── users/              # Authentication & roles
├── profiles/           # Learner & Tutor profiles
├── matching/           # Matching logic
├── bookings/           # Session booking & feedback
├── templates/          # HTML templates
├── static/             # CSS & JS
├── db.sqlite3          # Database
├── manage.py
└── requirements.txt
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone <your-repo-link>
cd adaptive_tutor_platform
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Create superuser (admin)

```bash
python manage.py createsuperuser
```

### 6️⃣ Run the server

```bash
python manage.py runserver
```

Open in browser:

```
http://127.0.0.1:8000/
```

---

## 🧪 How to Use

### 👩‍🎓 Learner

1. Register as learner
2. Fill profile + questionnaire
3. View matched tutors
4. Request session
5. View status (Pending / Accepted / Rejected)
6. Contact tutor after acceptance
7. Give feedback

### 👨‍🏫 Tutor

1. Register as tutor
2. Fill teaching profile
3. View session requests
4. Accept / Reject requests

---

## 🧠 System Workflow

1. User registers (Learner/Tutor)
2. Learner fills learning style questionnaire
3. System classifies learning style
4. Matching algorithm finds suitable tutors
5. Learner sends session request
6. Tutor accepts/rejects
7. Contact details shared
8. Feedback collected

---

## 🔥 Unique Features

* Learning-style-based tutor matching
* Adaptive recommendation logic
* Full request-response workflow
* Feedback-driven improvement system

---

## 📈 Future Enhancements

* Real-time chat system
* Email notifications
* AI-based recommendation model
* Performance analytics dashboard
* Tutor rating system integration

---

## 🎯 Academic Relevance

This project demonstrates concepts from:

* Artificial Intelligence in Education
* Personalized Learning Systems
* Web Development using Django
* Database Design
* User Interaction Systems

---

## 👩‍💻 Author

* **Ayana K A**

---

## 📜 License

This project is for academic and educational purposes.
