def score(game):
    game = str.upper(game)
    result = 0
    frame = 1
    in_first_half = True
    for i in range(len(game)):
        if game[i] == '/':
            result += 10 - last
        else:
            result += get_value(game[i])
        if frame < 10  and get_value(game[i]) == 10:
            if game[i] == '/':
                result += get_value(game[i+1])
            elif game[i] == 'X':
                result += get_value(game[i+1])
                if game[i+2] == '/':
                    result += 10 - get_value(game[i+1])
                else:
                    result += get_value(game[i+2])
        last = get_value(game[i])
        if not in_first_half or game[i] == 'X':
            frame += 1
            in_first_half = True
        else:
            in_first_half = False
    return result


def get_value(char):
    if char.isdigit():
        return int(char)
    if char in "X/":
        return 10
    else:
        return 0
