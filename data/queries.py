from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')


def get_most_rated(pages, ascdesc, counter):
    return data_manager.execute_select(
        f'''SELECT  shows.id,title, shows.year, runtime, ROUND(rating,2) AS rating, string_agg(genres.name::character varying, ', ') AS genre, homepage, trailer
        FROM shows
        INNER JOIN show_genres ON shows.id = show_genres.show_id
        INNER JOIN genres ON show_genres.genre_id = genres.id
        GROUP BY 1, 2, 3, 4, 5, 7, 8
        ORDER BY {pages} {ascdesc}
        LIMIT 15
        OFFSET {counter}''')


def get_last_page():
    return data_manager.execute_select(
        '''SELECT COUNT(id) AS last_page
        FROM SHOWS'''
    )

def get_actors_by_show_id(show_id):
    return data_manager.execute_select(
        f'''SELECT DISTINCT shows.id, string_agg(actors.name::character varying, ', ') AS actors
        FROM shows
        INNER JOIN show_characters ON shows.id = show_characters.show_id
        INNER JOIN actors ON actors.id = show_characters.actor_id
        WHERE shows.id = {show_id}
        GROUP BY 1
        LIMIT 3
        '''
    )


def get_seasons_data_by_id(show_id):
    return data_manager.execute_select(
        f'''SELECT shows.id AS show_id,
        shows.title AS show_name,
        seasons.*
        FROM shows
        INNER JOIN seasons ON seasons.show_id = shows.id
        WHERE shows.id = {show_id}
        GROUP BY 1, 2, 3
        ORDER BY 2
        '''
    )


def get_show_details(show_id):
    return data_manager.execute_select(
        f'''SELECT title, shows.year, runtime, ROUND(rating,2) AS rating,overview, homepage, trailer
        FROM shows
        WHERE id = {show_id}
        '''
    )


def get_show_genre_by_id(show_id):
    return data_manager.execute_select(
        f'''SELECT DISTINCT shows.id, string_agg(genres.name::character varying, ', ') AS genre FROM shows
        INNER JOIN show_genres ON shows.id = show_genres.show_id
        INNER JOIN genres ON genres.id = show_genres.genre_id
        WHERE shows.id = {show_id}
        GROUP BY 1
        '''
    )
