from datetime import datetime
from d_growth.extentions import db
from sqlalchemy import Sequence


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, Sequence('User_id_Seq', start=1001), primary_key=True)
    created_on = db.Column(db.DateTime())
    name = db.Column(db.String())
    gender = db.Column(db.String())
    dob = db.Column(db.Date())

    growths = db.relationship("GrowthDetails", cascade="save-update, delete")

    def __init__(self, appstruct):
        self.created_on = datetime.now()
        self.name = appstruct['name']
        self.gender = appstruct.get('gender')
        self.dob = appstruct.get('dob')

    def update(self, appstruct):
        self.name = appstruct['name']
        self.gender = appstruct['gender']
        self.dob = appstruct.get('dob')


class GrowthDetails(db.Model):
    __tablename__ = 'growth_details'
    id = db.Column(db.Integer, Sequence('Growth_id_Seq', start=1001), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'), index=True)
    height = db.Column(db.String())
    weight = db.Column(db.String())
    date = db.Column(db.Date())

    def __init__(self, appstruct):
        self.user_id = appstruct['user_id']
        self.height = appstruct['height']
        self.weight = appstruct['weight']
        self.date = appstruct['date']
