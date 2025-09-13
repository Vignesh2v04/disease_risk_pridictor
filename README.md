# Disease Risk Prediction Web Application
### *A project by Byte_busters25*

This is a full-stack web application built with Python and Flask that uses machine learning to predict the risk of Diabetes and Cardiovascular Disease based on user-provided health metrics.

---

### ✨ Key Features
- **Secure User Authentication:** Full registration and login functionality for a personalized experience.
- **Dual Prediction Models:** Offers separate, easy-to-use forms for predicting both Diabetes and Cardiovascular Disease (CVD).
- **Real-Time Analysis:** Delivers instant risk predictions using pre-trained machine learning models.
- **Intuitive User Interface:** A clean, responsive dashboard and results pages built with HTML and CSS.

---

### 🛠️ Tech Stack
- **Backend:** Python, Flask
- **Machine Learning:** Scikit-learn, Pandas, XGBoost, Joblib
- **Frontend:** HTML, CSS
- **Database:** SQLite for user management
- **Environment:** Python `venv` for dependency management

---

### 🏆 My Contributions & Project Leadership

As a core developer, I had a significant role in both front-end and back-end development. I also took the lead in modernizing the application's environment to ensure it remains functional and robust.

*   **Backend Development (Python & Flask):**
    *   I engineered the server-side logic using Flask to manage all user requests and API routes.
    *   I developed the crucial data processing pipeline that takes user input from the forms and prepares it for the machine learning models.
    *   I integrated the pre-trained Scikit-learn and XGBoost models into the Flask backend, enabling real-time predictions.

*   **Frontend Development (HTML):**
    *   I designed and built the user interface templates for the login, registration, dashboard, and prediction forms.
    *   My focus was on creating a clean and intuitive user experience, ensuring the application is accessible and easy to navigate.

*   **Project Modernization & Debugging:**
    *   I took ownership of resolving critical runtime errors caused by an outdated virtual environment and an incomplete list of dependencies.
    *   I systematically debugged the application, identified all missing libraries, and rebuilt the `requirements.txt` file from the ground up.
    *   I refactored the codebase to remove incompatible legacy libraries (`Flask-Frozen`), ensuring the project is stable and runnable on modern systems.

---

### 🚀 Getting Started: Installation & Setup

These instructions have been tested and verified to get the application running correctly.

1.  **Clone your improved version of the repository:**
    ```bash
    git clone https://github.com/Vignesh2v04/disease_risk_pridictor.git
    cd disease_risk_pridictor
    ```

2.  **Create and activate a Python virtual environment:**
    ```bash
    # For Windows
    python -m venv venv
    .\\venv\\Scripts\\activate
    ```

3.  **Install all the corrected dependencies from the requirements file:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Flask application:**
    ```bash
    python app.py
    ```

5.  Open your web browser and navigate to **`http://127.0.0.1:5000`** to see the application live.
