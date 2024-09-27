from flask import render_template
from app import create_app
import os

app = create_app()

# Handler de error 404
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)


# Creacion de ruta principal
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    print("is prod: ",os.getenv('PRODUCTION'))

    if os.getenv('PRODUCTION'):
        os.system('python dbCreator.py')
    
    port = int(os.environ.get('PORT', 5000))

    app.run(host='0.0.0.0', port=port, debug=True)