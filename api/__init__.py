def init_app(app):
    from .routes import init_routes
    init_routes(app)
