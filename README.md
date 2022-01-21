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
Do postawienia bazy danych z przykładowymi danymi wykorzystaliśmy gotowy
[skrypt](https://raw.githubusercontent.com/pthom/northwind_psql/master/northwind.sql)
umieszczony w repozytorium https://github.com/pthom/northwind_psql.

## Inicjalizacja bazy
Do postawienia bazy danych używamy dockera i obrazu postgres:14.1-alpine.
Tworzymy swój własny obraz w którym umieszczemy skrypt do zainicjalizowania schematu bazy northwind.

# Uruchomienie aplikacji webowej

### Wymagania
 - python>=3.10

### Instalacja

`pip install -r requirements.txt -t lib`

### Uruchomienie

`PYTHONPATH=lib python src\python\northwind_db_api\run.py`

# CRUD

### get customers
```
curl --request GET  --url 'http://${host}:8888/customers/?skip=1&limit=2'
```
### get customer
`curl --request GET  --url http://127.0.0.1:8888/customers/${customer_id}`

### get customer orders
`curl --request GET  --url http://127.0.0.1:8888/customers/${customer_id}/orders`

### delete_customer
`curl --request DELETE --url http://${host}:8888/customers/${customer_id}`

### create_customer
```
curl --request POST \
  --url http://${host}:8888/customers/ \
  --header 'Content-Type: application/json' \
  --data '	{
		"customer_id": "ADAM",
		"company_name": "asd asd",
		"contact_name": "Fajna",
		"contact_title": "Firma",
		"address": "Obere Str. 57",
		"city": "Berlin",
		"postal_code": "12209",
		"country": "Germany",
		"phone": "030-0074321",
		"fax": "030-0076545"
	}'
```

### update_customer
```
curl --request PUT \
     --url http://${host}:8888/customers/${customer_id} \
     --header 'Content-Type: application/json' \
     --data '{
        "company_name": "Moja",
        "contact_name": "Fajna",
        "contact_title": "Firma",
        "address": "Obere Str. 57",
        "city": "Berlin",
        "postal_code": "12209",
        "country": "Germany",
        "phone": "030-0074321",
        "fax": "030-0076545"
     }'
```