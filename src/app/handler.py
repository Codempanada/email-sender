from flask import jsonify


def register_error_handlers(app):
    # 400 - Bad Request
    @app.errorhandler(400)
    def bad_request(e):
        return jsonify(
            status=400,
            response="Bad Request"
        )

    # 403 - Forbidden
    @app.errorhandler(403)
    def forbidden(e):
        return jsonify(
            status=400,
            response="Forbidden"
        )

    # 404 - Page Not Found
    @app.errorhandler(404)
    def page_not_found(e):
        return jsonify(
            status=400,
            response="Path/Route Not Found"
        )

    # 405 - Method Not Allowed
    @app.errorhandler(405)
    def method_not_allowed(e):
        return jsonify(
            status=400,
            response="Method Not Allowed"
        )

    # 500 - Internal Server Error
    @app.errorhandler(500)
    def server_error(e):
        return jsonify(
            status=500,
            response="Server Error"
        )
