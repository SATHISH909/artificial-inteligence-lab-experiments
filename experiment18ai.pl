% Define the database of names and dates of birth
db(Name, DOB).

% Sample entries
db('Alice', '1990-05-15').
db('Bob', '1985-10-20').
db('Charlie', '1992-03-30').
db('Diana', '1988-07-25').

% Query to find DOB by Name
find_dob(Name, DOB) :- db(Name, DOB).
