% -------------------------------
% Knowledge Base
% -------------------------------

% student_teacher_subcode(StudentName, TeacherName, SubjectCode)

student_teacher_subcode('Alice',   'Dr. Smith',   'CS101').
student_teacher_subcode('Bob',     'Prof. Jones', 'CS102').
student_teacher_subcode('Charlie', 'Dr. Smith',   'CS101').
student_teacher_subcode('Diana',   'Dr. Brown',   'CS103').
student_teacher_subcode('Ethan',   'Prof. Jones', 'CS102').
student_teacher_subcode('Fiona',   'Dr. Brown',   'CS103').

% -------------------------------
% Rules
% -------------------------------

% Find the teacher for a given student
find_teacher(Student, Teacher) :-
    student_teacher_subcode(Student, Teacher, _).

% Find all students taught by a given teacher
find_students(Teacher, Student) :-
    student_teacher_subcode(Student, Teacher, _).

% Find subject code for a given student
find_subject(Student, SubjectCode) :-
    student_teacher_subcode(Student, _, SubjectCode).

% Find all students studying a given subject
find_students_by_subject(SubjectCode, Student) :-
    student_teacher_subcode(Student, _, SubjectCode).
