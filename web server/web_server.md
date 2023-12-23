## Running WordPress on Jetson Orin Nano [[reference]](https://blog.j2i.net/tag/jetson/)

### Install Apache Web Server

> $ `sudo apt-get update`

> $ `sudo apt-get upgrade`

> $ `sudo reboot`

> $ `sudo apt-get install apache2`

Open a web browser and go to http://localhost. You should see this in the browser window:

<img width="1438" alt="image" src="https://github.com/Ezgii/CMPE244-Project/assets/4748948/a7a9ae85-913d-45aa-8a5a-e29d07f4a170">

### Install PHP

> $ `sudo apt-get install php`

With the PHP interpreter in place, we can add a page with some PHP code to see it processed.

Navigate to the folder that contains the Apache HTML content and add a new page named test-page.php

> $ `cd /var/www/html`

> $ `sudo touch test-page.php`

> $ `sudo vi test-page.php`

Click i to enable insert mode. Write the below in the file, then press Esc, and type :wq to save and exit.

> `<?php echo "Hey!"; ?>`

Open a browser and go to http://localhost/test-page.php. You should see the below:

<img width="1439" alt="image" src="https://github.com/Ezgii/CMPE244-Project/assets/4748948/953b5b1e-be45-41bd-b237-e0dd85c64a06">

### Install the Database

Maria Database is a mySQL database. It will contain the content for our site. Install it with the following command.

> $ `sudo apt-get install mariadb-server`

The database is installed, but it needs to be configured. To access it, we need to setup a user account and a password. Decide what your user ID and password will be now. Also choose a name for the database. You will need to substitute my instances of USER_PLACEHOLDER, PASSWORD_PLACEHOLDER, and DATABASE_PLACEHOLDER with the names and passwords that you have chosen.

USER_PLACEHOLDER = 016042871

PASSWORD_PLACEHOLDER = my school password

DATABASE_PLACEHOLDER = mydb

> $ `sudo mysql -uroot`

You will be presented with the MariaDB prompt. Type the following commands to create your user account, database, and to give permission to the database.


> MariaDB [(none)]> `CREATE USER 'USER_PLACEHOLDER'@'localhost' IDENTIFIED BY 'PASSWORD_PLACEHOLDER';`

> MariaDB [(none)]> `CREATE DATABASE DATABASE_PLACEHOLDER;`

> MariaDB [(none)]> `GRANT ALL ON DATABASE_PLACEHOLDER.* to 'USER_PLACEHOLDER'@'localhost';`

> MariaDB [(none)]> `quit;`

We need to make sure that account can access the database. Let’s connect to the database using the account that you just created.

> $ `mysql -u USER_PLACEHOLDER -p`

You will be prompted to enter the password that you choose earlier. After you are logged in, type the following to list the databases.

> MariaDB [(none)]> `SHOW DATABASES;`

A list of the databases will show, which should include a predefined system database and the one you just created.

We also need to install a package so that PHP and MySQL can interact with each other.

> $ `sudo apt-get install php-mysql`

### Installing WordPress

The downloadable version of WordPress can be found at wordpress.org/download. To download it directly from the device to the web folder use the following command.

> $ `sudo wget https://wordpress.org/latest.zip -O /var/www/html/wordpress.zip`

Enter the folder and unzip the archive and grant permissions to Apache for the folder.

> $ `cd /var/www/html`

> $ `sudo unzip wordpress.zip`

> $ `sudo chmod 755 wordpress -R`

> $ `sudo chown www-data wordpress -R`

We are about to access our site. It can be accessed through the devices IP address at http://IP_ADDRESS_HERE/wordpress. As a personal preference, I would prefer for the site suffix to be something other than wordpress. I’m changing it to something more generic, “site”.

> $ `sudo mv wordpress site`

Now let’s restart Apache.

> $ `sudo service apache2 restart`

From here on I am going to interact with the device from another computer with a desktop browser. I won’t need to do anything in the device terminal. Using a browser on another computer I navigate to my device’s IP address in the /site folder. The IP address of my device is 192.168.1.252. The complete URL that I use is `http://192.168.1.252/site`. When I navigate there, I get prompted to select a language.

![image](https://github.com/Ezgii/CMPE244-Project/assets/4748948/eee208ac-06d9-49aa-88bc-caad60fd3ad9)

The next page lets you know the information that you will need to complete the setup. That information includes

The database name

The database user name

The database password

The database host

The Table name prefix

The first three items should be familiar. The fourth item, the database host, is the name of the machine that has the database. Since we are running the database and WordPress from the same device this entry will be “localhost”. If we were running more than one site from this device to keep the databases separate, the tables for each instance could have a common prefix. I’m going to use the prefix wp_ for all of the tables. All of this information will be saved to a file named wp-config.php. If you need to change anything later your settings can be modified from that file.

![image](https://github.com/Ezgii/CMPE244-Project/assets/4748948/11c4ed88-3cdf-4552-aa10-425ee85280de)

Enter your database name, user name, and password that you decided earlier. Leave the host name and the table prefix with their defaults and click on “submit.” If you entered everything correctly, on the next screen you will be prompted with a button to run the installation.

![image](https://github.com/Ezgii/CMPE244-Project/assets/4748948/fd14dc07-4ade-4cff-b0ea-73597c62e8ce)

On the next page you must choose some final settings of your Word Press configuration.

![image](https://github.com/Ezgii/CMPE244-Project/assets/4748948/c7425bdb-be93-4b00-be62-3c03f583bd4d)

After clicking on “Install WordPress” on this screen, you’ve completed the setup. With the instructions as I’ve written them, the site will be in the path /wordpress. The administrative interface will be in the path /wordpress/wp-admin. WordPress is easy to use, but a complete explanation of how it works could be lengthy and won’t be covered here.

http://192.168.1.252/site/wp-login.php

### Enabling CGI Scripts in Apache [[reference]](https://www.youtube.com/watch?v=ELFdP7eEZ5w)















<!---

### Enabling CGI Scripts in Apache [[reference]](https://tecadmin.net/enable-or-disable-cgi-in-apache24/)

1. Install the CGI Module (Ubuntu and Debian):
   
> $ `sudo apt-get install libapache2-mod-cgi`

2. Enable the CGI Module:

> $ `sudo a2enmod cgi`

3. Configure Apache to Execute CGI Scripts:

> $ `sudo vi /etc/apache2/apache2.conf`

4. Locate the following block of text within the configuration file

   <Directory "/var/www/html">

   (The directory path may vary depending on your system’s configuration.)

5. Add the following lines within the block:

   ![image](https://github.com/Ezgii/CMPE244-Project/assets/4748948/0b2b4b33-3a17-4412-8d00-824a51f7341a)

<img width="775" alt="image" src="https://github.com/Ezgii/CMPE244-Project/assets/4748948/3b71e2f6-b04f-4393-9e2c-ebcfcda83f18">

This configuration allows Apache to execute CGI scripts with .py file extension.

Save the changes and close the text editor.

6. Restart the Apache web server to apply the changes:

> $ `sudo systemctl restart apache2`


### Using Python CGI

1. Write the python script and make sure it has the execute permissions:

   > $ `chmod +x ezgi_cmpe244_project.py`

2. In your web directory (e.g., /var/www/html/your-directory), create a CGI script (let's call it control_motor.cgi).

> $ `cd /var/www/html/site`

> $ `sudo touch control_motor.cgi`

> $ `sudo chmod +rwx control_motor.cgi`

This CGI script will handle the requests from the web interface and trigger the ezgi_cmpe244_project.py script.

Sample control_motor.cgi:

      #!/usr/bin/python3
     
      import subprocess
      import cgi
      
      print("Content-type: text/html\n\n")
      print("<html><body>")
      
      form = cgi.FieldStorage()
      if "trigger_motor" in form:
          subprocess.run(['/home/ezgi/Desktop/codes/ezgi_cmpe244_project.py'])
          print("<h2>Motor triggered!</h2>")
      else:
          print("<h2>No action specified!</h2>")
      
      print("</body></html>")


3. Integrate web interface


-->





   




   



