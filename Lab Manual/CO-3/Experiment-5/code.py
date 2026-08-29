at(monkey, floor).
at(banana, ceiling).
at(box, floor).
has(monkey, no).

move :-
    at(monkey, floor),
    at(box, floor),
    write('Monkey pushes box'), nl,
    write('Monkey climbs box'), nl,
    write('Monkey gets banana').
