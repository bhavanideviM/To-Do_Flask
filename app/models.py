from flask_sqlalchemy import SQLAlchemy
from app import db 

class Todo(db.Model): 
	id = db.Column(db.Integer, primary_key=True) 
	text = db.Column(db.String(200), nullable=False) 
	complete = db.Column(db.Boolean, default=False) 

	def __repr__(self): 
		return self.text 
