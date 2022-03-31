from fastapi import BackgroundTasks, FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse
from database import SessionLocal
from typing import List
import schemas
import models
from hashing import Hasher
import action

db = SessionLocal()


app = FastAPI()

@app.get("/")
def about():
    return {"FastApi"}


@app.post('/user',response_model=schemas.User ,status_code=201)
async def register(user: schemas.User, background_tasks: BackgroundTasks):
    find_user = action.finđ_user_by_emai(user.email)
    if find_user is None:
        new_user = models.User(
        name = user.name,
        email = user.email,
        pass_word = Hasher.password_hash(user.pass_word),
        is_verified = user.is_verified
    )
        send_email_backgroundtasks(background_tasks,user.email,user.name)

        db.add(new_user)
        db.commit()    
        return new_user
    else:
        return {
            "message" : "Email đã được sử dụng"
        }

@app.post('/login')
def login(user: schemas.UserLogin):
    find_user = action.finđ_user_by_emai(user.email)
    if find_user is not None:
        check_pass = Hasher.verify_password(user.pass_word,find_user.pass_word)
        if check_pass is True:
            return {
                "message" : "Đăng nhập thành công"
                }
        else:
            return {
                "message" : "Sai mật khẩu"
                }
    else:
        return {
            "message": "Sai tài khoản xin mời nhập lại"
            }

@app.get('/users', response_model=List[schemas.User], status_code=200)
async def get_all_user():
    users = db.query(models.User).all()

    return users


@app.get('/user/{user_id}')
def get_an_user(user_id:  int):
    user = db.query(models.User).filter(models.User.id==user_id).first()
    return user

@app.get('/user/{user_id}/profile',response_model=schemas.User, status_code=200)
def get_user_profile(user_id: int):
    user_profile = db.query(models.User).filter(models.User.id == user_id).first()
    return user_profile

@app.patch("/user/{user_id}/upload-images")
async def upload_user_images(
    user_id: int,
    file: UploadFile = File(..., description="Files as UploadFile")
):
    update_user = get_an_user(user_id)
    update_user.image_url = file.filename

    db.commit()
    return update_user

@app.get('/send-email/backgroundtasks')
def send_email_backgroundtasks(background_tasks: BackgroundTasks,email:str, name:str):
    action.send_email_background(background_tasks, 'Thank You Flow!', email, {'title': 'THANK YOU!', 'name':name})
    return 'Mời kiểm tra email xác nhận'


