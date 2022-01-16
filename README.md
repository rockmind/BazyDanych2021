# Bazy Danych 2021

## Członkowie grupy
- Błażej Szulc [bszulc@student.agh.edu.pl](mailto:bszulc@student.agh.edu.pl)
- Katarzyna Szulc [kasiaszulc@student.agh.edu.pl](mailto:kasiaszulc@student.agh.edu.pl)

## Wybrane technologie 
- RDBS: [PostgresSQL](https://www.postgresql.org/)
- Język: [Python 3.10](https://www.python.org/)
- Web framework: [FastApi](https://fastapi.tiangolo.com/)
 
# Cel projektu
Celem projektu jest zaimplementowanie systemu realizującego
wybrane podstawowe operacje w przykładowej bazie Northwind
w wybranej technologii.

# Baza Danych
Do postawienia bazy danych z przykładowymi danymi wykorzystaliśmy gotowy skrypt umieszczony
w repozytorium https://github.com/pthom/northwind_psql.

## Inicjalizacja bazy
Do postawienia bazy danych używamy dockera i obrazu postgres:14.1-alpine.
Tworzymy swój własny obraz w którym umieszczemy skrypt do zainicjalizowania schematu bazy northwind.

