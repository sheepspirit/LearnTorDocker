# Totally based on blondelg's code from here https://github.com/blondelg/docker-tor
What I've done is simply added another Tor instance and mapped its ports to my local machine. Unfortunately, this didn't work out, and I still need some help. I've commented out the non-working part of the code in core.py. If you comment the first part and uncomment the second part, you will see the problem: the program doesn't display or rotate the IP of the Tor container.

*I will leave the original description unchanged Below:*
# docker-tor
Yet another tor-on-docker project, based on a tor container and a python client
which can **send requests to tor container** and also **make tor container's
public ip rotated**.

## Dependencies
* docker-compose

## Start project
```bash
docker-compose up -d --build
```
It launches two containers:
* Tor
* Flask server

## Test
When containers are running well:
[http://127.0.0.1:5000/](http://127.0.0.1:5000/)
