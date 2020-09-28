from app.database import db
import string
from random import choice

class Links(db.Model):
    __tablename__ = 'links'
    id = db.Column(db.Integer, primary_key=True)
    old_link = db.Column(db.String(500), nullable=False)
    new_link = db.Column(db.String(50), nullable=False)

    def add(self):
        db.session.add(self)
        db.session.commit()

    def query_link(self, new_url):
        query = self.query.filter_by(new_link=new_url).first()
        return query.old_link

    @staticmethod
    def generateNewLink(StringLength=6):
        generate = string.ascii_lowercase + string.ascii_uppercase + string.digits
        return ''.join(choice(generate) for i in range(StringLength))