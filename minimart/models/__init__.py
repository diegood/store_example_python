from minimart import db


import minimart.models.store

storeinstace = store.Store('lo de waz', 'saraza')
db.create_all()
db.session.add(storeinstace)
db.session.commit()
