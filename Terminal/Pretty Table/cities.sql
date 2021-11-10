DROP TABLE IF EXISTS Cities;

CREATE TABLE Cities(Id INTEGER PRIMARY KEY, Name TEXT, Area INTEGER, 
    Population INTEGER, Rainfall REAL);

INSERT INTO Cities(Name, Area, Population, Rainfall) VALUES("Adelaide", 1295, 1158259, 600.5);
INSERT INTO Cities(Name, Area, Population, Rainfall) VALUES("Brisbane", 5905, 1857594, 1146.4);
INSERT INTO Cities(Name, Area, Population, Rainfall) VALUES("Darwin", 112, 120900, 1714.7);
INSERT INTO Cities(Name, Area, Population, Rainfall) VALUES("Hobart", 1357, 205556, 619.5);
INSERT INTO Cities(Name, Area, Population, Rainfall) VALUES("Sydney", 2058, 4336374, 1214.8);
INSERT INTO Cities(Name, Area, Population, Rainfall) VALUES("Melbourne", 1566, 3806092, 646.9);
INSERT INTO Cities(Name, Area, Population, Rainfall) VALUES("Perth", 5386, 1554769, 869.4);
