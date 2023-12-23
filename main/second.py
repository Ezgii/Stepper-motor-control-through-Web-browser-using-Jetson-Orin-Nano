#!/home/ezgi/web_server_venv/bin/python3.8
import sys
import subprocess
import cgitb
import cgi
cgitb.enable()

#print("Content-type:text/html\r\n\r\n")
#print('<html>')
#print('<body>')

if len(sys.argv) > 1:
    angle = sys.argv[1]
    direction = sys.argv[2]
else:
    angle = "15"
    direction = "clockwise"

command = [f"/home/ezgi/web_server_venv/bin/python3.8 /home/ezgi/Desktop/codes/ezgi_cmpe244_project.py {angle} {direction}"]
try:
    # Execute the command and capture the output
    result = subprocess.run(command, shell=True)
    # Print the output of the command
    #print('<p>Output from the script:</p>')
    #print('<pre>')
    #print(result.stdout)
    #print('</pre>')
except subprocess.CalledProcessError as e:
    # Handle if the command execution fails
   print(f'Error executing the command: {e}')

#print('</body>')
#print('</html>')
