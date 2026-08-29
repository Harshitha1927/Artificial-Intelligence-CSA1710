fact(bird).
fact(has_wings).

can_fly :-
    fact(bird),
    fact(has_wings).

backward :-
    can_fly,
    write('Bird can fly').
