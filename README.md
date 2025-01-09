# AirBnB Clone - MySQL

## Description
This is the second version of our AirBnB clone project where we implement a MySQL storage engine. The project is a complete web application, integrating database storage, a back-end API, and front-end interface in a clone of AirBnB.

This repository contains the initial stage of this project, where we implement the data models with MySQL as the storage engine.

## Environment
* Language: Python3
* OS: Ubuntu 20.04 LTS
* Style guidelines: [PEP 8 (version 2.8.*)](https://www.python.org/dev/peps/pep-0008/)
* MySQL 8.0

## Installation
```bash
git clone https://github.com/yourusername/AirBnB_clone_v2.git
cd AirBnB_clone_v2
```

## Usage
First, set up MySQL databases:
```bash
cat setup_mysql_dev.sql | mysql -hlocalhost -uroot -p
cat setup_mysql_test.sql | mysql -hlocalhost -uroot -p
```

Set environment variables:
```bash
export HBNB_MYSQL_USER=hbnb_dev
export HBNB_MYSQL_PWD=hbnb_dev_pwd
export HBNB_MYSQL_HOST=localhost
export HBNB_MYSQL_DB=hbnb_dev_db
export HBNB_TYPE_STORAGE=db
```

Run the console:
```bash
./console.py
```

## Testing
```bash
python3 -m unittest discover tests
```

## Console Commands
* create - Create a new instance of a class
* show - Show an instance based on class and id
* destroy - Destroy an instance based on class and id
* all - Show all instances of a class
* update - Update attributes of an instance based on class name and id
* quit/EOF - Exit the console

## Models
* Base Model
* User
* State
* City
* Amenity
* Place
* Review

## Authors
See AUTHORS file.