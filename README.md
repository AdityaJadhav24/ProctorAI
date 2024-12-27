# ProctorAI
ProctorAI is a machine learning-based exam proctoring system using TensorFlow. It monitors students during online exams, detecting suspicious activities like multiple faces, mobile phones, and browser/tab switching. The system locks the browser, logs events, and provides teachers with real-time insights and detailed logs for exam integrity.

## 🚀 Features

- **Real-Time Monitoring**: Uses machine learning models for continuous monitoring during online exams.
- **Face Detection**: Detects faces to ensure the student is present throughout the exam.
- **Suspicious Behavior Detection**: Identifies multiple people in the frame, unauthorized devices (e.g., mobile phones), or any abnormal activity.
- **Tab-Switching Detection**: Logs attempts to switch tabs or exit the exam page.
- **Teacher Dashboard**: Teachers can create and manage exam rooms, track student progress, and view detailed activity logs.
- **Secure Exam Environment**: Locks the browser to prevent cheating and ensures that the student cannot access any external resources during the exam.

## 📋 Prerequisites

Before you begin, make sure you have the following installed:

- Python 3.x
- Django 5.1.1 (or as specified in `requirements.txt`)

## ⚙️ Installation

Follow these steps to set up the project on your local machine:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/AdityaJadhav24/ProctorAI.git

2. **Navigate to the project directory:**:
    ```bash
    cd ProctorAI

3. **Set up a virtual environment (optional but recommended)**:
    ```bash
    python -m venv .venv

4. **Activate the virtual environment:**:

    For Windows:
        ```bash
        .venv\Scripts\activate

    For macOS/Linux:
        ```bash
        source .venv/bin/activate

5. **Install dependencies**:

    ```bash
    pip install -r requirements.txt

6. **Run the development server**:
    
    ```bash
    python manage.py runserver

**The application should now be running at http://127.0.0.1:8000/.**

