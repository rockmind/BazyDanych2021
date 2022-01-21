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
`curl --request GET  --url http://${host}:8888/customers/${customer_id}`

### get customer orders
`curl --request GET  --url http://${host}:8888/customers/${customer_id}/orders`

### delete customer
`curl --request DELETE --url http://${host}:8888/customers/${customer_id}`

### create customer
```
curl --request POST \
  --url http://${host}:8888/customers/ \
  --header 'Content-Type: application/json' \
  --data '	{
		"customer_id": "${customer_id}",
		"company_name": "${company_name}",
		"contact_name": "${contact_name}",
		"contact_title": "${contact_title}",
		"address": "${address}",
		"city": "${city}",
		"postal_code": "${postal_code}",
		"country": "${country}",
		"phone": "${phone}",
		"fax": "${fax}"
	}'
```

### update customer
```
curl --request PUT \
     --url http://${host}:8888/customers/${customer_id} \
     --header 'Content-Type: application/json' \
     --data '{
        "company_name": "${company_name}",
        "contact_name": "${contact_name}",
        "contact_title": "${contact_title}",
        "address": "${address}",
        "city": "${city}",
        "postal_code": "${postal_code}",
        "country": "${country}",
        "phone": "${phone}",
        "fax": "${fax}"
     }'
```