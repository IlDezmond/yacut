from flask import flash, redirect, render_template, url_for

from . import app, db
from .forms import URLMapForm
from .models import URLMap
from .utils import generate_short_link


@app.route('/', methods=("GET", "POST"))
def index():
    form = URLMapForm()
    if form.validate_on_submit():
        original_link = form.original_link.data
        short_link = form.custom_id.data
        if short_link is None or short_link == '':
            short_link = generate_short_link(original_link)
        else:
            if not URLMap.short_link_not_exists(short_link):
                flash(f'Имя {short_link} уже занято!')
                return render_template('main.html', form=form)

        url_map = URLMap(
            original=form.original_link.data,
            short=short_link,
        )
        db.session.add(url_map)
        db.session.commit()
        return render_template(
            'main.html',
            form=form,
            short_link=url_for(
                'redirect_view',
                short_id=short_link,
                _external=True,
            )
        )
    return render_template('main.html', form=form)


@app.route('/<string:short_id>', strict_slashes=False)
def redirect_view(short_id: str):
    return redirect(
        URLMap.query.filter_by(short=short_id).first_or_404().original,
    )
