def split(file_object):
    lines = (file_object.strip('\n').split('\n'))
    for index, line in enumerate(lines):
        lines[index] = line.split("\t")
    return lines


def open_file(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            text = f.read()
            games = split(text)
            return games
    except FileNotFoundError:
        print("Wrong file name.")
        exit()


def count_by_genre(file_name, genre):
    games = open_file(file_name)
    return len([row[0] for row in games if genre in row])


def count_games(file_name):
    return len(open_file(file_name))


def get_genres(file_name):
    games = open_file(file_name)
    return set([row[3] for row in games])


def get_most_played(file_name):
    games = open_file(file_name)
    most_played = ('', 0)
    for game in games:
        if float(game[1]) > most_played[1]:
            most_played = (game[0], float(game[1]))
    return most_played[0]


def sum_sold(file_name):
    games = open_file(file_name)
    return sum([float(row[1]) for row in games])


def get_selling_avg(file_name):
    return sum_sold(file_name)/count_games(file_name)


def count_longest_title(file_name):
    games = open_file(file_name)
    longest = max([row[0] for row in games], key=len)
    return len(longest)


def get_date_avg(file_name):
    games = open_file(file_name)
    sum_years = sum([float(row[2]) for row in games])
    return round(sum_years / count_games(file_name))


def get_game(file_name, title):
    games = open_file(file_name)
    for game in games:
        if title in game:
            game[1] = float(game[1])
            game[2] = int(game[2])
            return game


def count_grouped_by_genre(file_name):
    genre_count = {}
    genres = get_genres(file_name)
    for genre in genres:
        genre_count[genre] = count_by_genre(file_name, genre)
    return genre_count
