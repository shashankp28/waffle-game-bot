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
all_letters = lis_to_chars(inputs_l)
horizontal_l = collect_horizontal(inputs_l)
vertical_l = collect_vertical(inputs_l)
horizontal_c = collect_horizontal(inputs_c)
vertical_c = collect_vertical(inputs_c)
d_change = []
for word in d:
    proper = True
    for letter in list(word):
        proper = proper and (all_letters.count(
            letter) >= list(word).count(letter))
    if proper:
        d_change.append(word)

d_change.sort()
perfect_candidates = [horizontal_l[0],
                      vertical_l[2], horizontal_l[2], vertical_l[0]]
fixed = [w[0]+w[4] for w in perfect_candidates]
fixed_clockwise = []
for fl in fixed:
    fixed_clockwise.append(first_last(fl, d_change))

try:
    up, right, down, left, mid_h, mid_v = final_filter(
        fixed_clockwise, d_change, all_letters, horizontal_l)
    print()
    print("Solution:")
    print(up.upper())
    print((left[1]+' '+mid_v[1]+' '+right[1]).upper())
    print(mid_h.upper())
    print((left[3]+' '+mid_v[3]+' '+right[3]).upper())
    print(down.upper())
except:
    print("Sorry Solution Not Found!")
