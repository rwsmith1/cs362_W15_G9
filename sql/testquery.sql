INSERT INTO User (name, password, email) VALUES 
  ('user1', '1234', 'user1@gmail.com'),
  ('user2', '1234', 'user2@gmail.com'),
  ('user3', '1234', 'user13@gmail.com');

INSERT INTO Student (name, email) VALUES 
  ('student1', 'student1@test.com'),
  ('student2', 'student2@test.com'),
  ('student3', 'student3@test.com');

INSERT INTO Message (fkUser,fkStudent,mailbox) VALUES 
  ((SELECT pkUser FROM User WHERE name = 'user1' ),(SELECT pkStudent FROM Student WHERE name = 'student2'),'One ring to rule them all'),
  ((SELECT pkUser FROM User WHERE name = 'user2' ),(SELECT pkStudent FROM Student WHERE name = 'student2'),'One ring to find them'),
  ((SELECT pkUser FROM User WHERE name = 'user3' ),(SELECT pkStudent FROM Student WHERE name = 'student1'),'One Ring to bring them all and in the darkness bind them');

INSERT INTO Appointment (fkUser, fkStudent, time, date, location, canceled) VALUES 
  ((SELECT pkUser FROM User WHERE name = 'user1' ),(SELECT pkStudent FROM Student WHERE name = 'student2'), 132, 2012/12/12, 'online', 0),
  ((SELECT pkUser FROM User WHERE name = 'user2' ),(SELECT pkStudent FROM Student WHERE name = 'student2'), 132, 2012/12/12, 'Kevins House', 0),
  ((SELECT pkUser FROM User WHERE name = 'user3' ),(SELECT pkStudent FROM Student WHERE name = 'student1'), 132, 2012/12/12, 'OSU', 0);
