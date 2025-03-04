# EPFL CIVIL-127, Lab 3

This exercise session will focus on Object Oriented Programming (OOP) and
automated testing.

## Exercise 3.1

A stack is a last in, first out (LIFO) data structure. The data that gets pushed
last gets popped first. Stacks are commonly used to implement features such as
undo in a word processor. They can also be used when solving search problems
(such as depth first searches). Recursive functions (such as `rlc` in exercise
1.4) make use of an implicit stack since function arguments live on a stack.

```txt
Example:

We start with an empty stack:

|   |
|   |
|   |
 ---


We then push(1):

|   |
|   |
| 1 |
 ---

Followed with push(5):

|   |
| 5 |
| 1 |
 ---

We then push(9):

| 9 |
| 5 |
| 1 |
 ---

A pop() should return 9:

|   |
| 5 |
| 1 |
 ---

push(2):

| 2 |
| 5 |
| 1 |
 ---
```

Implement a Stack class which works with integers and gives you the maximum
and minimum values currently in the stack. Your class should have the following
API:

  - push(int)
  - pop() -> int
  - max() -> int
  - min() -> int

For example:

```python
s = Stack()
s.push(1)
s.push(5)
print(s.max()) # should print 5
s.push(9)
print(s.pop()) # should print 9
s.push(2)
print(s.max()) # should print 5
```

There are at least two ways to implement `max()` and `min()`. You can either
iterate over the stack’s data (an operation with O(n) runtime, where n is the
stack size), or you can use additional storage and return the result instantly
(making these operations O(1) runtime). Implement both versions. How much
additional space does the O(1) version take?

This kind of speed⇔memory tradeoff is very common in software engineering.
Donald Knuth said “premature optimization is the root of all evil”. Looking at
both your implementations, do you relate to this piece of wisdom? Your O(1)
implementation is likely to be more complex than the O(n) version. Such
optimizations should therefore only be implemented when sure about their
benefits.

## Exercise 3.2

Implement tests for your stack class. Did writing tests reveal any bugs in your
code? You can also exchange tests with your peers.

Did your tests cover the following edge cases?
- Poping when the stack is empty
- Calling `max()` or `min()` when the stack is empty?

## Exercise 3.3

Note: We recommend using `git` to track your code changes. You may however
skip using `git` for this and the remaining labs if you want to focus on the
coding side of things. We understand that `git` has a learning curve.

Refactor your Sokoban code from labs 1 and 2 and use classes. You should
end up with at least a Model, a View, and a Controller class. You might
have additional classes.

If you are using `git` to track your code changes, your refactor should be
split into small commits (somewhere between 3-5 commits). As you prepare
each commit, make sure your game still works.

## Exercise 3.4

Write unittests for your code. Your tests should check that:

  - a player can move to an empty space
  - a player cannot move into a wall
  - a player can push a box if the box will occupy an empty space
  - a player cannot push a box if another box is blocking it
  - a player cannot push a box if a wall is blocking it

You can use the existing level data or create your own simpler level data for
the purpose of writing tests.

## Exercise 3.5 (optional)

```python
def wrap_underscores(word):
    '''Adds an underscore between each letter. E.g. "hello" becomes "_h_e_l_l_o_".'''
    r = "_"
    for i in range(len(word)):
        r = word[i] + "_"
    return r
```

`wrap_underscores` is meant to surround each character in `word` with
underscores. The code is however buggy. Write a unittest to demonstrate that the
code does not work. Then locate and fix the bug.

## Exercise 3.6 (optional)
A country has the following coinage: $2, $3, $7. We want to know how many
different ways we can represent $40. Write a function which takes a list of
coinage and a target sum and returns all the permutations.

E.g.
```python
def permutations(coinage, sum):
   …
```

```txt
> permutations([2, 3, 7], 40)
1. $2 x 20
2. $2 x 15, $3 x 1, $7 x 1
…
```
