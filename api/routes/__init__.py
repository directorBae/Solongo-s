def init_routes(app):
    from .agent import agent_bp
    from .auth import auth_bp
    from .chatlog import chatlog_bp
    from .pallete import pallete_bp
    from .pathfind import pathfind_bp
    from .place import place_bp
    from .purchase import purchase_bp
    from .status import status_bp

    app.register_blueprint(agent_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(chatlog_bp)
    app.register_blueprint(pallete_bp)
    app.register_blueprint(pathfind_bp)
    app.register_blueprint(place_bp)
    app.register_blueprint(purchase_bp)
    app.register_blueprint(status_bp)

