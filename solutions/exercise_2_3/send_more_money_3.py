from itertools import permutations

for (s, e, n, d, m, o, r, y) in permutations(range(0, 10), r=8):
  if s == 0 or m == 0:
    continue
  send = 1000*s + 100*e + 10*n + d
  more = 1000*m + 100*o + 10*r + e
  money = 10000*m + 1000*o + 100*n + 10*e + y
  if send + more == money:
    print("   {}\n+  {}\n  =====\n  {}".format(send, more , money))
