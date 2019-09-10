.read su19data.sql

CREATE TABLE obedience AS
  SELECT seven, instructor from students;

CREATE TABLE smallest_int AS
  SELECT time, smallest from students
  WHERE smallest>2 order by smallest limit 20;

CREATE TABLE matchmaker AS
  SELECT x.pet, x.song, x.color, y.color
  from students as x, students as y
  where x.pet = y.pet and x.song = y.song and x.time < y.time
  ;

CREATE TABLE smallest_int_having AS
  SELECT time,smallest
  from students
  group by smallest
  having instructor = 1;
