from fastapi_mail import MessageSchema, FastMail
from mail import Conf
from fastapi import BackgroundTasks
from database import SessionLocal
import models

conf = Conf()

db = SessionLocal()

def send_email_background(background_tasks: BackgroundTasks, subject: str, email_to: str, body: dict):
    message = MessageSchema(
        subject=subject,
        recipients=[email_to],
        template_body=body,
        subtype='html')
    fm = FastMail(conf)
    background_tasks.add_task(
        fm.send_message, message, template_name='email.html')

def finđ_user_by_emai(email: str):
    user = db.query(models.User).filter(models.User.email == email).first()
    return user