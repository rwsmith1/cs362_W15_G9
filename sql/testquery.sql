INSERT INTO User (name, password, email) VALUES 
  ('user1', '1234', 'user1@gmail.com'),
  ('user2', '1234', 'user2@gmail.com'),
  ('user3', '1234', 'user3@gmail.com');

INSERT INTO Student (name, email) VALUES 
  ('student1', 'student1@test.com'),
  ('student2', 'student2@test.com'),
  ('student3', 'student3@test.com');

INSERT INTO Message (fkUser,fkStudent,mailbox) VALUES 
  ((SELECT pkUser FROM User WHERE name = 'user1' ),(SELECT pkStudent FROM Student WHERE name = 'student2'),'One ring to rule them all'),
  ((SELECT pkUser FROM User WHERE name = 'user2' ),(SELECT pkStudent FROM Student WHERE name = 'student2'),'One ring to find them'),
  ((SELECT pkUser FROM User WHERE name = 'user3' ),(SELECT pkStudent FROM Student WHERE name = 'student1'),'One Ring to bring them all and in the darkness bind them')
  ((SELECT pkUser FROM User WHERE name = 'user1' ),(SELECT pkStudent FROM Student WHERE name = 'student2'),'Val');

INSERT INTO Appointment (fkUser, fkStudent, uId, timeStart, timeEnd, date, location, canceled) VALUES 
  ((SELECT pkUser FROM User WHERE name = 'user1' ),(SELECT pkStudent FROM Student WHERE name = 'student2'), NULL, '08:30:00', '09:30:00', '2015-02-11', 'online', 0),
  ((SELECT pkUser FROM User WHERE name = 'user2' ),(SELECT pkStudent FROM Student WHERE name = 'student2'), NULL, '11:30:00', '12:30:00', '2015-12-16', 'Kevins House', 0),
  ((SELECT pkUser FROM User WHERE name = 'user3' ),(SELECT pkStudent FROM Student WHERE name = 'student1'), NULL, '23:00:00', '24:00:00', '2015-02-14', 'OSU', 0),
  ((SELECT pkUser FROM User WHERE name = 'user1' ),(SELECT pkStudent FROM Student WHERE name = 'student3'), NULL, '05:45:00', '06:45:00', '2015-03-13', 'online', 0),
  ((SELECT pkUser FROM User WHERE name = 'user2' ),(SELECT pkStudent FROM Student WHERE name = 'student1'), NULL, '07:15:00', '08:15:00', '2015-12-12', 'Kevins House', 0),
  ((SELECT pkUser FROM User WHERE name = 'user3' ),(SELECT pkStudent FROM Student WHERE name = 'student3'), NULL, '12:00:00', '13:00:00', '2015-02-14', 'OSU', 0);
