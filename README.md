# Specification
You may work on this assignment in pairs. This should be an equal partnership and both of you should understand all the code you write.
Please read [this document](https://yale.instructure.com/courses/63186/files/4990276/download) to get some tips for successful pair programming.
If you prefer not to work with a partner, that's fine too. Depending on your personality and/or scheduling issues, you may be better off solo.
If you do pair programming, you can add your partner to your submission when you upload it on Gradescope (**only one of you needs to submit!**).
However, there is an additional requirement that each of you submit a brief individual statement summarizing your experience working on the assignment
and what you learned. You may add these to the end of the write-up document you will be submitting. Make sure it is clear who wrote which statement.

## Description
In this assignment you will take what you have learned about modeling problems with classes and design patterns, and build an application to play
Checkers (a.k.a. English Draughts). You will design the class structure yourself to implement the game logic. Then you will start writing simple AI players.

The next assignment will build on this one. There we will ask you to improve on your AI players and demonstrate the flexibility of your design by
extending it to variants of Checkers/Chess.

## Rules summary
These rules are adapted from the Wikipedia page for [english draughts](https://en.wikipedia.org/wiki/English_draughts).
I've made a couple tweaks to the setup part.

### Setup
Each player starts with peasants (single checkers, traditionally called men) on every white square within the three rows closest to that player's side.
The row closest to each player is called the kings row or crownhead. The white player starts at the bottom of the board (rows 6-8 for a normal size
board, see the figure). The player with the white pieces moves first. Then turns alternate.

### Move rules
There are two different ways to move in English draughts:
1. Simple move: A simple move consists of moving a piece one square diagonally to an adjacent unoccupied dark square. Peasants can move diagonally
forward only; kings can move in any diagonal direction.
2. Jump: A jump consists of moving a piece that is diagonally adjacent an opponent's piece, to an empty square immediately beyond it in the same
direction (thus "jumping over" the opponent's piece front and back). Peasants can jump diagonally forward only; kings can jump in any diagonal direction.
A jumped piece is considered "captured" and removed from the game. Any piece, king or peasant, can jump a king.

**Jumping is always mandatory**: if a player has the option to jump, he must take it, even if doing so results in disadvantage for the jumping player.
For example, a mandated single jump might set up the player such that the opponent has a multi-jump in reply.

Multiple jumps are possible, if after one jump, another piece is immediately eligible to be jumped—even if that jump is in a different diagonal direction.
If more than one multi-jump is available, the player can choose which piece to jump with, and which sequence of jumps to make. The sequence chosen is
not required to be the one that maximizes the number of jumps in the turn; however, a player must make all available jumps in the sequence chosen.

### Kings
If a peasant moves into the kings row on the opponent's side of the board, it is crowned as a king and gains the ability to move both forward and backward.
If a peasant moves into the kings row or if it jumps into the kings row, the current move terminates; the piece is crowned as a king but cannot jump back
out as in a multi-jump, until another move.

### End of game
A player wins by capturing all of the opponent's pieces. The game ends in a draw if either player still has pieces, but is left with no legal moves,
or if 50 turns pass without any pieces being captured.

## Requirements
- **20 points**. Construct an 8x8 checker board and set it up as described above. Begin the program by printing it to stdout. Below is an example.
There are a few important things to note about this output.
  - Typically pieces would start on and use only the black squares, but in all our examples here we are playing on the white squares, so stick to that
  in your implementations.
  - a1 is normally the bottom left black square, but we will label the rows in the opposite order.
  - We are using Unicode characters for the squares and all four types of pieces. You may need to be careful about copying/pasting to avoid including
  any invisible characters added by a browser. In some editors/terminals the letters at the bottom should line up with the columns of the board. This
  depends on how these Unicode characters are rendered.
  - If you use "dark mode" in your editor and/or terminal then the black/white will probably be flipped when you view them. That's fine as long as you
  are using the correct characters in the correct places.
```
1 ⚈ ◼ ⚈ ◼ ⚈ ◼ ⚈ ◼
2 ◼ ⚈ ◼ ⚈ ◼ ⚈ ◼ ⚈
3 ⚈ ◼ ⚈ ◼ ⚈ ◼ ⚈ ◼
4 ◼ ◻ ◼ ◻ ◼ ◻ ◼ ◻
5 ◻ ◼ ◻ ◼ ◻ ◼ ◻ ◼
6 ◼ ⚆ ◼ ⚆ ◼ ⚆ ◼ ⚆
7 ⚆ ◼ ⚆ ◼ ⚆ ◼ ⚆ ◼
8 ◼ ⚆ ◼ ⚆ ◼ ⚆ ◼ ⚆
  a b c d e f g h
```
- **45 points**. Enable two human players (or one playing both sides) to play the game via command line inputs. A player is prompted to select a piece
using the board coordinates. a8 represents the bottom left corner of a standard board. h1 is the top right corner. Some code is provided to help you
convert this into matrix coordinates, such that a8->(7, 0). Once a piece is chosen, your program will calculate and display all the available moves as
a menu.  After the move is completed, the turn passes to the next player and this process repeats until one player has lost all their pieces. See example
input/outputs at the end of this document.
- **15 points**. At the start of a turn, check if the game has ended in a victory or draw. If the current player has no pieces, then the other player wins.
If that player still has pieces, but none of them are able to move, then the game ends in a draw. This involves enumerating all possible moves for the
current player, which will also help in the next part. If 50 turns have past without any captures then the game ends in a draw. You can store a counter
for this along with the current game state.
- **20 points**. Write two types of basic computer opponents to play against. A Random computer player will randomly choose a play from the set of allowed
moves. A slightly more sophisticated Greedy computer player will take the available move that captures the most pieces (break ties with random selection).
Two bots should be able to play against each other, in which case it will run through all the turns without prompting for additional input. To make your
programs easier to test and grade, whenever you set up these players, use a Random object where you pass in a seed loaded from a file called seed.txt.
- **20 points**. Enable undo/redo functionality. When enabled with the history command line argument, the game should give the options undo, redo, or next
before every turn. Undo should roll back to the previous game state.  Redo reverses undos.  Undo does nothing if at turn 1 and redo does nothing if it is
already the latest turn. After using undo, taking any new turn should invalidate any turns that could have been redone. To continue taking turns as usual,
the user should enter next.
- **15 points**. Create a UML diagram for your program demonstrating the relationships between the classes you created.
- **15 points**. Submit a brief write-up (upper limit of 500 words) describing how you made use of design patterns we talked about in class, and how your
design will enable you to extend your code to work for other variants of Checkers/Chess on the next assignment. I expect you will be able to work in at
least 4 distinct design patterns easily (and maybe some more than once), but you're welcome to include more as long as they are appropriate to the task.
Iterator counts, but only if you have created your own custom iterator that does something more than just stepping through a list.
 

## Running your code
Your code should take in arguments from the command line to configure the types of players and whether history (undo/redo) should be enabled or not.
Note that you will want history off when running two computers against each other so that you don't have to type next every turn. Up to three arguments
may be passed in to `main.py` from the command line. `argv[1]` is player1, `argv[2]` is player2, and `argv[3]` is history. This means that you cannot give
an argument without supplying the ones before it. The arguments that are omitted from the end will have the default values.

The defaults for each are...
`player1 = human`
`player2 = human`
`history = off`

Therefore `python3 main.py` is equivalent to `python3 main.py human human`

Other examples...
`python3 main.py greedy random`
`python3 main.py random random`
`python3 main.py human random on`

## Guidance
1. There is almost no code structure predefined for this assignment because this is an opportunity to practice design techniques. If you find yourself
stuck getting started then please come to office hours to talk through the design process.
2. Your main file should take in the command line args, then use them to set up a manager object that will drive the core game loop.
3. Since the next homework will ask you to extend this code to play other games on a checker board, you want to make your code general and re-usable.
Think about what parts are specific to the rules of the game and keep those encapsulated. The rest can act like it is any 2-player game played in turns
with pieces on a checkered board (that's an awful lot to have in common as far as games go).
4. I recommend working through the requirements above in order, since they build on one another.
5. Multiple-jumping is the trickiest part of this assignment so think carefully about how you want to implement it. If it seems simple at first, remember
that Kings make it more difficult as you need to make sure you don't re-jump the same piece later on in a cycle of jumps. Consider how multiple-jumps will
interact with other parts of your application as well. For example, is it treated like a single move, or multiple within one turn? How would this decision
impact your computer players or undo functionality?
6. Keep the undo/redo requirement in mind when you start laying out your classes/objects. This task is made easier with a clean object-oriented design.
Depending on how you choose to implement undo/redo, you may find it useful to look into `copy` and `deepcopy`. There are two design patterns that can make
this part fairly straightforward. We will see the first one in lectures soon.
7. Having two computer players play each other repeatedly may help you catch obscure bugs.

## Testing
You are strongly encouraged to write unittests for your code. Even some simple test cases written early on (setting up the board, printing it out) will be
helpful as you go. However, we will not specifically check your tests in this assignment.

## Submissions
Submit your project to gradescope with whatever files are necessary to run `main.py` (including `seed.txt`). In the same submission, include your write-up
and UML diagram in PDF format. Some public test cases will be added to Gradescope soon to give you some sanity checks particularly for formatting.
You can expect blackbox testing that checks whether the interactions work properly, and sets up specific scenarios in the game to check that rules are
enforced correctly.

## Example input/outputs
```
$ python main.py human random
1 ⚈ ◼ ⚈ ◼ ⚈ ◼ ⚈ ◼ 
2 ◼ ⚈ ◼ ⚈ ◼ ⚈ ◼ ⚈ 
3 ⚈ ◼ ⚈ ◼ ⚈ ◼ ⚈ ◼ 
4 ◼ ◻ ◼ ◻ ◼ ◻ ◼ ◻ 
5 ◻ ◼ ◻ ◼ ◻ ◼ ◻ ◼ 
6 ◼ ⚆ ◼ ⚆ ◼ ⚆ ◼ ⚆ 
7 ⚆ ◼ ⚆ ◼ ⚆ ◼ ⚆ ◼ 
8 ◼ ⚆ ◼ ⚆ ◼ ⚆ ◼ ⚆ 
  a b c d e f g h
Turn: 1, white
Select a piece to move
d6
0: basic move: d6->c5
1: basic move: d6->e5
Select a move by entering the corresponding index
1
1 ⚈ ◼ ⚈ ◼ ⚈ ◼ ⚈ ◼ 
2 ◼ ⚈ ◼ ⚈ ◼ ⚈ ◼ ⚈ 
3 ⚈ ◼ ⚈ ◼ ⚈ ◼ ⚈ ◼ 
4 ◼ ◻ ◼ ◻ ◼ ◻ ◼ ◻ 
5 ◻ ◼ ◻ ◼ ⚆ ◼ ◻ ◼ 
6 ◼ ⚆ ◼ ◻ ◼ ⚆ ◼ ⚆ 
7 ⚆ ◼ ⚆ ◼ ⚆ ◼ ⚆ ◼ 
8 ◼ ⚆ ◼ ⚆ ◼ ⚆ ◼ ⚆ 
  a b c d e f g h
Turn: 2, black
1 ⚈ ◼ ⚈ ◼ ⚈ ◼ ⚈ ◼ 
2 ◼ ⚈ ◼ ⚈ ◼ ⚈ ◼ ⚈ 
3 ⚈ ◼ ◻ ◼ ⚈ ◼ ⚈ ◼ 
4 ◼ ◻ ◼ ⚈ ◼ ◻ ◼ ◻ 
5 ◻ ◼ ◻ ◼ ⚆ ◼ ◻ ◼ 
6 ◼ ⚆ ◼ ◻ ◼ ⚆ ◼ ⚆ 
7 ⚆ ◼ ⚆ ◼ ⚆ ◼ ⚆ ◼ 
8 ◼ ⚆ ◼ ⚆ ◼ ⚆ ◼ ⚆ 
  a b c d e f g h
Turn: 3, white
Select a piece to move
h6
That piece cannot move
Select a piece to move
e5
0: jump move: e5->c3, capturing [d4]
Select a move by entering the corresponding index
0
1 ⚈ ◼ ⚈ ◼ ⚈ ◼ ⚈ ◼ 
2 ◼ ⚈ ◼ ⚈ ◼ ⚈ ◼ ⚈ 
3 ⚈ ◼ ⚆ ◼ ⚈ ◼ ⚈ ◼ 
4 ◼ ◻ ◼ ◻ ◼ ◻ ◼ ◻ 
5 ◻ ◼ ◻ ◼ ◻ ◼ ◻ ◼ 
6 ◼ ⚆ ◼ ◻ ◼ ⚆ ◼ ⚆ 
7 ⚆ ◼ ⚆ ◼ ⚆ ◼ ⚆ ◼ 
8 ◼ ⚆ ◼ ⚆ ◼ ⚆ ◼ ⚆ 
  a b c d e f g h
Turn: 4, black
1 ⚈ ◼ ⚈ ◼ ⚈ ◼ ⚈ ◼ 
2 ◼ ⚈ ◼ ◻ ◼ ⚈ ◼ ⚈ 
3 ⚈ ◼ ◻ ◼ ⚈ ◼ ⚈ ◼ 
4 ◼ ⚈ ◼ ◻ ◼ ◻ ◼ ◻ 
5 ◻ ◼ ◻ ◼ ◻ ◼ ◻ ◼ 
6 ◼ ⚆ ◼ ◻ ◼ ⚆ ◼ ⚆ 
7 ⚆ ◼ ⚆ ◼ ⚆ ◼ ⚆ ◼ 
8 ◼ ⚆ ◼ ⚆ ◼ ⚆ ◼ ⚆ 
  a b c d e f g h
Turn: 5, white
Select a piece to move
...
```

Selecting invalid pieces

```
$ python main.py human random
1 ⚈ ◼ ⚈ ◼ ⚈ ◼ ⚈ ◼ 
2 ◼ ⚈ ◼ ⚈ ◼ ⚈ ◼ ⚈ 
3 ⚈ ◼ ⚈ ◼ ⚈ ◼ ⚈ ◼ 
4 ◼ ◻ ◼ ◻ ◼ ◻ ◼ ◻ 
5 ◻ ◼ ◻ ◼ ◻ ◼ ◻ ◼ 
6 ◼ ⚆ ◼ ⚆ ◼ ⚆ ◼ ⚆ 
7 ⚆ ◼ ⚆ ◼ ⚆ ◼ ⚆ ◼ 
8 ◼ ⚆ ◼ ⚆ ◼ ⚆ ◼ ⚆ 
  a b c d e f g h
Turn: 1, white
Select a piece to move
b8
That piece cannot move
Select a piece to move
c6
No piece at that location
Select a piece to move
a3
That is not your piece
Select a piece to move
h6
0: basic move: h6->g5
Select a move by entering the corresponding index
0
1 ⚈ ◼ ⚈ ◼ ⚈ ◼ ⚈ ◼ 
2 ◼ ⚈ ◼ ⚈ ◼ ⚈ ◼ ⚈ 
3 ⚈ ◼ ⚈ ◼ ⚈ ◼ ⚈ ◼ 
4 ◼ ◻ ◼ ◻ ◼ ◻ ◼ ◻ 
5 ◻ ◼ ◻ ◼ ◻ ◼ ⚆ ◼ 
6 ◼ ⚆ ◼ ⚆ ◼ ⚆ ◼ ◻ 
7 ⚆ ◼ ⚆ ◼ ⚆ ◼ ⚆ ◼ 
8 ◼ ⚆ ◼ ⚆ ◼ ⚆ ◼ ⚆ 
  a b c d e f g h
Turn: 2, black
1 ⚈ ◼ ⚈ ◼ ⚈ ◼ ⚈ ◼ 
2 ◼ ⚈ ◼ ⚈ ◼ ⚈ ◼ ⚈ 
3 ◻ ◼ ⚈ ◼ ⚈ ◼ ⚈ ◼ 
4 ◼ ⚈ ◼ ◻ ◼ ◻ ◼ ◻ 
5 ◻ ◼ ◻ ◼ ◻ ◼ ⚆ ◼ 
6 ◼ ⚆ ◼ ⚆ ◼ ⚆ ◼ ◻ 
7 ⚆ ◼ ⚆ ◼ ⚆ ◼ ⚆ ◼ 
8 ◼ ⚆ ◼ ⚆ ◼ ⚆ ◼ ⚆ 
  a b c d e f g h
Turn: 3, white
Select a piece to move
...
```

Victory example

```
$ python main.py simple random
...
1 ◻ ◼ ◻ ◼ ◻ ◼ ⚇ ◼ 
2 ◼ ◻ ◼ ◻ ◼ ⚉ ◼ ◻ 
3 ◻ ◼ ◻ ◼ ◻ ◼ ◻ ◼ 
4 ◼ ◻ ◼ ◻ ◼ ◻ ◼ ◻ 
5 ◻ ◼ ◻ ◼ ◻ ◼ ◻ ◼ 
6 ◼ ◻ ◼ ◻ ◼ ⚆ ◼ ⚆ 
7 ◻ ◼ ◻ ◼ ◻ ◼ ◻ ◼ 
8 ◼ ◻ ◼ ◻ ◼ ◻ ◼ ◻ 
  a b c d e f g h
Turn: 191, white
1 ◻ ◼ ◻ ◼ ◻ ◼ ◻ ◼ 
2 ◼ ◻ ◼ ◻ ◼ ◻ ◼ ◻ 
3 ◻ ◼ ◻ ◼ ⚇ ◼ ◻ ◼ 
4 ◼ ◻ ◼ ◻ ◼ ◻ ◼ ◻ 
5 ◻ ◼ ◻ ◼ ◻ ◼ ◻ ◼ 
6 ◼ ◻ ◼ ◻ ◼ ⚆ ◼ ⚆ 
7 ◻ ◼ ◻ ◼ ◻ ◼ ◻ ◼ 
8 ◼ ◻ ◼ ◻ ◼ ◻ ◼ ◻ 
  a b c d e f g h
Turn: 192, black
white has won
```

Example of a double jump and king promotion

```
...
1 ⚈ ◼ ⚈ ◼ ◻ ◼ ⚈ ◼ 
2 ◼ ⚈ ◼ ⚈ ◼ ⚈ ◼ ⚈ 
3 ⚈ ◼ ◻ ◼ ⚈ ◼ ⚈ ◼ 
4 ◼ ◻ ◼ ⚈ ◼ ◻ ◼ ⚈ 
5 ⚆ ◼ ⚆ ◼ ◻ ◼ ⚆ ◼ 
6 ◼ ◻ ◼ ⚆ ◼ ◻ ◼ ⚆ 
7 ⚆ ◼ ⚆ ◼ ⚆ ◼ ⚆ ◼ 
8 ◼ ⚆ ◼ ◻ ◼ ⚆ ◼ ⚆ 
  a b c d e f g h
Turn: 10, black
Select a piece to move
d4
0: jump move: d4->d8, capturing [c5, c7]
Select a move by entering the corresponding index
0
1 ⚈ ◼ ⚈ ◼ ◻ ◼ ⚈ ◼ 
2 ◼ ⚈ ◼ ⚈ ◼ ⚈ ◼ ⚈ 
3 ⚈ ◼ ◻ ◼ ⚈ ◼ ⚈ ◼ 
4 ◼ ◻ ◼ ◻ ◼ ◻ ◼ ⚈ 
5 ⚆ ◼ ◻ ◼ ◻ ◼ ⚆ ◼ 
6 ◼ ◻ ◼ ⚆ ◼ ◻ ◼ ⚆ 
7 ⚆ ◼ ◻ ◼ ⚆ ◼ ⚆ ◼ 
8 ◼ ⚆ ◼ ⚉ ◼ ⚆ ◼ ⚆ 
  a b c d e f g h
Turn: 11, white
Select a piece to move
...
```

Example of a draw

```
...
1 ◻ ◼ ◻ ◼ ◻ ◼ ◻ ◼ 
2 ◼ ◻ ◼ ◻ ◼ ◻ ◼ ⚈ 
3 ◻ ◼ ◻ ◼ ◻ ◼ ⚇ ◼ 
4 ◼ ◻ ◼ ◻ ◼ ◻ ◼ ◻ 
5 ◻ ◼ ◻ ◼ ⚈ ◼ ◻ ◼ 
6 ◼ ⚈ ◼ ◻ ◼ ⚈ ◼ ◻ 
7 ◻ ◼ ◻ ◼ ⚉ ◼ ⚈ ◼ 
8 ◼ ◻ ◼ ◻ ◼ ◻ ◼ ⚆ 
  a b c d e f g h
Turn: 56, black
1 ◻ ◼ ◻ ◼ ◻ ◼ ◻ ◼ 
2 ◼ ◻ ◼ ◻ ◼ ◻ ◼ ◻ 
3 ◻ ◼ ◻ ◼ ◻ ◼ ◻ ◼ 
4 ◼ ◻ ◼ ◻ ◼ ⚈ ◼ ◻ 
5 ◻ ◼ ◻ ◼ ⚈ ◼ ◻ ◼ 
6 ◼ ⚈ ◼ ◻ ◼ ⚈ ◼ ◻ 
7 ◻ ◼ ◻ ◼ ⚉ ◼ ⚈ ◼ 
8 ◼ ◻ ◼ ◻ ◼ ◻ ◼ ⚆ 
  a b c d e f g h
Turn: 57, white
draw
```

Undo/redo example

```
$ python main.py human random on
1 ⚈ ◼ ⚈ ◼ ⚈ ◼ ⚈ ◼ 
2 ◼ ⚈ ◼ ⚈ ◼ ⚈ ◼ ⚈ 
3 ⚈ ◼ ⚈ ◼ ⚈ ◼ ⚈ ◼ 
4 ◼ ◻ ◼ ◻ ◼ ◻ ◼ ◻ 
5 ◻ ◼ ◻ ◼ ◻ ◼ ◻ ◼ 
6 ◼ ⚆ ◼ ⚆ ◼ ⚆ ◼ ⚆ 
7 ⚆ ◼ ⚆ ◼ ⚆ ◼ ⚆ ◼ 
8 ◼ ⚆ ◼ ⚆ ◼ ⚆ ◼ ⚆ 
  a b c d e f g h
Turn: 1, white
undo, redo, or next
next
Select a piece to move
d6
0: basic move: d6->c5
1: basic move: d6->e5
Select a move by entering the corresponding index
0
1 ⚈ ◼ ⚈ ◼ ⚈ ◼ ⚈ ◼ 
2 ◼ ⚈ ◼ ⚈ ◼ ⚈ ◼ ⚈ 
3 ⚈ ◼ ⚈ ◼ ⚈ ◼ ⚈ ◼ 
4 ◼ ◻ ◼ ◻ ◼ ◻ ◼ ◻ 
5 ◻ ◼ ◻ ◼ ⚆ ◼ ◻ ◼ 
6 ◼ ⚆ ◼ ◻ ◼ ⚆ ◼ ⚆ 
7 ⚆ ◼ ⚆ ◼ ⚆ ◼ ⚆ ◼ 
8 ◼ ⚆ ◼ ⚆ ◼ ⚆ ◼ ⚆ 
  a b c d e f g h
Turn: 2, black
undo, redo, or next
next
1 ⚈ ◼ ⚈ ◼ ⚈ ◼ ⚈ ◼ 
2 ◼ ⚈ ◼ ⚈ ◼ ⚈ ◼ ⚈ 
3 ◻ ◼ ⚈ ◼ ⚈ ◼ ⚈ ◼ 
4 ◼ ⚈ ◼ ◻ ◼ ◻ ◼ ◻ 
5 ◻ ◼ ◻ ◼ ⚆ ◼ ◻ ◼ 
6 ◼ ⚆ ◼ ◻ ◼ ⚆ ◼ ⚆ 
7 ⚆ ◼ ⚆ ◼ ⚆ ◼ ⚆ ◼ 
8 ◼ ⚆ ◼ ⚆ ◼ ⚆ ◼ ⚆ 
  a b c d e f g h
Turn: 3, white
undo, redo, or next
next
Select a piece to move
h6
0: basic move: h6->g5
Select a move by entering the corresponding index
0
1 ⚈ ◼ ⚈ ◼ ⚈ ◼ ⚈ ◼ 
2 ◼ ⚈ ◼ ⚈ ◼ ⚈ ◼ ⚈ 
3 ◻ ◼ ⚈ ◼ ⚈ ◼ ⚈ ◼ 
4 ◼ ⚈ ◼ ◻ ◼ ◻ ◼ ◻ 
5 ◻ ◼ ◻ ◼ ⚆ ◼ ⚆ ◼ 
6 ◼ ⚆ ◼ ◻ ◼ ⚆ ◼ ◻ 
7 ⚆ ◼ ⚆ ◼ ⚆ ◼ ⚆ ◼ 
8 ◼ ⚆ ◼ ⚆ ◼ ⚆ ◼ ⚆ 
  a b c d e f g h
Turn: 4, black
undo, redo, or next
next
1 ⚈ ◼ ⚈ ◼ ⚈ ◼ ⚈ ◼ 
2 ◼ ⚈ ◼ ⚈ ◼ ⚈ ◼ ⚈ 
3 ◻ ◼ ⚈ ◼ ⚈ ◼ ◻ ◼ 
4 ◼ ⚈ ◼ ◻ ◼ ⚈ ◼ ◻ 
5 ◻ ◼ ◻ ◼ ⚆ ◼ ⚆ ◼ 
6 ◼ ⚆ ◼ ◻ ◼ ⚆ ◼ ◻ 
7 ⚆ ◼ ⚆ ◼ ⚆ ◼ ⚆ ◼ 
8 ◼ ⚆ ◼ ⚆ ◼ ⚆ ◼ ⚆ 
  a b c d e f g h
Turn: 5, white
undo, redo, or next
next
Select a piece to move
e5
0: jump move: e5->g3, capturing [f4]
Select a move by entering the corresponding index
0
1 ⚈ ◼ ⚈ ◼ ⚈ ◼ ⚈ ◼ 
2 ◼ ⚈ ◼ ⚈ ◼ ⚈ ◼ ⚈ 
3 ◻ ◼ ⚈ ◼ ⚈ ◼ ⚆ ◼ 
4 ◼ ⚈ ◼ ◻ ◼ ◻ ◼ ◻ 
5 ◻ ◼ ◻ ◼ ◻ ◼ ⚆ ◼ 
6 ◼ ⚆ ◼ ◻ ◼ ⚆ ◼ ◻ 
7 ⚆ ◼ ⚆ ◼ ⚆ ◼ ⚆ ◼ 
8 ◼ ⚆ ◼ ⚆ ◼ ⚆ ◼ ⚆ 
  a b c d e f g h
Turn: 6, black
undo, redo, or next
undo
1 ⚈ ◼ ⚈ ◼ ⚈ ◼ ⚈ ◼ 
2 ◼ ⚈ ◼ ⚈ ◼ ⚈ ◼ ⚈ 
3 ◻ ◼ ⚈ ◼ ⚈ ◼ ◻ ◼ 
4 ◼ ⚈ ◼ ◻ ◼ ⚈ ◼ ◻ 
5 ◻ ◼ ◻ ◼ ⚆ ◼ ⚆ ◼ 
6 ◼ ⚆ ◼ ◻ ◼ ⚆ ◼ ◻ 
7 ⚆ ◼ ⚆ ◼ ⚆ ◼ ⚆ ◼ 
8 ◼ ⚆ ◼ ⚆ ◼ ⚆ ◼ ⚆ 
  a b c d e f g h
Turn: 5, white
undo, redo, or next
undo
1 ⚈ ◼ ⚈ ◼ ⚈ ◼ ⚈ ◼ 
2 ◼ ⚈ ◼ ⚈ ◼ ⚈ ◼ ⚈ 
3 ◻ ◼ ⚈ ◼ ⚈ ◼ ⚈ ◼ 
4 ◼ ⚈ ◼ ◻ ◼ ◻ ◼ ◻ 
5 ◻ ◼ ◻ ◼ ⚆ ◼ ⚆ ◼ 
6 ◼ ⚆ ◼ ◻ ◼ ⚆ ◼ ◻ 
7 ⚆ ◼ ⚆ ◼ ⚆ ◼ ⚆ ◼ 
8 ◼ ⚆ ◼ ⚆ ◼ ⚆ ◼ ⚆ 
  a b c d e f g h
Turn: 4, black
undo, redo, or next
undo
1 ⚈ ◼ ⚈ ◼ ⚈ ◼ ⚈ ◼ 
2 ◼ ⚈ ◼ ⚈ ◼ ⚈ ◼ ⚈ 
3 ◻ ◼ ⚈ ◼ ⚈ ◼ ⚈ ◼ 
4 ◼ ⚈ ◼ ◻ ◼ ◻ ◼ ◻ 
5 ◻ ◼ ◻ ◼ ⚆ ◼ ◻ ◼ 
6 ◼ ⚆ ◼ ◻ ◼ ⚆ ◼ ⚆ 
7 ⚆ ◼ ⚆ ◼ ⚆ ◼ ⚆ ◼ 
8 ◼ ⚆ ◼ ⚆ ◼ ⚆ ◼ ⚆ 
a b c d e f g h
Turn: 3, white
undo, redo, or next
redo
1 ⚈ ◼ ⚈ ◼ ⚈ ◼ ⚈ ◼ 
2 ◼ ⚈ ◼ ⚈ ◼ ⚈ ◼ ⚈ 
3 ◻ ◼ ⚈ ◼ ⚈ ◼ ⚈ ◼ 
4 ◼ ⚈ ◼ ◻ ◼ ◻ ◼ ◻ 
5 ◻ ◼ ◻ ◼ ⚆ ◼ ⚆ ◼ 
6 ◼ ⚆ ◼ ◻ ◼ ⚆ ◼ ◻ 
7 ⚆ ◼ ⚆ ◼ ⚆ ◼ ⚆ ◼ 
8 ◼ ⚆ ◼ ⚆ ◼ ⚆ ◼ ⚆ 
a b c d e f g h
Turn: 4, black
undo, redo, or next
redo
1 ⚈ ◼ ⚈ ◼ ⚈ ◼ ⚈ ◼ 
2 ◼ ⚈ ◼ ⚈ ◼ ⚈ ◼ ⚈ 
3 ◻ ◼ ⚈ ◼ ⚈ ◼ ◻ ◼ 
4 ◼ ⚈ ◼ ◻ ◼ ⚈ ◼ ◻ 
5 ◻ ◼ ◻ ◼ ⚆ ◼ ⚆ ◼ 
6 ◼ ⚆ ◼ ◻ ◼ ⚆ ◼ ◻ 
7 ⚆ ◼ ⚆ ◼ ⚆ ◼ ⚆ ◼ 
8 ◼ ⚆ ◼ ⚆ ◼ ⚆ ◼ ⚆ 
a b c d e f g h
Turn: 5, white
undo, redo, or next
undo
1 ⚈ ◼ ⚈ ◼ ⚈ ◼ ⚈ ◼ 
2 ◼ ⚈ ◼ ⚈ ◼ ⚈ ◼ ⚈ 
3 ◻ ◼ ⚈ ◼ ⚈ ◼ ⚈ ◼ 
4 ◼ ⚈ ◼ ◻ ◼ ◻ ◼ ◻ 
5 ◻ ◼ ◻ ◼ ⚆ ◼ ⚆ ◼ 
6 ◼ ⚆ ◼ ◻ ◼ ⚆ ◼ ◻ 
7 ⚆ ◼ ⚆ ◼ ⚆ ◼ ⚆ ◼ 
8 ◼ ⚆ ◼ ⚆ ◼ ⚆ ◼ ⚆ 
a b c d e f g h
Turn: 4, black
undo, redo, or next
next
1 ⚈ ◼ ⚈ ◼ ⚈ ◼ ⚈ ◼ 
2 ◼ ⚈ ◼ ⚈ ◼ ⚈ ◼ ⚈ 
3 ◻ ◼ ⚈ ◼ ⚈ ◼ ◻ ◼ 
4 ◼ ⚈ ◼ ◻ ◼ ⚈ ◼ ◻ 
5 ◻ ◼ ◻ ◼ ⚆ ◼ ⚆ ◼ 
6 ◼ ⚆ ◼ ◻ ◼ ⚆ ◼ ◻ 
7 ⚆ ◼ ⚆ ◼ ⚆ ◼ ⚆ ◼ 
8 ◼ ⚆ ◼ ⚆ ◼ ⚆ ◼ ⚆ 
a b c d e f g h
Turn: 5, white
undo, redo, or next
redo
1 ⚈ ◼ ⚈ ◼ ⚈ ◼ ⚈ ◼ 
2 ◼ ⚈ ◼ ⚈ ◼ ⚈ ◼ ⚈ 
3 ◻ ◼ ⚈ ◼ ⚈ ◼ ◻ ◼ 
4 ◼ ⚈ ◼ ◻ ◼ ⚈ ◼ ◻ 
5 ◻ ◼ ◻ ◼ ⚆ ◼ ⚆ ◼ 
6 ◼ ⚆ ◼ ◻ ◼ ⚆ ◼ ◻ 
7 ⚆ ◼ ⚆ ◼ ⚆ ◼ ⚆ ◼ 
8 ◼ ⚆ ◼ ⚆ ◼ ⚆ ◼ ⚆ 
a b c d e f g h
Turn: 5, white
undo, redo, or next
next
Select a piece to move
e5
0: jump move: e5->g3, capturing [f4]
Select a move by entering the corresponding index
0
1 ⚈ ◼ ⚈ ◼ ⚈ ◼ ⚈ ◼ 
2 ◼ ⚈ ◼ ⚈ ◼ ⚈ ◼ ⚈ 
3 ◻ ◼ ⚈ ◼ ⚈ ◼ ⚆ ◼ 
4 ◼ ⚈ ◼ ◻ ◼ ◻ ◼ ◻ 
5 ◻ ◼ ◻ ◼ ◻ ◼ ⚆ ◼ 
6 ◼ ⚆ ◼ ◻ ◼ ⚆ ◼ ◻ 
7 ⚆ ◼ ⚆ ◼ ⚆ ◼ ⚆ ◼ 
8 ◼ ⚆ ◼ ⚆ ◼ ⚆ ◼ ⚆ 
a b c d e f g h
Turn: 6, black
undo, redo, or next
next
1 ⚈ ◼ ⚈ ◼ ⚈ ◼ ⚈ ◼ 
2 ◼ ⚈ ◼ ⚈ ◼ ◻ ◼ ⚈ 
3 ◻ ◼ ⚈ ◼ ⚈ ◼ ◻ ◼ 
4 ◼ ⚈ ◼ ◻ ◼ ◻ ◼ ⚈ 
5 ◻ ◼ ◻ ◼ ◻ ◼ ⚆ ◼ 
6 ◼ ⚆ ◼ ◻ ◼ ⚆ ◼ ◻ 
7 ⚆ ◼ ⚆ ◼ ⚆ ◼ ⚆ ◼ 
8 ◼ ⚆ ◼ ⚆ ◼ ⚆ ◼ ⚆ 
a b c d e f g h
Turn: 6, black
undo, redo, or next
...
```
