import os
import smtplib
from email.message import EmailMessage
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import psycopg2

app = FastAPI(title="Military Service Application API")

# Ρυθμίσεις περιβάλλοντος (από Docker / Environment)
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "devops_db")
DB_USER = os.getenv("DB_USER", "devops_user")
DB_PASS = os.getenv("DB_PASS", "devops_password")
SMTP_HOST = os.getenv("SMTP_HOST", "localhost")
SMTP_PORT = int(os.getenv("SMTP_PORT", 1025))


class ApplicationRequest(BaseModel):
    full_name: str
    email: str
    action_type: str  # "deferment" (αναβολή) ή "enlistment" (κατάταξη)
    preferred_branch: str  # "army", "navy", "airforce"


def send_email_notification(to_email: str, subject: str, body: str):
    try:
        msg = EmailMessage()
        msg.set_content(body)
        msg["Subject"] = subject
        msg["From"] = "noreply@stratologia.gr"
        msg["To"] = to_email

        with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
            server.send_message(msg)
    except Exception as e:
        print(f"Error sending email: {e}")


@app.get("/")
def read_root():
    return {"status": "ok", "message": "Military Service API is running"}


@app.post("/applications/")
def create_application(app_req: ApplicationRequest):
    # 1. Αποθήκευση στη PostgreSQL
    try:
        conn = psycopg2.connect(
            host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS
        )
        cur = conn.cursor()
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS applications (
                id SERIAL PRIMARY KEY,
                full_name VARCHAR(100),
                email VARCHAR(100),
                action_type VARCHAR(50),
                preferred_branch VARCHAR(50),
                status VARCHAR(20) DEFAULT 'PENDING'
            )
        """
        )
        cur.execute(
            """
            INSERT INTO applications (full_name, email, action_type, preferred_branch)
            VALUES (%s, %s, %s, %s) RETURNING id
        """,
            (
                app_req.full_name,
                app_req.email,
                app_req.action_type,
                app_req.preferred_branch,
            ),
        )
        app_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Database connection error: {str(e)}"
        )

    # 2. Αποστολή Email Ενημέρωσης
    email_body = f"Γεια σας {app_req.full_name},\n\nΗ αίτησή σας ({app_req.action_type}) υποβλήθηκε επιτυχώς με αναγνωριστικό #{app_id}."
    send_email_notification(
        app_req.email, "Επιβεβαίωση Υποβολής Αίτησης", email_body
    )

    return {
        "id": app_id,
        "message": "Application submitted successfully",
        "status": "PENDING",
    }