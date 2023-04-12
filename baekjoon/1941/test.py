a = "((((arstarstars))))"
b = "((((barsta rst arst))))"



lst = [b, a]

print(lst)

lst.sort(key=lambda x:len(x))

print(lst)