from app import db
import os
import unicodedata

class User(db.Model):
	__tablename__ = "users"
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True)
	email = db.Column(db.String(50), unique=True)
	password = db.Column(db.String(20))

	@property
	def is_authenticated(self):
		return True

	@property
	def is_active(self):
		return True

	@property
	def is_anonymous(self):
		return False

	def get_id(self):
		return str(self.id)

	def __init__(self, username, password, email):
		self.username = username
		self.password = password
		self.email = email

	def __repr__(self):
		return "<User %r>" % self.username























