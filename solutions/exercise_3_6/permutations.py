def permutations(coinage, sum):
    solutions = []
    permutations2(coinage, sum, [], solutions)
    for i, solution in enumerate(solutions):
        print("{}. {}".format(i+1, solution))


def permutations2(coinage, remaining, used, solutions):
    """ Recursively solve the coinage problem.
        coinage: list of coins we can use.
        remaining: amount remaining from our target sum.
        used: list of strings representing what coins we have used so far.
        solutions: list of strings we push solutions to. """
    if remaining == 0:
        # we have found a solution, so we record it
        solutions.append(", ".join(used))
        return
    elif coinage == []:
        # we don't have any more coins left
        return

    # each recursive call into permutations2 will consume one coin from coinage
    current_coin = coinage[0]

    # use integer division to figure out the upper bound for how many of the
    # current coin we can use.
    max = remaining // current_coin

    # case where we use the current coin between 1 and max (inclusive) times
    for i in range(1, max+1):
        # notice: we don't want to mutate the used list, so we use list
        # concatenation instead of append.
        permutations2(coinage[1:], remaining - i * current_coin,
                      used + ["${} x {}".format(current_coin, i)], solutions)

    # We don't want to record when we don't use a coin (i.e. we don't want "$2 x 0"),
    # so we special case i=0.
    permutations2(coinage[1:], remaining, used, solutions)


permutations([2, 3, 7], 40)

