# 0x04. AirBnB clone - Web framework
## 0. Hello Flask!

Write a script that starts a Flask web application:

   - Your web application must be listening on 0.0.0.0, port 5000
   - Routes:
       - /: Hello HBNB!display
   - You must use the option strict_slashes=False in your route definition

```
guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.0-hello_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```

In another tab:
```
guillaume@ubuntu:~$ curl 0.0.0.0:5000 ; echo "" | cat -e
Hello HBNB!$
guillaume@ubuntu:~$
```

## 1. HBNB


Write a script that starts a Flask web application:

   - Your web application must be listening on 0.0.0.0, port 5000
   - Routes:
       - /: Hello HBNB!display
       - /hbnb: HBNBdisplay
   - You must use the option strict_slashes=False in your route definition

```
guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.1-hbnb_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```
In another tab:

```
guillaume@ubuntu:~$ curl 0.0.0.0:5000/hbnb ; echo "" | cat -e
HBNB$
guillaume@ubuntu:~$ 
```