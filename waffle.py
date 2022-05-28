from functions import *

inputs_l = []
inputs_c = []
horizontal_l = []
vertical_l = []
d = []
f = open("dict.txt", "r+")
for line in f:
    d.append(line.strip("\n").lower())
f.close()

print("Input Format for letters:")
print("VALUE")
print("I I S")
print("VOMIT")
print("I I E")
print("DETER")
print()
print("Input Format for Colors:")
print("Similar to letters with R = Gray, Y = Yellow, G = Green")
print()

while True:
    inputs_l = []
    inputs_c = []
    print("Input initial configuration (letters):")
    for i in range(n):
        inputs_l.append(list(input().lower()))
    if not verify_positions(inputs_l):
        print("Wrong letter format please try again")
        print()
        continue
    print()

    print("Input initial configuration (colors):")
    for i in range(n):
        inputs_c.append(list(input().lower()))
    if not verify_colors(inputs_c):
        print("Wrong color format please try again")
        print()
        continue
    print()
    break

horizontal_l = collect_horizontal(inputs_l)
vertical_l = collect_vertical(inputs_l)

horizontal_c = collect_horizontal(inputs_c)
vertical_c = collect_vertical(inputs_c)

d_change = []
for guess, feed in zip(horizontal_l+vertical_l, horizontal_c+vertical_c):
    temp = d[:]
    d_change += change(temp, feed, guess)

# print(d_change)
all_letters = lis_to_chars(inputs_l)
d_change2 = []
for word in d_change:
    proper = True
    for letter in list(word):
        proper = proper and (all_letters.count(
            letter) >= list(word).count(letter))
    if proper:
        d_change2.append(word)

d_change2.sort()
# print(d_change2)
perfect_candidates = [horizontal_l[0],
                      vertical_l[2], horizontal_l[2], vertical_l[0]]
fixed = [w[0]+w[4] for w in perfect_candidates]

fixed_clockwise = []
for fl in fixed:
    fixed_clockwise.append(first_last(fl, d_change2))

sol = False
for up in fixed_clockwise[0]:
    if sol:
        break
    for right in fixed_clockwise[1]:
        if sol:
            break
        for down in fixed_clockwise[2]:
            if sol:
                break
            for left in fixed_clockwise[3]:
                if sol:
                    break
                mid_hs = first_last(left[2]+right[2], d_change2)
                mid_vs = first_last(up[2]+down[2], d_change2)
                for mid_h in mid_hs:
                    if sol:
                        break
                    for mid_v in mid_vs:
                        if final_sat(up, right, down, left, mid_h, mid_v, horizontal_l[2][2]):
                            sol = True
                            break

# print(up, right, down, left, mid_h, mid_v)

try:
    print("Solution:")
    print(up.upper())
    print((left[1]+' '+mid_v[1]+' '+right[1]).upper())
    print(mid_h.upper())
    print((left[3]+' '+mid_v[3]+' '+right[3]).upper())
    print(down.upper())
except:
    print("Sorry Solution Not Found!")
