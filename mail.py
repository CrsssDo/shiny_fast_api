from fastapi_mail import ConnectionConfig

def Conf():
    conf = ConnectionConfig(
        MAIL_USERNAME="dobongsoon82@gmail.com",
        MAIL_PASSWORD="Nguyen12@",
        MAIL_FROM="dobongsoon82@gmail.com",
        MAIL_PORT=587,
        MAIL_SERVER="smtp.gmail.com",
        MAIL_FROM_NAME="Shiny Team",
        MAIL_TLS=True,
        MAIL_SSL=False,
        TEMPLATE_FOLDER='templates/'
    )

    return conf