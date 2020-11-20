from minimart import db


class Store(db.Model):
    __tablename__ = 'stores'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    logo = db.Column(db.String(255))
    address = db.Column(db.String(255))
    work_hours = db.Column(db.String(255))

    def __init__(self, name, address):
        self.address = address
        self.name = name

    def __ref__(self):
        return self.id
