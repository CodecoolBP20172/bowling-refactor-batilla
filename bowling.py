def score(game):
    game = str.upper(game)
    result = 0
    frame = 1
    # last_count = []
    in_first_half = True
    for i in range(len(game)):
        if game[i] == '/':
            result += 10 - last
        else:
            result += get_value(game[i])
            print(result)
        # if not in_first_half:
            # frame += 1
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
        # last_count.append(last)
        # print(last_count, "last")
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
