n = 5
colors = ["r", "y", "g"]


def to_str(lis):
    return ''.join(lis)


def collect_horizontal(inputs):
    hors = []
    for i in range(0, n, 2):
        hors.append(to_str(inputs[i]))
    return hors


def collect_vertical(inputs):
    vers = []
    for i in range(0, n, 2):
        temp = []
        for j in range(n):
            temp.append(inputs[j][i])
        vers.append(to_str(temp))
    return vers


def verify_positions(inputs):
    ans = True
    if len(inputs) != n:
        return False
    for i in range(n):
        if(len(inputs[i])) != n:
            return False
    ans = ans and all([inputs[1][1] == ' ', inputs[1][3] == ' ',
                       inputs[3][1] == ' ', inputs[3][3] == ' '])
    return ans


def verify_colors(inputs):
    ans = True
    if not verify_positions(inputs):
        return False
    for i in range(n):
        if len(set(colors+[' ']) & set(inputs[i])) == 0:
            return False
    ans = ans and all([inputs[0][0] == 'g', inputs[0][4] == 'g',
                      inputs[4][0] == 'g', inputs[2][2] == 'g', inputs[4][4] == 'g'])
    return ans


def satisfy(x, feed, guess):
    x, feed, guess = [list(x), list(feed), list(guess)]
    for i in range(5):
        if guess[i] == x[i] and feed[i] == 'y':
            return False
    while feed.count('g') != 0:
        i = feed.index('g')
        if guess[i] != x[i]:
            return False
        else:
            guess.pop(i)
            x.pop(i)
            feed.pop(i)
    while feed.count('y') != 0:
        i = feed.index('y')
        if guess[i] not in x:
            return False
        else:
            x.pop(x.index(guess[i]))
            guess.pop(i)
            feed.pop(i)
    for i in range(len(guess)):
        if guess[i] in x:
            return False
    return True


def change(d, feed, guess):
    d = [x if satisfy(x, feed, guess) else '' for x in d]
    while d.count('') != 0:
        d.remove('')
    return d


def lis_to_chars(lis):
    chars = []
    for word in lis:
        chars += [ch for ch in list(word) if ch != ' ']
    return chars


def first_last(fl, lis):
    candidate = []
    for word in lis:
        if word[0] == fl[0] and word[4] == fl[1]:
            candidate.append(word)
    return candidate


def final_sat(up, right, down, left, mid_h, mid_v, center):
    if len(set([up, down, left, right, mid_v, mid_h])) != 6:
        return False
    if mid_v[2] != center or mid_h[2] != center:
        return False
    return True
