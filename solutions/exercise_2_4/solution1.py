def remove_every_k_element(N, K):
    active = K  # which person will be removed next
    people = list(range(N))

    while len(people) > 1:
        print("removing", people[active])
        people = people[:active] + people[active+1:]
        active = (active + K - 1) % len(people)
        print("remaining:", people)

remove_every_k_element(5, 2)
