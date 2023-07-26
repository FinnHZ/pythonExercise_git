

a = {"a1": "sdsa", 
     "b1": "sdsyry"}


b = {"a2": "ytuyt", 
     "b2": "jhgh"}


# a.update(b)
# print(dict(sorted(a.items(), key=lambda item: item[0])))

c = a | b

print(c)
print(
    dict(
        sorted(
            c.items(), key=lambda item: item[0]
            )
        )
    )