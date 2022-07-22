# RaspberryPiWebServer
I am attempting to control GPIO pins using a web page and python scripts, so that I can control my evaporative cooler from any device and from anywhere, and eventually hook it up to other things around the house to control.
So far, its not going great, couldn't get PHP to run my python scripts, seems like it's something to do with permissions. It's on hold right now while I dig a bit more into this and hopefully find a solution.

I was able to get the actual web server up and running, and I could use SSH to run my python scripts over the local network. So, proof of concept  is there, but there's a gap in my knowledge that I need to fill before this thing is going to work.

Once I do figure out how to turn on an LED from a web page, I can design the control panel and hook the Pi up to the evaporative cooler, and write some scripts to run timers, run depending on tempurature, etc etc. The cooler only has two switches, one for the water pump and one for the fan, so I should be able to add a ton more functionality to it and make it a more effective cooling device for our home.
