name="my name is sandeep"
rev=""
for i in name:
    if i[::-1]:
        print(i)

name="my name is sandeep"
words=name.split()
reversed_words=words[::-1]
result=" ".join(reversed_words)
print("reversed string is:",result)
