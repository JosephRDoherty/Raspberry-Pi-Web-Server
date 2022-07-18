#!/usr/bin/python3
import cgi
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

led = 11;
GPIO.setup(led, GPIO.OUT)

def ledOn():
    GPIO.output(led, GPIO.HIGH)

def ledOff():
    GPIO.output(led, GPIO.LOW)

# Output the headers.
print("Content-Type: text/html" # html content to follow)



# Output the content.
print("""
<!DOCTYPE html>

<html>
    <head>
        <title>LED Test Page</title>
        <link rel="stylesheet" type="text/css" href="StyleSheet1.css" media="screen"/>
    </head>
    <body>
        <div id="title">
            <h1>J.Pi Server</h1>
            <p>Tech solutions for the Doherty House</p>
        </div>

        <div id="navBar">
            <ul>
                <li><button id="homescreen" onclick="location.href='index.html'" type="button">HomeScreen</button></li>
                <li><button onclick="location.href='weather.html'" type="button">Weather</button></li>
                <li><button onclick="location.href='LedTestPage.py'" type="button">LED Test</button></li>
            </ul>
        </div>

        <div>
            <h2>LED Test</h2>

        </div>
     </body>
</html>
""")

