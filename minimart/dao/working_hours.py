from minimart import ma
from minimart.models.working_hours import WorkingHours


class WorkingHoursDao(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = WorkingHours
    
    id = ma.auto_field()
    store_id = ma.auto_field()
    monday_open = ma.auto_field()
    monday_close = ma.auto_field()
    tuesday_open = ma.auto_field()
    tuesday_close = ma.auto_field()
    wednesday_open = ma.auto_field()
    wednesday_close = ma.auto_field()
    thursaday_open = ma.auto_field()
    thursaday_close = ma.auto_field()
    friday_open = ma.auto_field()
    friday_close = ma.auto_field()
    saturday_open = ma.auto_field()
    saturday_close = ma.auto_field()
    sunday_open = ma.auto_field()
    sunday_close = ma.auto_field()
