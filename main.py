1) Добавить туда 10 строк

INSERT INTO gemes (id, name, downloaded) VALUES (1,"The Forest","1 564 386")

INSERT INTO gemes (id, name, downloaded) VALUES (2,"7 Days to Die","5 364 26")

INSERT INTO gemes (id, name, downloaded) VALUES (3,"Garry s Mod","2 564 456")

INSERT INTO gemes (id, name, downloaded) VALUES (4,"Raft","1 243 431")

INSERT INTO gemes (id, name, downloaded) VALUES (5,"Terraria","2 556 431")

INSERT INTO gemes (id, name, downloaded) VALUES (6,"Phasmophobia","1 000 000")

INSERT INTO gemes (id, name, downloaded) VALUES (7,"Team Fortress 2","3 545 443")

INSERT INTO gemes (id, name, downloaded) VALUES (8,"Geometry Dash","2 323 543")

INSERT INTO gemes (id, name, downloaded) VALUES (9,"minecraft","4 543 343")

INSERT INTO gemes (id, name, downloaded) VALUES (10,"Rake","1 340 60");

2) Показать все

 SELECT * FROM (gemes)  

3) Показать только имена

 SELECT name FROM (gemes)  

4) Показать имена и скачивали

 SELECT name , downloaded FROM (gemes)  


5) Посчитать сколько игр с скачивания больше чем 1000

SELECT downloaded FROM (gemes)   WHERE id = 3

SELECT downloaded FROM (gemes)   WHERE id = 5

SELECT downloaded FROM (gemes)   WHERE id = 7

SELECT downloaded FROM (gemes)   WHERE id = 8

SELECT downloaded FROM (gemes)   WHERE id = 9

6) Показать сколько игр с скачивания меньше чем 1000


SELECT downloaded FROM (gemes)   WHERE id = 1

SELECT downloaded FROM (gemes)   WHERE id = 2

SELECT downloaded FROM (gemes)   WHERE id = 4

SELECT downloaded FROM (gemes)   WHERE id = 6

SELECT downloaded FROM (gemes)   WHERE id = 10


