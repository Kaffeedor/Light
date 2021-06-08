from colour import Color

c = Color("blue")
g = Color("green")
li = list(c.range_to(g, 111))

for i in li:
    print(i.get_hex())

