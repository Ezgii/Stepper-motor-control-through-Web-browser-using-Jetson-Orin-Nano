## How to run Python CGI script on Apache2 server [[reference]](https://stackoverflow.com/questions/44871139/how-do-i-run-python-cgi-script-on-apache2-server-on-ubuntu-16-04)

1. Install Apache2 Web Server:
   
         sudo apt-get update
         sudo apt-get upgrade
         sudo reboot
         sudo apt-get install apache2

   Open a web browser and go to http://localhost. You should see this in the browser window:

   <img width="1438" alt="image" src="https://github.com/Ezgii/CMPE244-Project/assets/4748948/a7a9ae85-913d-45aa-8a5a-e29d07f4a170">

2. Enable CGI module.

         sudo a2enmod cgi

   Here we set /var/www/cgi-bin/ as cgi-bin directory. If you want a different directory, change files appropriately.

3. Open Apache server configuration file:

         sudo vi /etc/apache2/apache2.conf

   And following lines to the end of the file.

         #########     Adding capaility to run CGI-scripts #################
         ServerName localhost
         ScriptAlias /cgi-bin/ /var/www/cgi-bin/
         Options +ExecCGI
         AddHandler cgi-script .cgi .pl .py

4. Open the below file:

         sudo vi /etc/apache2/conf-available/serve-cgi-bin.conf

   Change lines :

         ScriptAlias /cgi-bin/ /usr/lib/cgi-bin/
         <Directory "/usr/lib/cgi-bin">
             AllowOverride None
             Options +ExecCGI -MultiViews +SymLinksIfOwnerMatch
             Require all granted
         </Directory>
   
   To :

         ScriptAlias /cgi-bin/ /var/www/cgi-bin/
         <Directory "/var/www/cgi-bin/">
             AllowOverride None
             Options +ExecCGI
         </Directory>

5. Now restart apache2 server.

         sudo service apache2 restart
   
6. Now create python script say, first.py inside directory /var/www/cgi-bin/ by,

         cd /var/www/

         sudo mkdir cgi-bin

         cd cgi-bin

         sudo vi /var/www/cgi-bin/first.py

   
   and add following sample code :

         #!/usr/bin/env python
         import cgitb
         
         cgitb.enable()
         
         print("Content-Type: text/html;charset=utf-8")
         print ("Content-type:text/html\r\n")
         print("<H1> Hello, From python server :) </H1>")


   And give executable permission to first.py by,

         sudo chmod +x /var/www/cgi-bin/first.py

   Now curl will work:

         curl http://localhost/cgi-bin/first.py
         
         <H1> Hello, From python server :) </H1>
         
   Or open browser and browse http://localhost/cgi-bin/first.py. This should work and will display webpage showing "Hello, From python server :)".

   <img width="721" alt="image" src="https://github.com/Ezgii/CMPE244-Project/assets/4748948/c984745c-1797-466b-b499-5d62632fd1c1">

7. Example: Execute a .py file inside the CGI file

   **simple.py file:**

   <img width="526" alt="image" src="https://github.com/Ezgii/CMPE244-Project/assets/4748948/08550350-5927-49bf-a21a-e978c3c9ed95">


   **second.py file:**

         #!/usr/bin/env python
         import datetime
         import subprocess
         import cgitb
         
         cgitb.enable()
         
         print("Content-type:text/html\r\n\r\n")
         print('<html>')
         print('<body>')
         
         ##command = ["/bin/bash", "-c", "source /home/ezgi/archiconda3/bin/activate cmpe244", "python3", "/home/ezgi/Desktop/codes/ezgi_cmpe244_project.py"]
         
         command = ["python3", "/home/ezgi/Desktop/codes/simple.py"]
         
         try:
             # Execute the command and capture the output
             result = subprocess.run(command, capture_output=True, text=True, check=True)
         
             # Print the output of the command
             print('<p>Output from the script:</p>')
             print('<pre>')
             print(result.stdout)
             print('</pre>')
         except subprocess.CalledProcessError as e:
             # Handle if the command execution fails
            print(f'Error executing the command: {e}')
         
         print('</body>')
         print('</html>')

     **web browser:**

   ![image](https://github.com/Ezgii/CMPE244-Project/assets/4748948/29a40e3a-5856-4a8c-b6af-86841e2fc921)


8. Example: Execute a .py file inside the CGI file, using a virtual environment

   First, install virtualenv:

         export PATH="$PATH:/home/ezgi/.local/bin"

         pip install virtualenv

   Go to /home directory:

         cd

   Create a virtual environment:

         virtualenv -p /usr/bin/python3 ./web_server_venv/

   Activate the virtual environement:

         source ./web_server_venv/bin/activate

   Install numpy, for test purposes:

         pip install numpy

   Check where is python, and copy the path:

         whereis python

   copy: **/home/ezgi/web_server_venv/bin/python3.8**

   **simple.py file:**

   ![image](https://github.com/Ezgii/CMPE244-Project/assets/4748948/f8aedab2-347e-4980-8155-d4054866b390)

   **second.py file:**

         #!/home/ezgi/web_server_venv/bin/python3.8

         import subprocess
         import cgitb
         cgitb.enable()
         #print("Content-type:text/html\r\n\r\n")
         print('<html>')
         print('<body>')
         
         command = ["/home/ezgi/web_server_venv/bin/python3.8 /home/ezgi/Desktop/codes/simple.py"]
         
         try:
             # Execute the command and capture the output
             result = subprocess.run(command, shell=True)
             # Print the output of the command
             #print('<p>Output from the script:</p>')
             #print('<pre>')
             #print(result.stdout)
             # print('</pre>')
         except subprocess.CalledProcessError as e:
             # Handle if the command execution fails
            print(f'Error executing the command: {e}')
         
         print('</body>')
         print('</html>')


   **web browser:**

   ![image](https://github.com/Ezgii/CMPE244-Project/assets/4748948/2d77a05d-146d-455f-96f8-4544d42579ab)




   


   

   









