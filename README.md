
# My Portfolio

Creating a website to display your resume is a great way to showcase your skills and experience to potential employers and clients in a modern and interactive format. With the right design and content, your online resume can help you stand out from the competition and make a lasting impression on your visitors.
<span style="color:blue">This text is blue.</span>


## Commands And Steps-Django


## Installation

#### Create a virtual environment

```bash
  python3 -m venv myvenv

```
#### Activate the virtual environment

```bash
source myvenv/bin/activate
```
#### Install Django
```bash
pip install django
```
#### Create a new Django project
```
django-admin startproject portfolio
```
This command will create a new directory named projectname in your current directory, which will contain the basic structure for a Django project. It will also create a manage.py file, which can be used to run various administrative tasks such as starting the development server, creating database tables, and running tests.

#### Change directory into the new project
```bash
cd portfolio
```
#### Create a new app within the project
```bash
python manage.py startapp my_profile
```
#### Run the server
```bash
python manage.py runserver
```

By following the above steps, you can create a Django project and app, and run it on a local server. From here, you can begin to add your own custom styling and content to create a unique and visually appealing online resume.


### GitHub - Repository

1. Create a new repository on GitHub by clicking on the "New" button on the main page.
2. Choose a name for your repository and add a brief description.
3. Choose whether you want your repository to be public or private.
4. Click on "Create repository".
5. On your local machine, navigate to the directory where your project is stored using the command line interface.
6. Initialize a new Git repository using the following command:


```bash
git init

```
7. Add your project files to the repository using the following command:

```bash
git add .
```
8. Commit your changes to the repository using the following command:
```bash
git commit -m "Initial commit"
```
9. Connect your local repository to the remote GitHub repository using the following command, replacing "username" with your GitHub username and "repository" with the name of your repository:

```bash
git remote add origin https://github.com/username/repository.git
```
10. Push your changes to the GitHub repository using the following command:
```bash
git push -u origin main
```
11. Enter your GitHub username and password when prompted.
12. Your changes should now be pushed to your GitHub repository.
## Deployment - AWS

To host your Django project on AWS console, you need to follow the below steps:

Update the system and upgrade any installed packages with the following commands:

```bash
sudo apt-get update
sudo apt-get upgrade

```
Install Python virtual environment with the following command:

```bash
sudo apt-get install python3-venv

```
Create a new virtual environment for your project with the following command:

```bash
python3 -m venv env_portfolio

```
Activate the virtual environment with the following command:

```bash
source env_portfolio/bin/activate

```

Install Django within the virtual environment with the following command:

```bash
pip3 install Django

```

Check the list of installed packages with the following command:

```bash
pip list

```
Install Nginx and Gunicorn with the following commands:

```bash
sudo apt-get install -y nginx
pip install gunicorn

```
Create a new Gunicorn configuration file with the following commands:

```bash
cd /etc/supervisor/conf.d/
sudo touch gunicorn.conf
sudo nano gunicorn.conf

```
Add the following lines to the file:

```bash
[program:gunicorn]
directory=/home/ubuntu/my_portfolio
command=/home/ubuntu/env_portfolio/bin/gunicorn --workers 3 --bind unix:/home/ubuntu/my_portfolio/app.sock portfolio.wsgi:application
autostart=true
autorestart=true
stderr_logfile=/var/log/gunicorn/gunicorn.err.log
stdout_logfile=/var/log/gunicorn/gunicorn.out.log

[group:guni]
programs:gunicorn

```
Create a new directory for Gunicorn logs with the following command:

```bash
sudo mkdir /var/log/gunicorn

```
Reload and update the Supervisor configuration with the following commands:
```bash
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl status

```
Check the Gunicorn error log for any errors with the following command:

```bash
sudo nano /var/log/gunicorn/gunicorn.err.log

```
Navigate to the Nginx configuration directory with the following commands:
```bash
cd ..
cd ..
cd /etc/nginx/

```
Navigate to the Nginx sites-available directory with the following command:

```bash
cd sites-available/

```

Create a new configuration file for your Django project with the following command:

```bash
sudo touch django.conf
sudo nano django.conf

```
Add the following lines to the file:

```bash
server {
    listen 80;
    server_name your-domain-name.com;
    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/ubuntu/my_portfolio;
    }
    location / {
        include proxy_params;
        proxy_pass http://unix:/home/ubuntu/my_portfolio/app.sock;
    }
}

```
Create a symbolic link for your configuration file in the sites-enabled directory with the following command:

```bash
sudo ln django.conf /etc/nginx/sites-enabled/

```
Restart the Nginx service with the following command:

```bash
sudo service nginx restart

```
Install an SSL certificate with Certbot with the following command:

```bash
sudo apt-get update
sudo apt-get install certbot python3-certbot-nginx
nslookup your-domain-name.com
sudo certbot --nginx -d YOUR DOMAIN

```
Once the SSL certificate is generated and installed, it will encrypt the traffic between the website and its visitors, providing a secure browsing experience.
## Screenshots of Website






## 🚀 About Me
I am a skilled software developer with over three years of experience in delivering secure and reliable applications. My expertise lies in back-end user development and AI-related work. Currently, I am employed as an AI and Full Stack Django Web Developer at Sayone Technology Ltd., a US-based IT firm. I have a strong background in Python programming and am dedicated to continuously improving my skills and knowledge in the field.

