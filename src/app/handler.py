from flask import jsonify

def register_error_handlers(app):
    
    # 400 - Bad Request
    @app.errorhandler(400)
    def bad_request(e):
        return jsonify()

    # 403 - Forbidden
    @app.errorhandler(403)
    def forbidden(e):
        return jsonify()

    # 404 - Page Not Found
    @app.errorhandler(404)
    def page_not_found(e):
        return jsonify()

    # 405 - Method Not Allowed
    @app.errorhandler(405)
    def method_not_allowed(e):
        return jsonify()

    # 500 - Internal Server Error
    @app.errorhandler(500)
    def server_error(e):
        return jsonify()