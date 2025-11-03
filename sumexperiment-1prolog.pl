% sum_to_n(N, Sum)
% Succeeds if Sum is the sum of all integers from 1 to N.

sum_to_n(1, 1).  % Base case: sum of first 1 number is 1
sum_to_n(N, Sum) :-
    N > 1,
    N1 is N - 1,
    sum_to_n(N1, PartialSum),
    Sum is PartialSum + N.
