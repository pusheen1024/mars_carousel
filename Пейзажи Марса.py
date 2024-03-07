from flask import Flask, request, render_template, url_for
from werkzeug.utils import secure_filename

settings = dict()
app = Flask(__name__)


@app.route('/carousel')
def return_carousel():
    if 'pictures' not in settings:
        settings['pictures'] = [(f"{url_for('static', filename=f'img/{i}.jpg')}", f"mars_{i}") for i in range(1, 6)]
    return render_template('carousel.html', pictures=settings['pictures'])


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')