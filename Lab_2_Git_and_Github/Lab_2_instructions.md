# EPFL CIVIL-127, Lab 2

The objective of this exercise session is to learn how to use git.

For a walkthough on the installation and setting up, please have a look at [here](https://weijiang1998.notion.site/Using-Git-in-VS-Code-and-Github-19f44b73854b809fa008c4b593054741?pvs=4) or the file "Using Git in VS Code and Github.md"

## Exercise 2.1

You will start by solving the first 15 levels (Introduction Sequence, Ramping Up, Moving Work Around, A Mixed Bag) of [learngitbranching](https://learngitbranching.js.org/).
It might take you some time to complete them, but it will teach you the commands you need to use git properly.

You can (optional) also solve all the remaining 19 levels (Advanced Topics, Push & Pull -- Git Remotes!, To Origin And Beyond -- Advanced Git Remotes!).

For the rest of this exercise session, the commands are provided for MacOS/Linux terminal. The line starts with a “$” sign, it is not part of the command you should use, the comments after the # signs are not to be pasted in your terminal either.

For Windows users, equivalent commands are provided as comments (e.g., those after a "#") or you can do equivalent things (usually coping files and changing folders) with the graphical user interface.
Concretely, the linux commands used in this exercise are `mkdir` `cp` `cd` `ls`, and the equivalent commands in windows are `mkdir` `copy` `cd` `dir`.
For a complete comparison, you can refer to https://www.geeksforgeeks.org/linux-vs-windows-commands.

## Exercise 2.2

Start by creating an empty git repository. You can use the following commands in the terminal:

```bash
$ mkdir sokoban  # “Make Directory” will create a new folder named “sokoban”
$ cd sokoban  # Move to the created folder (change directory)
$ git init  # This command will initialize a git repository in the current location
```

We will now create a commit with your Sokoban code from lab 1 (exercise 1.5). 
If you have not completed it, you can test these steps with any new file or the solution files.

Assume your codes are written in the file `sokoban.py`.
`<path_to_lab1_code>` (including `< >`) should be replaced with the actual path to the file, you can also choose to move it manually if you prefer. 
The dot `.` means all files in this folder. `cp` is the command to copy files. 

```bash
$ cp <path_to_lab1_code> .
$ git add sokoban.py  # Add the file 'sokoban.py' to git stage 
$ git commit -m "initial commit: data loader"  # Commits the changes with a message describing the commit.
```

Now create a git branch to work on the next feature. Creating branches allows you to work on new features or fixes without affecting the main code.

```bash
$ git switch -c player-box-movement # “-c <name>” will create a new branch <name>
```

Implement player and box movement. Prompt the user to enter “w, a, s, d” (or other keys if you prefer) and move the player accordingly (W for up, A for left, S for down, D for right if you have a Swiss keyboard, in the same fashion you would have in video games).

Use the existing getPlayerPosition(), isEmpty(), isBox() functions you previously implemented. Implement any helper functions you feel necessary.

If the move is valid, print the grid. If the move is invalid, print an explanation for why the it is invalid (e.g. “a wall is blocking you”, “a wall is blocking the box you are trying to move”, “another box is blocking the box you are trying to move”, etc.).

Now commit your code.

```bash
$ git add . # By doing this, you add all your files to the staging area.
$ git commit -m 'player and box movement implementation' # commit with a meaningful message
```

Your tree should now look something like:

```bash
“Initial commit: data loader” (main)
                             \-- “player and box movement implementation” (player-box-movement)
```

Let’s merge your branch with the main.

```bash
$ git switch main
$ git merge --no-ff player-box-movement # “--no-ff” keeps the branch history explicit.
$ git branch -d player-box-movement # Deletes the branch <player-box-movement>
```

Your tree should now look like this:

```bash
“Initial commit: data loader” <-- “player and box movement implementation” (player-box-movement) <-- merge (main)
```

Congrats! You’ve successfully initialized a Git repository, created and merged a feature branch for player and box movement, and maintained a clean commit history for structured development.

## Exercise 2.3 (optional)

```text
      SEND
    + MORE
      ----
     MONEY
```

“SEND + MORE = MONEY” is a classic math puzzle. The goal is to find integer values between 0 and 9 for each letter. Two different letters must have different values. S and M can’t be 0.

First, write a program to solve this puzzle without using any other Python libraries. You can start with a naive brute-force program that tries all possible combinations until it finds a solution..
Then, write another solution using any Python library you desire.

## Exercise 2.4 (optional)

N people are standing in a circle. They are numbered 0 to N-1 in clockwise order. Starting from the person numbered 0, every Kth person is removed from the circle. Write a program to calculate the number of the last person left in the circle.

E.g. if N=5 and K=2:

```text
Start:
  [0]
 4   1
  3 2

Step 1: 2 is removed
   0
 4   1
  3 x

Step 2: 4 is removed
   0
 x   1
  3 x

 Step 3: 1 is removed
   0
 x   x
  3 x


 Step 4: 0 is removed
   x
 x   x
  3 x
```

Answer is 3.
