from minimart import db, api
from minimart.models.working_hours import WorkingHours
from flask_restx import fields


class Store(db.Model):
    __tablename__ = 'stores'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    logo = db.Column(db.String(255))
    address = db.Column(db.String(255))
    working_hours = db.relationship(WorkingHours, backref=db.backref(
        'stores', lazy='joined'), cascade="all", uselist=False)

    def __init__(self, name, logo, address, working_hours):
        self.name = name
        self.logo = logo
        self.address = address
        self.working_hours = working_hours

    def __ref__(self):
        return self.id

    def swagger(edit=False):
        schema = {
            'id': fields.Integer(readonly=True, description='The store unique identifier'),
            'name': fields.String(required=True, description='Store name', example='COCO Downtown'),
            'logo': fields.String(required=True, description='Store logo url', example='https://www.sightseeingpass.com/images/attractions/attraction-images-670x270/san-francisco/attimg_cocofreshteajuice1_large.jpg'),
            'address': fields.String(required=True, description='Pysical store address', example='742 Evergreen Terrace, Springfield'),
            'working_hours': fields.Nested(WorkingHours.swaggerSchema())
        }
        if edit:
            del schema['name']
            del schema['address']
        return api.model('StoreBase', schema)
