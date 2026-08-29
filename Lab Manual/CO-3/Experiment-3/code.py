parent(john, mary).
parent(john, tom).
parent(mary, sam).
parent(mary, lisa).

male(john).
male(tom).
male(sam).

female(mary).
female(lisa).

father(X,Y) :-
    parent(X,Y), male(X).

mother(X,Y) :-
    parent(X,Y), female(X).

grandparent(X,Y) :-
    parent(X,Z), parent(Z,Y).
