from minimart import db, api
from flask_restx import fields


class WorkingHours(db.Model):
    __tablename__ = 'working_hours'
    id = db.Column(db.Integer, primary_key=True)
    store_id = db.Column(db.Integer, db.ForeignKey(
        'stores.id'), nullable=False)
    monday_open = db.Column(db.DateTime())
    monday_close = db.Column(db.DateTime())
    tuesday_open = db.Column(db.DateTime())
    tuesday_close = db.Column(db.DateTime())
    wednesday_open = db.Column(db.DateTime())
    wednesday_close = db.Column(db.DateTime())
    thursaday_open = db.Column(db.DateTime())
    thursaday_close = db.Column(db.DateTime())
    friday_open = db.Column(db.DateTime())
    friday_close = db.Column(db.DateTime())
    saturday_open = db.Column(db.DateTime())
    saturday_close = db.Column(db.DateTime())
    sunday_open = db.Column(db.DateTime())
    sunday_close = db.Column(db.DateTime())

    def __init__(self, **kwargs):
        self.monday_open = kwargs['monday_open']
        self.monday_close = kwargs['monday_close']
        self.tuesday_open = kwargs['tuesday_open']
        self.tuesday_close = kwargs['tuesday_close']
        self.wednesday_open = kwargs['wednesday_open']
        self.wednesday_close = kwargs['wednesday_close']
        self.thursaday_open = kwargs['thursaday_open']
        self.thursaday_close = kwargs['thursaday_close']
        self.friday_open = kwargs['friday_open']
        self.friday_close = kwargs['friday_close']
        self.saturday_open = kwargs['saturday_open']
        self.saturday_close = kwargs['saturday_close']
        self.sunday_open = kwargs['sunday_open']
        self.sunday_close = kwargs['sunday_close']

    def swaggerSchema():
        return api.model('working_hours', {
            'monday_open': fields.DateTime(description='hours in which it opens on monday'),
            'monday_close': fields.DateTime(description='hours in which it close on monday'),
            'tuesday_open': fields.DateTime(description='hours in which it opens on tuesday'),
            'tuesday_close': fields.DateTime(description='hours in which it close on tuesday'),
            'wednesday_open': fields.DateTime(description='hours in which it opens on wednesday'),
            'wednesday_close': fields.DateTime(description='hours in which it close on wednesday'),
            'thursaday_open': fields.DateTime(description='hours in which it opens on thursaday'),
            'thursaday_close': fields.DateTime(description='hours in which it close on thursaday'),
            'friday_open': fields.DateTime(description='hours in which it opens on friday'),
            'friday_close': fields.DateTime(description='hours in which it close on friday'),
            'saturday_open': fields.DateTime(description='hours in which it opens on saturday'),
            'saturday_close': fields.DateTime(description='hours in which it close on saturday'),
            'sunday_open': fields.DateTime(description='hours in which it opens on sunday'),
            'sunday_close': fields.DateTime(description='hours in which it close on sunday')
        })
