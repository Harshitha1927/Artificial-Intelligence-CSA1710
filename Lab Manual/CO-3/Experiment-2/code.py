bird(parrot).
bird(eagle).
bird(penguin).
bird(ostrich).

can_fly(parrot).
can_fly(eagle).

cannot_fly(penguin).
cannot_fly(ostrich).

fly(Bird) :-
    can_fly(Bird),
    write(Bird), write(' can fly').

fly(Bird) :-
    cannot_fly(Bird),
    write(Bird), write(' cannot fly').
