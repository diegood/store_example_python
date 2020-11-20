from minimart import app

@app.route('/')
def index():
    app.logger.warning('sample message')
    return  'HOLA'
