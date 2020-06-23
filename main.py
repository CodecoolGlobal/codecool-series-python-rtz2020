from flask import Flask, render_template

from data import queries

app = Flask('codecool_series')


@app.route('/')
def index():
    shows = queries.get_shows()
    return render_template('index.html', shows=shows)


@app.route('/design')
def design():
    return render_template('design.html')


@app.route('/top-actors')
def get_top_actors():
    top_actors = queries.get_top_actors(10)
    return render_template('top_actors.html', top_actors=top_actors, top_actors_length=len(top_actors))


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
