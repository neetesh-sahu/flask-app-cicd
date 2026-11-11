from flask import jsonify

def register_routes(app):

    @app.route("/")
    def home():
        return jsonify({
            "message": "Flask CI/CD Pipeline is Running!",
            "status": "success",
            "technology": "Python Flask + Docker"
        })

    @app.route("/health")
    def health():
        return jsonify({
            "status": "healthy"
        }), 200

    @app.route("/api/info")
    def info():
        return jsonify({
            "project": "Flask Docker CI/CD",
            "version": "1.0.0",
            "deployment": "Automated",
            "platform": "Pop!_OS"
        })