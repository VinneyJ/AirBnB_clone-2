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
## 3. Python is cool!

Write a script that starts a Flask web application:

   - Your web application must be listening on 0.0.0.0, port 5000
   - Routes:
       - /: Hello HBNB!display
       - /hbnb: HBNBdisplay
       - /c/<text>:  followed by the value of the text variable (replace underscore _ symbols with a space )C display
       - /python/(<text>): , followed by the value of the text variable (replace underscore _ symbols with a space )Python display
       - The default value of text "is cool" 
   - You must use the option strict_slashes=False in your route definition

```
guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.3-hbnb_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```
In another tab:

```
guillaume@ubuntu:~$ curl -Ls 0.0.0.0:5000/python/is_magic ; echo "" | cat -e
Python is magic$
guillaume@ubuntu:~$ curl -Ls 0.0.0.0:5000/python ; echo "" | cat -e
Python is cool$
guillaume@ubuntu:~$ curl -Ls 0.0.0.0:5000/python/ ; echo "" | cat -e
Python is cool$
guillaume@ubuntu:~$ 
```

## 4. Is it a number?


Write a script that starts a Flask web application:

   - Your web application must be listening on 0.0.0.0, port 5000
   - Routes:
       - /: Hello HBNB!display
       - /hbnb: HBNBdisplay
       - /c/<text>:  followed by the value of the text variable (replace underscore _ symbols with a space )C display
       - /python/(<text>): , followed by the value of the text variable (replace underscore _ symbols with a space )Python display
       - The default value of text is "is cool"

       - /number/<n>: display "n is a number" if n is an integer 
   - You must use the option strict_slashes=False in your route definition

```
guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.3-hbnb_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```
In another tab:

```
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number/89 ; echo "" | cat -e
89 is a number$
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number/8.9 
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number/python 
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
guillaume@ubuntu:~$
```

## 5. Number template

Write a script that starts a Flask web application:

   - Your web application must be listening on 0.0.0.0, port 5000
   - Routes:
       - /: Hello HBNB!display
       - /hbnb: HBNBdisplay
       - /c/<text>:  followed by the value of the text variable (replace underscore _ symbols with a space )C display
       - /python/(<text>): , followed by the value of the text variable (replace underscore _ symbols with a space )Python display
       - The default value of text is "is cool"

       - /number/<n>: display "n is a number" if n is an integer
       - /number_template/<n>: display a HTML page only if n is an integer:
       - H1 tag: "Numneber: n" inside the tag BODY  
   - You must use the option strict_slashes=False in your route definition

```
guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.5-number-template
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```
In another tab:

```
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_template/89 ; echo ""
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>
        <H1>Number: 89</H1>
    </BODY>
</HTML>
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_template/8.9 
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_template/python 
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
guillaume@ubuntu:~$
```

## 6. Odd or even?

Write a script that starts a Flask web application:

   - Your web application must be listening on 0.0.0.0, port 5000
   - Routes:
       - /: Hello HBNB!display
       - /hbnb: HBNBdisplay
       - /c/<text>:  followed by the value of the text variable (replace underscore _ symbols with a space )C display
       - /python/(<text>): , followed by the value of the text variable (replace underscore _ symbols with a space )Python display
           - The default value of text is "is cool"

       - /number/<n>: display "n is a number" if n is an integer
       - /number_template/<n>: display a HTML page only if n is an integer:
           - H1 tag: "Number: n" inside the tag BODY
       - /number_odd_or_even/<n> : display a HTML page only if n is an integer:		                - H1 tag: "Number: n is even|odd" inside the tag   
   - You must use the option strict_slashes=False in your route definition

```
guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.5-number-template
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```
In another tab:

```
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_odd_or_even/89 ; echo ""
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>
        <H1>Number: 89 is odd</H1>
    </BODY>
</HTML>
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_odd_or_even/32 ; echo ""
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>
        <H1>Number: 32 is even</H1>
    </BODY>
</HTML>
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_odd_or_even/python 
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
guillaume@ubuntu:~$ 
```