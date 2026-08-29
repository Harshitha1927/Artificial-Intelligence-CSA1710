person(ravi, '10-05-2004').
person(anu, '15-08-2005').
person(kiran, '20-01-2004').

dob(Name, DOB) :-
    person(Name, DOB).
