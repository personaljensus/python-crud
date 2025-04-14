CREATE EXTENSION postgis;
CREATE SCHEMA dummy;
CREATE TABLE dummy.cities ( id SERIAL PRIMARY KEY, "name" varchar(100), "img" varchar(100), geom geometry('Point', 2056));
INSERT INTO dummy.cities VALUES
  (DEFAULT, 'Site Cheseaux', 'campus_cheseaux.jpg', 'SRID=2056;POINT(2540517.10 1181200.34)'),
  (DEFAULT, 'Centre St-Roch', 'campus_st-roch.jpg', 'SRID=2056;POINT(2539560.03 1181416.72)');
