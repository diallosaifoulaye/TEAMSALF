#from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from appli import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_perso(perso_id):
    return Personnel.query.get(int(perso_id))

#########################################################################################
#TABLE PERSONNEL
#########################################################################################   
class Personnel(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(20), unique=True, nullable=False)
    image_file = db.Column (db.String(20), nullable=False, default='default.jpg')
    password = db.Column (db.String(60), nullable=False)
    def __repr__(self):
        return f"Personnel('{self.name}','{self.email}','{self.image_file}')"

class User(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(20), unique=True, nullable=False)
    image_file = db.Column (db.String(20), nullable=False, default='default.jpg')
    password = db.Column (db.String(60), nullable=False)
    #posts = db.relationship('Post', backref='author', lazy=True)
    
    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"
#########################################################################################
#TABLE COHORE
#########################################################################################
class Cohorte(db.Model):
    idtalent = db.Column(db.Integer, primary_key=True)
    phase = db.Column(db.String(100), nullable=False)
    nom = db.Column(db.String(100), nullable=False)
    prenom = db.Column(db.String(100), nullable=False) 
    email = db.Column(db.String(100), nullable=False)  
    option = db.Column(db.String(100), nullable=False)  
    tptotal = db.Column(db.Integer, nullable=False)
    tpfait = db.Column(db.Integer, nullable=False) 
    totalmakersday = db.Column(db.Integer, nullable=False) 
    abscencemakersday = db.Column(db.Integer, nullable=False) 
    totalquiz = db.Column(db.Integer, nullable=False) 
    quizfait = db.Column(db.Integer, nullable=False)
    moisnonpaye= db.Column(db.Integer, nullable=False)
   # detail = db.relationship('DetailT', backref='author', lazy=True)

    def __repr__(self):
        return f"Cohorte('{self.phase}','{self.nom}','{self.prenom}','{self.email}','{self.option}')"
#########################################################################################
#TABLE DETAIL TALENT
#########################################################################################
'''class DetailT(db.Model):
    idphase = db.Column(db.Integer, primary_key=True)
    tptotal = db.Column(db.Integer, nullable=False)
    tpfait = db.Column(db.Integer, nullable=False) 
    totalmakersday = db.Column(db.Integer, nullable=False) 
    abscencemakersday = db.Column(db.Integer, nullable=False) 
    totalquiz = db.Column(db.Integer, nullable=False) 
    quizfait = db.Column(db.Integer, nullable=False)
    moisnonpaye= db.Column(db.Integer, nullable=False)
    cohorte_id = db.Column(db.Integer, db.ForeignKey('cohorte.idtalent'), nullable=False)

    def __repr__(self):
        return f"DetailT('{self.idphase}','{self.phase}','{self.tptotal}','{self.tpfait}','{self.totalmakersday}', '{self.totalquiz}','{self.quizfait}','{self.moisnonpaye}')"
'''
#db.create_all()
