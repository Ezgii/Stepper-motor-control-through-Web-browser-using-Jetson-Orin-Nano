
### Code

1. Motor driver code:

   Save [ezgi_cmpe244_project.py](https://github.com/Ezgii/CMPE244-Project/blob/main/main/ezgi_cmpe244_project.py) in `/home/ezgi/Desktop/codes`.

2. Save [second.py](https://github.com/Ezgii/CMPE244-Project/blob/main/main/second.py) in `/var/www/cgi-bin`.

3. Save [app.py](https://github.com/Ezgii/CMPE244-Project/blob/main/main/app.py) in `/var/www`.

4. Add the [html code](https://github.com/Ezgii/CMPE244-Project/blob/main/main/html.html) into a "custom html" in the wordpress webpage.

<!--- 

### To disable remote connection through wifi, type:

      sudo ifconfig wlan0 down

<img width="1305" alt="image" src="https://github.com/Ezgii/CMPE244-Project/assets/4748948/38dacff3-9e68-4660-8ec6-fea559a6a25a">

--->

### Run Flask App

Activate the virtual environemnt: 

      source deactivate
      cd
      source ./web_server_venv/bin/activate

Start flask app on Jetson Orin nano:

      cd /var/www
      flask run --host=0.0.0.0

### Open the web-browser

Go to http://192.168.3.2/site/ on any device.




