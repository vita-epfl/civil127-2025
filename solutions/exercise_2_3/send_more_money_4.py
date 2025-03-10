# You'll need to first install z3 (https://github.com/Z3Prover/z3/)
# there should be binary packages available for your operating
# system (e.g. via homebrew on MacOSX).
#
# You'll then need to `pip install z3-solver`

from z3 import Int, Solver, Distinct, sat

S, E, N, D, M, O, R, Y = Int('S'), Int('E'), Int(
    'N'), Int('D'), Int('M'), Int('O'), Int('R'), Int('Y')

solver = Solver()
solver.add(Distinct(S, E, N, D, M, O, R, Y))
solver.add(S >= 1, S <= 9)
solver.add(E >= 0, E <= 9)
solver.add(N >= 0, N <= 9)
solver.add(D >= 0, D <= 9)
solver.add(M >= 1, M <= 9)
solver.add(O >= 0, O <= 9)
solver.add(R >= 0, R <= 9)
solver.add(Y >= 0, Y <= 9)
solver.add(
    (S * 1000 + E * 100 + N * 10 + D) +
    (M * 1000 + O * 100 + R * 10 + E) ==
    (M * 10000 + O * 1000 + N * 100 + E * 10 + Y)
)

# Check if a solution exists
t = solver.check()
if t == sat:
    m = solver.model()
    send = "{}{}{}{}".format(m[S], m[E], m[N], m[D])
    more = "{}{}{}{}".format(m[M], m[O], m[R], m[E])
    money = "{}{}{}{}{}".format(m[M], m[O], m[N], m[E], m[Y])
    print("   {}\n+  {}\n  =====\n  {}".format(send, more, money))
else:
    print("No solution found.")
