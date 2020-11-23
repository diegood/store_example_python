from minimart import db


import minimart.models.store
import minimart.models.working_hours

storeinstace = store.Store('lo de waz', 'saraza')
db.create_all()
db.session.add(storeinstace)
db.session.commit()
