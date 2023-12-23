### Installing all the dependencies needed

Go to home directory:

      cd

Activate the virtual environement:

      source ./web_server_venv/bin/activate

Install the dependencies:

      pip install adafruit-circuitpython-lsm303dlh_mag

      pip install Jetson.GPIO

      pip install openai==0.28

      pip install Flask

      pip install flask-cors

To see which packages are installed:

      pip freeze

<img width="984" alt="image" src="https://github.com/Ezgii/CMPE244-Project/assets/4748948/ef87e936-aa43-4ba1-b4d8-7514bd8ec503">


To control the drivers through web-server, provide necessary permissions to the web-server user (username = www-data):

      sudo usermod -aG gpio www-data

      sudo usermod -aG i2c www-data





