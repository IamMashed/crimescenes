from app import app, db
from datetime import datetime


class Crime(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float(10, 6))
    longitude = db.Column(db.Float(10, 6))
    date = db.Column(db.DATE)
    category = db.Column(db.String(50))
    description = db.Column(db.String(1000))
    updated_at = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        return '{}'.format(self.description)
        # return 'latitude {}, longitude {}'.format(self.latitude, self.longitude)

    def as_dict(self):
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}
