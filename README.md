# Software-Engineer-Exam
to install, create the database test in mariadb

CREATE DATABASE test;
exit;

then install the following libraries

linux (debian-based distro)

*if you already have the django, djangorestframework, mysqlclient libraries installed, avoid installing these libraries

```sudo pip3 uninstall jwt```


```sudo pip3 install pyjwt```


```pip3 install django```


```pip3 install djangorestframework```


```sudo apt install default-libmysqlclient-dev```


```sudo pip3 install mysqlclient```


```pip3 install django-cors-headers```


```pip3 install drf-yasg```


```pip3 install PyMySQL```


```pip3 install djangorestframework-simplejwt```

change the parameters of the database connection in the settings.py file

move to the folder where we have downloaded the project and migrate the changes

import the json file to postman to be able to see the calls


