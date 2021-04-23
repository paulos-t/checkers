## TODO:
1. UML diagram
2. Write-up of design patterns used

## Important things to consider:
- Making code general and reusable for other checker-board games like chess


## Planning the UML Diagram

CheckerBoard
- board_state
- turns

Player
- canJump(): bool
    - if there are multiple options, then the player chooses which piece to jump with

Abstract Base Class: Piece
- state: can be IN_PLAY or CAPTURED
- color
- simple_move method
    - diagonally forward
- jump method
    - needs to know:
        - is diagonally adjacent
        - empty next space

King (inherits from Piece)
- override simple_move and jump so that it can move/jump backwards as well

Peasants
- inKingsRow(): bool