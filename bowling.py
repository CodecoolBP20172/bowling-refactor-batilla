def score(game):
    game = str.upper(game)
    result = 0
    frame = 1
    in_first_half = True
    for trow in range(len(game)):
        if game[trow] == '/':
            result += 10 - last
        else:
            result += get_value(game[trow])
        if frame < 10  and get_value(game[trow]) == 10:
            if game[trow] == '/':
                result += get_value(game[trow+1])
            elif game[trow] == 'X':
                result += get_value(game[trow+1])
                if game[trow+2] == '/':
                    result += 10 - get_value(game[trow+1])
                else:
                    result += get_value(game[trow+2])
        last = get_value(game[trow])
        if not in_first_half or game[trow] == 'X':
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
