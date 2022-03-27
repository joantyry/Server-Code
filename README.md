# Server-Code
This repo contains the project's server code.

Each server has three folders namely: codes, PostProcess and Database.
codes- This is where all the Python and C++ codes are located. (Apache CGIs)
PostProcess- Listens and processes post requests.

1. How to setup the Cloud Servers:

a. Create an Ubuntu virtual machine on Microsoft Azure (azure.microsoft.com)
b. Install Apache Server
c. Generate self signed certificates to use "https" instead of http.
d. Install Python and dependent packages: Cython, requests, sympy etc.
e. Install C++ NTL library https://libntl.org/doc/tour-unix.html.
f. Enable CGI's so as to execute Python and C++ codes as follows:

i) In the file /etc/apache2/conf-enabled/serve-cgi-bin.conf

ScriptAlias /cgi-bin/ /dir where your cgi files will be located/
<Directory /dir where your cgi files will be located/>
Options +ExecCGI
AddHandler cgi-script .cgi .py 
</Directory>

ii) In the file /etc/apache2/envvars 
change the values to (export APACHE_RUN_USER=user  export APACHE_RUN_GROUP=user)

iii) sudo a2enmod cgi
iv)  sudo service apache2 restart



2. How to setup the HomeServer:

a. Download and install XAMMP on your machine and set up a localhost server.
b. On a web browser enter your router's ip address and hit enter. You will be asked to enter a username and pwd. This information can be obtained on the router box.
c. Once you login, used DHCP protocol to reserve/assign an IP address to the machine based on its MAC addresses.
d. Select a port (large enough and not 8080) and set up traffic forwarding to this IP address based on the port selected.
e. To get the router's external IP address, type \textit{whatismyip.com} on the browser. This is the public IP address that will be used to access the localhost server on your machine online, one has to just specify the port number you selected to reach the intended server for example http://174.0.246.67:9000/
f. Follow steps c to e in (1.)
g.   Enable CGI's so as to execute Python and C++ codes as follows:
    i) In the file httpd.conf file add ”AddHandler cgi-script .py"
    ii) Restart apache server




