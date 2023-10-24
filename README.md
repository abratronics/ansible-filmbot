# ansible-filmbot
Simple web scraper that uses beautifulsoup

# Why?

Some friends like to make movies, and needed a way to easily remind them of film festival submissions. So this can be used for sending messages about upcoming 
film festivals.

The URL in the python script can be changed. 

This is quick and dirty. Nothing more. :)

# dependencies 

python dependencies
```
pip install requests
pip install beautifulsoup4
```

# How to run 

Adjust webhook ID and token for your server

```
ansible-playbook ansible-filmbot.yml
```

Set up cron job to run once a week 

```
0 0 * * 0 ansible-playbook ansible-filmbot.yml
```
  
