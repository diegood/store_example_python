from minimart import db, api
from minimart.models.working_hours import WorkingHours
from flask_restx import fields


class Store(db.Model):
    __tablename__ = 'stores'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    logo = db.Column(db.String(255))
    address = db.Column(db.String(255))
    work_hours = db.relationship(WorkingHours, backref='stores', cascade="all", lazy='dynamic')

    def __init__(self, name, address):
        self.address = address
        self.name = name

    def __ref__(self):
        return self.id

    def swagger():
        return api.model('StoreBase', {
            'id': fields.Integer(readonly=True, description='The store unique identifier'),
            'name': fields.String(required=True, description='Store name', example='COCO Downtown' ),
            'logo': fields.Url(required=True, description='Store logo url', example='https://www.sightseeingpass.com/images/attractions/attraction-images-670x270/san-francisco/attimg_cocofreshteajuice1_large.jpg'),
            'address': fields.String(required=True, description='Pysical store address', example='742 Evergreen Terrace, Springfield'),
            'work_addres': fields.Nested(WorkingHours.swaggerSchema())
        })
