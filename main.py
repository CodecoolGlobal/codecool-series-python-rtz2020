from flask import Flask, render_template, url_for, request
from data import queries, data_manager
import math

app = Flask('codecool_series')


@app.route('/')
def index():
    shows = queries.get_shows()
    return render_template('index.html', shows=shows)


@app.route('/design')
def design():
    return render_template('design.html')


@app.route('/shows', methods=["GET", "POST"])
@app.route('/shows/most-rated/<int:page>', methods=["GET", "POST"])
def most_rated(page=0):
    counter = 0
    order_by = request.args.get('order_by')
    ascdesc = request.args.get('order')
    last_page_data = queries.get_last_page()
    last_page = math.ceil(last_page_data[0]['last_page']/15)
    for pages in range(0, last_page):
        if page == pages:
            counter = pages * 15
            if order_by:
                data = queries.get_most_rated(order_by, ascdesc, counter)
            else:
                data = queries.get_most_rated(2, "ASC", counter)
            return render_template('top.html', data=data, page=page)


@app.route('/show/<id>', methods=["GET", "POST"])
def show_data(id):
    actors = queries.get_actors_by_show_id(id)
    seasons = queries.get_seasons_data_by_id(id)
    details = queries.get_show_details(id)
    genres = queries.get_show_genre_by_id(id)
    return render_template('show.html', details=details, genres=genres, actors=actors, seasons=seasons)


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
