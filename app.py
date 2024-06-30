from flask import Flask
from api.db import init_db, close_connection

def create_app():
    app = Flask(__name__)

    with app.app_context():
        init_db(app, 'userDB.db', 'api/models/schema.sql')
        init_db(app, 'placeDB.db', 'api/models/schema.sql')

        from api.routes.auth import auth_bp
        from api.routes.place import place_bp

        app.register_blueprint(auth_bp)
        app.register_blueprint(place_bp)

    app.teardown_appcontext(close_connection)
    
    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)