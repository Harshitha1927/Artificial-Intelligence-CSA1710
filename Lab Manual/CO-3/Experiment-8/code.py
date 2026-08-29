symptom(ravi, fever).
symptom(ravi, cough).
symptom(anu, headache).
symptom(anu, fever).

disease(X, flu) :-
    symptom(X, fever),
    symptom(X, cough).

disease(X, migraine) :-
    symptom(X, headache).

diagnose(X) :-
    disease(X,D),
    write('Disease: '), write(D).
