lyrics = """
baby sukhwan tururu turu
very cute tururu turu
in bed tururu turu
baby sukhwan
""".split()
q, r = divmod(int(input())-1, 14)
mask = "00110011001100"
if mask[r] == "1":
    repeat = (q + 1) + ((r+1) % 2)
    ruPart = "+ru*"+str(repeat) if repeat >= 5 else "ru" * repeat
    print("tu" + ruPart)
else:
    print(lyrics[r])
