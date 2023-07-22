from flask import jsonify, render_template

from yacut import app, db
from yacut.exceptions import APIError


@app.errorhandler(APIError)
def invalid_api_usage(error):
    return jsonify(error.to_dict()), error.status_code


@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html', error_message='404'), 404


@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('error.html', error_message='500'), 500
