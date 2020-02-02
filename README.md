# Web Scraping

This project have as goal scraping the news from sites

## Getting Started
```
git clone https://github.com/matttheus/web-scraping.git
```

### Prerequisites

The you things you need to install to run the project

* Just a computer with internet preferably with unix system families

### Installing

Create and active the python environment

```
$ virtualenv venv -p python3

$ source venv/bin/activate
```

Install the [requirements](https://github.com/matttheus/web-scraping/blob/master/requirements.txt)

```
$ pip install -r requirements.txt
```

## Demo

First, go the main directory where is the [folder](https://github.com/matttheus/web-scraping/tree/master/scraping) that contains the `manage.py`, the below command to create the pre-build database tables based in ORM:

```
$ python manage.py makemigrations

$ python manage.py migrate
```

Read the [file](https://github.com/matttheus/web-scraping/blob/master/scraping/sites.json) which store the search's parameters. Then, run the bellow command to get the data from the site:

``` 
$ python manage.py capturar_noticias
```

Run the server

``` 
python manage.py runserver
```

## Built With

* [Django](https://www.djangoproject.com/)

## Author

* **Matheus**

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/matttheus/web-scraping/blob/master/LICENSE) file for details

