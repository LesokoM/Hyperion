CREATE TABLE Student (

    STU_NUM CHAR(6),
    STU_SNAME VARCHAR(15),
    STU_FNAME VARCHAR(15),
    STU_INITIAL CHAR(1),
    STU_STARTDATE DATE,
    COURSE_CODE CHAR(3),
    PROJ_NUM INT(2),
    PRIMARY KEY (STU_NUM)


); -- Creating my table 


INSERT INTO Student (STU_NUM,STU_SNAME, STU_FNAME,STU_INITIAL,
STU_STARTDATE, COURSE_CODE,PROJ_NUM)
    
    VALUES ('01','Snow', 'John', 'E', '2014-04-05','201',6),
            ('02','Stark', 'Arya', 'C', '2017-07-12','305',11),
            ('03','Lannister', 'Jamie', 'C', '2012-09-05','101',2),
            ('04','Lannister', 'Cercei', 'J', '2012-09-05','101',2),
            ('05','Greyjoy', 'Theon', 'I', '2015-12-09,','402',14),
            ('06','Tyrell', 'Margaery', 'Y', '2017-07-12','305',10),
            ('07','Baratheon', 'Tommen', 'R', '2019-06-13','201',5);
            
            -- Inserting my values
            
            
Select 'Q1' AS message;
SELECT * FROM Student 
WHERE COURSE_CODE = '305'; -- Selectig students with 305 course code

            
UPDATE Student 
SET COURSE_CODE = '304'
WHERE STU_NUM = '07'; -- Changing course code for studnet number 7

            
Select 'Q2' AS message;
SELECT * FROM Student;

DELETE FROM Student 
WHERE STU_SNAME = 'Lannister' AND STU_FNAME = 'Jamie' AND STU_STARTDATE = '2012-09-05'AND
COURSE_CODE = '101' AND PROJ_NUM = 2; -- Removing Jamie from database
            
            
Select 'Q3' AS message;          
SELECT * FROM Student;   

UPDATE Student
SET PROJ_NUM = '14'
WHERE STU_STARTDATE < '2016-01-01' AND COURSE_CODE <= 201; -- Changing project num for older students

    
Select 'Q4' AS message;          
SELECT * FROM Student;   

DROP TABLE Student; -- Deleting table

