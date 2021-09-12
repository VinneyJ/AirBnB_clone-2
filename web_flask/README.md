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

## C is fun

Write a script that starts a Flask web application:

   - Your web application must be listening on 0.0.0.0, port 5000
   - Routes:
       - /: Hello HBNB!display
       - /hbnb: HBNBdisplay
       - /c/<text>:  followed by the value of the text variable (replace underscore _ symbols with a space )C display
   - You must use the option strict_slashes=False in your route definition

```
guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.2-hbnb_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```
In another tab:

```
guillaume@ubuntu:~$ curl 0.0.0.0:5000/c/is_fun ; echo "" | cat -e
C is fun$
guillaume@ubuntu:~$ curl 0.0.0.0:5000/c/cool ; echo "" | cat -e
C cool$
guillaume@ubuntu:~$ curl 0.0.0.0:5000/c
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p> 
```
