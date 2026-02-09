--------- DDL_CODE----------------------------------
create database University_Course_Registration ;
use  University_Course_Registration;
create table department (
DID INT PRIMARY KEY,
DName VARCHAR(50) NOT NULL UNIQUE
);
create table student (
SID int primary key AUTO_INCREMENT,
SSN int unique ,
level int,
FName VARCHAR(50)NOT NULL ,
MName VARCHAR(50)NOT NULL ,
LName VARCHAR(50)NOT NULL,
phone varchar(11),
Email varchar(200),
DID INT,
FOREIGN KEY (DID) REFERENCES department(DID) ON DELETE SET NULL,
CONSTRAINT chk_student_phone CHECK (phone REGEXP '^01[0-9]{9}$'),
CONSTRAINT chk_level CHECK (level BETWEEN 1 AND 4),
CONSTRAINT chk_student_email CHECK (Email REGEXP '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$')


);
create table course (
CID INT PRIMARY KEY,
CName VARCHAR(50),
C_Hours INT CHECK (C_Hours IN (0,2,3))
);

create table instructor(
IID int primary key,
FName VARCHAR(30) NOT NULL,
LName VARCHAR(30) NOT NULL,
phone varchar(11),
Email varchar(200),
CONSTRAINT chk_instructor_phone CHECK (phone REGEXP '^01[0-9]{9}$'),
CONSTRAINT chk_instructor_email CHECK (Email REGEXP '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$')

);
CREATE table enrollment(
SID INT,
FOREIGN KEY(SID) REFERENCES student(SID)  ON DELETE CASCADE ON UPDATE CASCADE,
CID INT,
FOREIGN KEY( CID) REFERENCES course( CID)  ON DELETE CASCADE ON UPDATE CASCADE,
primary key(SID,CID)
) ;

CREATE table instructor_course(
IID int ,
CID int,
primary key (IID,CID),
foreign key(CID) references course(CID)  ON DELETE CASCADE ON UPDATE CASCADE,
foreign key(IID) references instructor(IID) ON DELETE CASCADE ON UPDATE CASCADE
) ;
CREATE table instructor_dep(
IID int ,
DID int,
primary key (IID,DID),
foreign key(IID) references instructor(IID)  ON DELETE CASCADE ON UPDATE CASCADE,
foreign key(DID) references department(DID)  ON DELETE CASCADE ON UPDATE CASCADE
) ;
CREATE table course_department(
DID int ,
CID int,
primary key (CID,DID),
foreign key(CID) references course(CID)  ON DELETE CASCADE ON UPDATE CASCADE,
foreign key(DID) references department(DID)  ON DELETE CASCADE ON UPDATE CASCADE
) ;
alter table student modify SSN varchar(14);
alter table student add constraint check_SSN_LENGTH check(length(SSN)=14);
---------------- DML_CODE-------------------------------------------
-- 1
INSERT INTO department (DID, DName) VALUES
(1, 'Computer Science'),
(2, 'Information Technology'),
(3, 'Software Engineering'),
(4, 'Data Science'),
(5, 'Cyber Security'),
(6, 'Artificial Intelligence'),
(7, 'Computer Engineering'),
(8, 'Information Systems'),
(9, 'Network Engineering'),
(10, 'Web Development'),
(11, 'Mobile Computing'),
(12, 'Cloud Computing'),
(13, 'Database Systems'),
(14, 'Game Development'),
(15, 'Computer Graphics'),
(16, 'Human Computer Interaction'),
(17, 'Bioinformatics'),
(18, 'Computer Networks'),
(19, 'Digital Marketing'),
(20, 'E-commerce'),
(21, 'Business Informatics'),
(22, 'Health Informatics'),
(23, 'Robotics'),
(24, 'Internet of Things'),
(25, 'Quantum Computing'),
(26, 'Computer Architecture'),
(27, 'Operating Systems'),
(28, 'Compiler Design'),
(29, 'Computer Vision'),
(30, 'Natural Language Processing');
-- 2
INSERT INTO student (SSN, level, FName, MName, LName, phone, Email, DID) VALUES
('123-45-6789-01', 1, 'Ahmed', 'Mohamed', 'Ali', '01012345678', 'ahmed.ali@university.edu', 1),
('234-56-7890-12', 2, 'Mohamed', 'Mahmoud', 'Hassan', '01023456789', 'mohamed.hassan@university.edu', 2),
('345-67-8901-23', 3, 'Mahmoud', 'Omar', 'Ibrahim', '01034567890', 'mahmoud.ibrahim@university.edu', 3),
('456-78-9012-34', 4, 'Omar', 'Khaled', 'Saeed', '01045678901', 'omar.saeed@university.edu', 4),
('567-89-0123-45', 1, 'Khaled', 'Amr', 'Farouk', '01056789012', 'khaled.farouk@university.edu', 5),
('678-90-1234-56', 2, 'Amr', 'Wael', 'Nasser', '01067890123', 'amr.nasser@university.edu', 6),
('789-01-2345-67', 3, 'Wael', 'Hossam', 'Kamal', '01078901234', 'wael.kamal@university.edu', 7),
('890-12-3456-78', 4, 'Hossam', 'Tarek', 'Rashid', '01089012345', 'hossam.rashid@university.edu', 8),
('901-23-4567-89', 1, 'Tarek', 'Youssef', 'Samir', '01090123456', 'tarek.samir@university.edu', 9),
('012-34-5678-90', 2, 'Youssef', 'Bassem', 'Adel', '01001234567', 'youssef.adel@university.edu', 10),
('111-22-3333-44', 3, 'Bassem', 'Karim', 'Fathi', '01011122233', 'bassem.fathi@university.edu', 11),
('222-33-4444-55', 4, 'Karim', 'Sherif', 'Gamal', '01022233344', 'karim.gamal@university.edu', 12),
('333-44-5555-66', 1, 'Sherif', 'Nader', 'Hany', '01033344455', 'sherif.hany@university.edu', 13),
('444-55-6666-77', 2, 'Nader', 'Raafat', 'Ismail', '01044455566', 'nader.ismail@university.edu', 14),
('555-66-7777-88', 3, 'Raafat', 'Samih', 'Jalal', '01055566677', 'raafat.jalal@university.edu', 15),
('666-77-8888-99', 4, 'Samih', 'Medhat', 'Kamil', '01066677788', 'samih.kamil@university.edu', 16),
('777-88-9999-00', 1, 'Medhat', 'Atef', 'Lotfy', '01077788899', 'medhat.lotfy@university.edu', 17),
('888-99-0000-11', 2, 'Atef', 'Fares', 'Mounir', '01088899900', 'atef.mounir@university.edu', 18),
('999-00-1111-22', 3, 'Fares', 'Hisham', 'Naguib', '01099900011', 'fares.naguib@university.edu', 19),
('000-11-2222-33', 4, 'Hisham', 'Zaki', 'Osman', '01000011122', 'hisham.osman@university.edu', 20),
('111-00-2222-44', 1, 'Zaki', 'Ashraf', 'Pasha', '01011100022', 'zaki.pasha@university.edu', 21),
('222-11-3333-55', 2, 'Ashraf', 'Sobhy', 'Qasim', '01022211133', 'ashraf.qasim@university.edu', 22),
('333-22-4444-66', 3, 'Sobhy', 'Ramzy', 'Raouf', '01033322244', 'sobhy.raouf@university.edu', 23),
('444-33-5555-77', 4, 'Ramzy', 'Said', 'Sabry', '01044433355', 'ramzy.sabry@university.edu', 24),
('555-44-6666-88', 1, 'Said', 'Fekry', 'Tawfik', '01055544466', 'said.tawfik@university.edu', 25),
('666-55-7777-99', 2, 'Fekry', 'Gamil', 'Wael', '01066655577', 'fekry.wael@university.edu', 26),
('777-66-8888-00', 3, 'Gamil', 'Hassan', 'Yasser', '01077766688', 'gamil.yasser@university.edu', 27),
('888-77-9999-11', 4, 'Hassan', 'Ihab', 'Zakaria', '01088877799', 'hassan.zakaria@university.edu', 28),
('999-88-0000-22', 1, 'Ihab', 'Jalal', 'Ashraf', '01099988800', 'ihab.ashraf@university.edu', 29),
('000-99-1111-33', 2, 'Jalal', 'Khalil', 'Bassem', '01000099911', 'jalal.bassem@university.edu', 30);
-- 3
INSERT INTO course (CID, CName, C_Hours) VALUES
(101, 'Programming Fundamentals', 3),
(102, 'Data Structures', 3),
(103, 'Algorithms', 3),
(104, 'Database Systems', 3),
(105, 'Operating Systems', 3),
(106, 'Computer Networks', 3),
(107, 'Software Engineering', 3),
(108, 'Web Development', 3),
(109, 'Mobile App Development', 3),
(110, 'Artificial Intelligence', 3),
(111, 'Machine Learning', 3),
(112, 'Data Mining', 3),
(113, 'Computer Security', 3),
(114, 'Cloud Computing', 3),
(115, 'Big Data Analytics', 3),
(116, 'Computer Graphics', 3),
(117, 'Human Computer Interaction', 3),
(118, 'Natural Language Processing', 3),
(119, 'Computer Vision', 3),
(120, 'Robotics', 3),
(121, 'Internet of Things', 3),
(122, 'Quantum Computing', 2),
(123, 'Ethical Hacking', 2),
(124, 'Digital Forensics', 2),
(125, 'Game Development', 3),
(126, 'Virtual Reality', 2),
(127, 'Augmented Reality', 2),
(128, 'Blockchain Technology', 2),
(129, 'DevOps', 2),
(130, 'UI/UX Design', 2);
-- 4
INSERT INTO instructor (IID, FName, LName, phone, Email) VALUES
(1001, 'Dr. Ahmed', 'Salah', '01010011001', 'ahmed.salah@university.edu'),
(1002, 'Dr. Mohamed', 'Nasser', '01010021002', 'mohamed.nasser@university.edu'),
(1003, 'Dr. Mahmoud', 'Kamel', '01010031003', 'mahmoud.kamel@university.edu'),
(1004, 'Dr. Omar', 'Fouad', '01010041004', 'omar.fouad@university.edu'),
(1005, 'Dr. Khaled', 'Rady', '01010051005', 'khaled.rady@university.edu'),
(1006, 'Dr. Amr', 'Shawky', '01010061006', 'amr.shawky@university.edu'),
(1007, 'Dr. Wael', 'Hatem', '01010071007', 'wael.hatem@university.edu'),
(1008, 'Dr. Hossam', 'Yehia', '01010081008', 'hossam.yehia@university.edu'),
(1009, 'Dr. Tarek', 'Zaki', '01010091009', 'tarek.zaki@university.edu'),
(1010, 'Dr. Youssef', 'Samir', '01010101010', 'youssef.samir@university.edu'),
(1011, 'Dr. Bassem', 'Adel', '01010111011', 'bassem.adel@university.edu'),
(1012, 'Dr. Karim', 'Fathi', '01010121012', 'karim.fathi@university.edu'),
(1013, 'Dr. Sherif', 'Gamal', '01010131013', 'sherif.gamal@university.edu'),
(1014, 'Dr. Nader', 'Hany', '01010141014', 'nader.hany@university.edu'),
(1015, 'Dr. Raafat', 'Ismail', '01010151015', 'raafat.ismail@university.edu'),
(1016, 'Dr. Samih', 'Jalal', '01010161016', 'samih.jalal@university.edu'),
(1017, 'Dr. Medhat', 'Kamil', '01010171017', 'medhat.kamil@university.edu'),
(1018, 'Dr. Atef', 'Lotfy', '01010181018', 'atef.lotfy@university.edu'),
(1019, 'Dr. Fares', 'Mounir', '01010191019', 'fares.mounir@university.edu'),
(1020, 'Dr. Hisham', 'Naguib', '01010201020', 'hisham.naguib@university.edu'),
(1021, 'Dr. Zaki', 'Osman', '01010211021', 'zaki.osman@university.edu'),
(1022, 'Dr. Ashraf', 'Pasha', '01010221022', 'ashraf.pasha@university.edu'),
(1023, 'Dr. Sobhy', 'Qasim', '01010231023', 'sobhy.qasim@university.edu'),
(1024, 'Dr. Ramzy', 'Raouf', '01010241024', 'ramzy.raouf@university.edu'),
(1025, 'Dr. Said', 'Sabry', '01010251025', 'said.sabry@university.edu'),
(1026, 'Dr. Fekry', 'Tawfik', '01010261026', 'fekry.tawfik@university.edu'),
(1027, 'Dr. Gamil', 'Wael', '01010271027', 'gamil.wael@university.edu'),
(1028, 'Dr. Hassan', 'Yasser', '01010281028', 'hassan.yasser@university.edu'),
(1029, 'Dr. Ihab', 'Zakaria', '01010291029', 'ihab.zakaria@university.edu'),
(1030, 'Dr. Jalal', 'Ashraf', '01010301030', 'jalal.ashraf@university.edu');
-- 5
INSERT INTO enrollment (SID, CID) VALUES
(1, 101), (1, 102), (2, 103), (2, 104), (3, 105), (3, 106),
(4, 107), (4, 108), (5, 109), (5, 110), (6, 111), (6, 112),
(7, 113), (7, 114), (8, 115), (8, 116), (9, 117), (9, 118),
(10, 119), (10, 120), (11, 121), (11, 122), (12, 123), (12, 124),
(13, 125), (13, 126), (14, 127), (14, 128), (15, 129), (15, 130);
-- 6
INSERT INTO instructor_course (IID, CID) VALUES
(1001, 101), (1002, 102), (1003, 103), (1004, 104), (1005, 105),
(1006, 106), (1007, 107), (1008, 108), (1009, 109), (1010, 110),
(1011, 111), (1012, 112), (1013, 113), (1014, 114), (1015, 115),
(1016, 116), (1017, 117), (1018, 118), (1019, 119), (1020, 120),
(1021, 121), (1022, 122), (1023, 123), (1024, 124), (1025, 125),
(1026, 126), (1027, 127), (1028, 128), (1029, 129), (1030, 130);
-- 7
INSERT INTO instructor_dep (IID, DID) VALUES
(1001, 1), (1002, 2), (1003, 3), (1004, 4), (1005, 5),
(1006, 6), (1007, 7), (1008, 8), (1009, 9), (1010, 10),
(1011, 11), (1012, 12), (1013, 13), (1014, 14), (1015, 15),
(1016, 16), (1017, 17), (1018, 18), (1019, 19), (1020, 20),
(1021, 21), (1022, 22), (1023, 23), (1024, 24), (1025, 25),
(1026, 26), (1027, 27), (1028, 28), (1029, 29), (1030, 30);
-- 8
INSERT INTO course_department (DID, CID) VALUES
(1, 101), (2, 102), (3, 103), (4, 104), (5, 105),
(6, 106), (7, 107), (8, 108), (9, 109), (10, 110),
(11, 111), (12, 112), (13, 113), (14, 114), (15, 115),
(16, 116), (17, 117), (18, 118), (19, 119), (20, 120),
(21, 121), (22, 122), (23, 123), (24, 124), (25, 125),
(26, 126), (27, 127), (28, 128), (29, 129), (30, 130);
------------ DQL_CODE---------------------------------------------
select * from student;
select * from course;
select * from course_department;
select * from enrollment;
select * from instructor;
select * from instructor_dep;
select * from instructor_course;
select * from department;

SELECT S.FName, S.LName, D.DName
FROM student S
JOIN department D ON S.DID = D.DID;



SELECT SID, FName, LName, DID
FROM student;



SELECT IC.IID, IC.FName,IC.LName,C.CName
FROM instructor IC
join instructor_course  I_C ON IC.IID=I_C.IID
JOIN course C ON C.CID=I_C.CID
;
select * from department;

select S.SID,S.FName,S.LName,D.DName
FROM student S
left join department D on S.DID=D.DID
where DName="Data Science";


SELECT FName, LName
FROM student
ORDER BY FName ASC;



SELECT DName
FROM department
ORDER BY DName ASC;



SELECT FName, LName, Level
FROM student
WHERE Level = 2;


SELECT FName, LName
FROM instructor;

select S.SID,S.FName,S.LName,C.CID,C.CName
from student S
JOIN enrollment E ON S.SID=E.SID
join course C ON E.CID=C.CID
where S.SID=5;

select  i.Fname,i.Lname ,c.Cname
from instructor i 
join instructor_course ic on i.IID=ic.IID
join course c on ic.CID=c.CID
;