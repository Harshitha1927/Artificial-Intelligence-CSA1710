diet(diabetes, 'Low sugar diet').
diet(obesity, 'Low calorie diet').
diet(anemia, 'Iron rich diet').
diet(hypertension, 'Low salt diet').

suggest(Disease) :-
    diet(Disease,D),
    write('Suggested Diet: '), write(D).
