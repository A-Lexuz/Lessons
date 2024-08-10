def all_variants(text):
    for i in range(len(text)):
        for u in range(len(text)-i):
            yield text[u:u+i+1]

a = all_variants("abc")
for i in a:
    print(i)