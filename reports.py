def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def open_file(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            text = f.read()
            games = split(text)
            return games
    except FileNotFoundError:
        print("Wrong file name.")
        exit()


def split(file_object):
    lines = (file_object.strip('\n').split('\n'))
    for index, line in enumerate(lines):
        lines[index] = line.split("\t")
    return lines


def count_games(file_name):
    return len(open_file(file_name))


def decide(file_name, year):
    games = open_file(file_name)
    return any(str(year) in sl for sl in games)


def get_latest(file_name):
    games = open_file(file_name)
    year = max([row[2] for row in games])
    for game in games:
        if year in game:
            return game[0]


def count_by_genre(file_name, genre):
    games = open_file(file_name)
    return len([row[0] for row in games if genre in row])


def get_line_number_by_title(file_name, title):
    games = open_file(file_name)
    for index, line in enumerate(games):
        if title.lower() == line[0].lower():
            return index + 1
    raise ValueError("Game not in file!")


def get_genres(file_name):
    games = open_file(file_name)
    return set([row[3] for row in games])


def sort_abc(file_name):
    games = open_file(file_name)
    games = [item[0] for item in games]  # tworzenie listy samych tytułów
    games = insertion_sort(games)
    return games


def when_was_top_sold_fps(file_name):
    games = open_file(file_name)
    top = (0, 0)
    for game in games:
        if game[3] == 'First-person shooter':
            if float(game[1]) > float(top[0]):
                top = (game[1], game[2])
    if top == (0, 0):
        raise ValueError("First-person shooter not found")
    else:
        return int(top[1])


# print(open_file("game_stat.txt"))
# print(count_games("game_stat.txt"))
# print(decide("game_stat.txt", 2004))
# print(get_latest("game_stat.txt"))
# print(count_by_genre("game_stat.txt", "RPG"))
# print(get_line_number_by_title("game_stat.txt", "Half-Life"))
