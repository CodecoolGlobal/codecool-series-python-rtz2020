from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')


def get_top_actors(limit):
    return data_manager.execute_select('''
        SELECT name, COUNT(show_characters.id) AS character_count FROM actors
        LEFT JOIN show_characters ON actors.id = show_characters.actor_id
        GROUP BY actors.id
        ORDER BY character_count DESC
        LIMIT %(limit)s
    ''', variables={'limit': limit})