from tqdm import tqdm
n = 5
colors = ["r", "y", "g"]


def find_comb(lis_2d):
    p = 1
    for lis in lis_2d:
        p *= len(lis)
    return p


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


def to_structure(up, right, down, left, mid_h, mid_v):
    structure = []
    structure.append(up.lower())
    structure.append((left[1]+' '+mid_v[1]+' '+right[1]).lower())
    structure.append((mid_h.upper()).lower())
    structure.append((left[3]+' '+mid_v[3]+' '+right[3]).lower())
    structure.append((down).lower())
    return structure


def final_sat(up, right, down, left, mid_h, mid_v, center, all_letters):
    structure = to_structure(up, right, down, left, mid_h, mid_v)
    chars = lis_to_chars(structure)
    chars.sort()
    all_letters.sort()
    if chars != all_letters:
        return False
    if len(set([up, down, left, right, mid_v, mid_h])) != 6:
        return False
    if mid_v[2] != center or mid_h[2] != center:
        return False
    return True


def final_filter(fixed_clockwise, d, all_letters, horizontal_l):
    print("Searching filtered solutions...")
    pb = tqdm(total=find_comb(fixed_clockwise))
    for up in fixed_clockwise[0]:
        for right in fixed_clockwise[1]:
            for down in fixed_clockwise[2]:
                for left in fixed_clockwise[3]:
                    pb.update(n=1)
                    mid_hs = first_last(left[2]+right[2], d)
                    mid_vs = first_last(up[2]+down[2], d)
                    for mid_h in mid_hs:
                        for mid_v in mid_vs:
                            if final_sat(up, right, down, left, mid_h, mid_v, horizontal_l[1][2], all_letters):
                                return [up, right, down, left, mid_h, mid_v]
    return None
