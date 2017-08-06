def score(game):
    game = str.upper(game)
    result = 0
    frame = 1
    in_first_half = True
    for i in range(len(game)):
        if game[i] == '/':
            result += spare(game, i)
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
        if not in_first_half:
            frame += 1
        if in_first_half == True:
            in_first_half = False
        else:
            in_first_half = True
        if game[i] == 'X':
            in_first_half = True
            frame += 1
    return result


def spare(game, i):
    if game[i] == '/':
        return (10 - get_value(game[i-1]))
    else:
        return get_value(game[i])


def get_value(char):
    if char.isdigit():
        return int(char)
    if char in "X/":
        return 10
    elif char == '-':
        return 0
    else:
        raise ValueError()


print(score("1/35XXX458/X3/23"))
