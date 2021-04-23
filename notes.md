TODO: spec, UML diagram, then questions about organization of modules/classes and making code general and reusable for other checker-board games like chess; if there’s time, start looking at specifics on data structures and logic


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