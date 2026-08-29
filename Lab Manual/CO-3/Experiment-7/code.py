edge(a,b,2).
edge(a,c,4).
edge(b,d,1).
edge(c,d,2).

best_first(Start, Goal) :-
    search([Start], Goal).

search([Goal|_], Goal) :-
    write('Goal Reached').

search([Node|Rest], Goal) :-
    findall(C, edge(Node,C,_), Next),
    append(Rest, Next, Queue),
    search(Queue, Goal).
