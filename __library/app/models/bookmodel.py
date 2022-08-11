from app.app import db

class Books(db.Document) :
	bname = db.StringField(required=True)
	category = db.StringField(required=True)
	rent_per_day = db.IntField(required=True)
	bookid = db.StringField(required=True)
