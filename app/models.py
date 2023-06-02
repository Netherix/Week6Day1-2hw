from app import db, login_manager
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String)
    created_on = db.Column(db.DateTime, default=datetime.utcnow())
    posts = db.relationship('Poke', backref='author', lazy='dynamic')

    # hashes our password when user signs up
    def hash_password(self, signup_password):
        return generate_password_hash(signup_password)
    
    # This method will assign our columns with their respective values
    def from_dict(self, user_data):
        self.first_name = user_data['first_name']
        self.last_name = user_data['last_name']
        self.email = user_data['email']
        self.password = self.hash_password(user_data['password'])


class Poke(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    img_url = db.Column(db.String, nullable=False)
    poke_name = db.Column(db.String, nullable=False)
    ability = db.Column(db.String, nullable=False)
    base_experience = db.Column(db.Integer, nullable=False)
    hp = db.Column(db.Integer, nullable=False)
    attack = db.Column(db.Integer, nullable=False)
    defense = db.Column(db.Integer, nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.utcnow())
    # FK
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


    # This method will assign our columns with their respective values
    def from_dict(self, poke_data):
        print(poke_data)
        self.img_url = poke_data['img_url']
        self.poke_name = poke_data['poke_name']
        self.ability = poke_data['ability']
        self.base_experience = poke_data['base_experience']
        self.hp = poke_data['hp']
        self.attack = poke_data['attack']
        self.defense = poke_data['defense']
        self.user_id = poke_data['user_id']

# only need the model


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

