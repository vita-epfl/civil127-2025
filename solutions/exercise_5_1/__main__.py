from exercise_5_1.search import search

for i in range(1, 7):
    start = 10 ** i
    end = 10 ** (i+1)
    print(f"range: [{start}, {end-1}] ({i+1} digits)")
    r = range(start, end)
    search(r)
    print()
