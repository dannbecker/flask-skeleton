from app import db

class User(db.Model):
    __tablename__ = "user"

    # Abaixo os campos da tabela

    id = db.Column(db.Integer, primary_key=True)

    CREATED_AT = db.Column(db.DateTime, nullable=True)
    DELETED_AT = db.Column(db.DateTime, nullable=True)

    # Campos de login

    email = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(128), nullable=False)

    # Campos de informação do usuário

    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128), nullable=False)

    def fullName(self, first_name, last_name):
        return f"{first_name + ' ' + last_name}"