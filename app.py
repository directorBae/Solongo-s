from flask import Flask

def create_app():
    app = Flask(__name__)

    with app.app_context():
        from api import init_app
        init_app(app)

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
