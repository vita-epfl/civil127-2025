for s in range(1, 10):
    for e in range(0, 10):
        if e == s:
            continue
        for n in range(0, 10):
            if n in {s, e}:
                continue
            for d in range(0, 10):
                if d in {s, e, n}:
                    continue
                for m in range(1, 10):
                    if m in {s, e, n, d}:
                        continue
                    for o in range(0, 10):
                        if o in {s, e, n, d, m}:
                            continue
                        for r in range(0, 10):
                            if r in {s, e, n, d, m, o}:
                                continue
                            for y in range(0, 10):
                                if y in {s, e, n, d, m, o, r}:
                                    continue
                                send = 1000*s + 100*e + 10*n + d
                                more = 1000*m + 100*o + 10*r + e
                                money = 10000*m + 1000*o + 100*n + 10*e + y
                                if send + more == money:
                                    print(
                                        "   {}\n+  {}\n  =====\n  {}".format(send, more, money))
