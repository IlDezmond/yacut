from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms.fields import StringField
from wtforms.validators import (DataRequired, Optional, Regexp, URL)


class URLMapForm(FlaskForm):
    original_link = StringField(
        'Адрес URL',
        description='https://example.com',
        validators=(
            DataRequired(message='Обязательное поле.'),
            URL(message='Некорректный адрес URL.'),
        ),
    )
    custom_id = StringField(
        'Идентификатор ссылки',
        description='Идентификатор ссылки',
        validators=(
            Regexp(
                r'^[a-zA-Z0-9]{2,16}$',
                message=(
                    'Идентификатор может состоять только '
                    'из латинских букв и цифр.'
                    'Длина 6-16 символов.'
                ),
            ),
            Optional(),
        ),
    )
    submit = SubmitField('Сократить')
