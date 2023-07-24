from http import HTTPStatus

from flask import jsonify, request, url_for

from yacut import app, db
from .exceptions import APIError
from .models import URLMap
from .utils import generate_short_link, regex_short_link_validate


@app.route('/api/id/<string:short_url>/', methods=['GET'])
def get_original_link_api(short_url):
    original_link = URLMap.query.filter_by(short=short_url).first()
    if original_link is None:
        raise APIError('Указанный id не найден', HTTPStatus.NOT_FOUND)
    return jsonify({'url': original_link.original}), HTTPStatus.OK


@app.route('/api/id/', methods=['POST'])
def add_link_api():
    data = request.get_json(silent=True)
    if data is None:
        raise APIError('Отсутствует тело запроса')
    long_url = data.get('url')
    if long_url is None:
        raise APIError('"url" является обязательным полем!')
    short_link = data.get('custom_id')
    if short_link is None or short_link == '':
        short_link = generate_short_link(long_url)
    else:
        if not URLMap.short_link_not_exists(short_link):
            raise APIError(f'Имя "{short_link}" уже занято.')
        if not regex_short_link_validate(short_link):
            raise APIError('Указано недопустимое имя для короткой ссылки')
    instance = URLMap(
        original=long_url,
        short=short_link,
    )
    db.session.add(instance)
    db.session.commit()
    return jsonify(
        dict(
            url=data.get('url'),
            short_link=url_for(
                'redirect_view',
                short_id=short_link,
                _external=True
            ),
        )
    ), HTTPStatus.CREATED
