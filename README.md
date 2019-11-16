# Security Operation Center
InnoCTF Junior 2019 Final Project


# Requirements
------------

```
$ sudo apt-get install lksctp-tools
```


# Usage:
------------

### Для машины, которая получает данные:

> Установка скрипта
```
$ git clone https://github.com/roflanLUL/SOC.git
```
> Запуск скрипта
```
$ cd SOC/
$ sudo python3 script.py
```


### Для машины, которая отправляет данные:

> Запуск процесса
```
$ sctp_darn -H <self IP-adress> -P <self port>  -h <slaves IP>  -p <open slave's port> --send
```

# License
------------

License: MIT

Copyright © cyberkekers 2019

