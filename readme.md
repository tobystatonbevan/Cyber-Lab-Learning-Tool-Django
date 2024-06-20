##introduction to Cyber Lab##

Django based vulnerable webservice. This is a web service intended to be hosted locally in a university cyber lab. The intention of the cyber lab is two fold; one, this tool is to host a series of learning materials and activities for students to complete. Two, this web service is deliberately vulnerable so that it may gather "real" data from student usage and exploitation of this asset can be an end of module activity for students

If the final task is to the exploitation of this service, it is recommended that tutors hide unique information or markers in their instance and verify student achievement by confirming these markers with the students. More advanced students may be tasked with implementing mitigations to this web service, but each student may need their own instance for this. 

Students should be frequently reminded of the vulnerbility of this web service and thus should not use any real data other than name and student email address. 

The web service is intended to be spun up and replaced quickly and easily, as (hopefully) the vulnerabilities should mean that it gets broken or altered regularly. Tutors should note this, and if using the sevice for assessments to ensure that results are recorded away from the web service. Students should not assume that their work or account will be there when they return, and should behave accordingly.

PLEASE NOTE: the SECRET_KEY is not obscured in any way from this repo, so if you intend to run this in any production environment outside of a segmented network you should rotate this  

##content##

Home page: home page and general content pages for cyber lab
Lessons: security testing materials (html format)
Tasks: lab activities to be completed away from cyber lab (virtual box, etc)

##TO DO##

To do:  
-sign up/log in  
-Add lessons  
-Add tasks  
-Add vulnerabilities  
-Export of student records/achievements/account data  
-deploy in docker  

##vulnerabilities##

1. Weak admin credentials
2. Weak credential storage

##To configure on an Apache server##
(pip also required)
sudo apt install apache2
sudo apt install libapache-mod-wsgi
Create venv
source venv/bin/activate
pip install -r requirement.txt in venv
git repo clone
set static ip
allow host
append to /etc/apache2/sites-available/000-default.conf:
```
    Alias /static /home/user/project/static
    <Directory /home/user/project/static>
        Require all granted
    </Directory>

    Directory /home/user/project/myproject>
        <Files wsgi.py>
            Require all granted
        </Files>
    </Directory>

    WSGIDaemonProcess project python-home=/home/user/project/myprojectenv python-path=/home/user/project
    WSGIProcessGroup project
    WSGIScriptAlias / /home/user/project/myproject/wsgi.py
```
sudo chmod 664 /home/user/project/db.sqlite3
sudo chown :www-data /home/user/project/db.sqlite3
sudo chown :www-data /home/user/project
sudo chmod 755 /home/user (or 655 and make www-data an owner)
sudo ufw allow 'Apache Full'
sudo apache2ctl configtest
sudo systemctl restart apache2
in settings.py, add STATIC_ROOT to Apache directory for static (/var/www/html/static)
in VM; sudo /home/user/venv/bin/python manage.py collectstatic
in VM; sudo nano /etc/apache2/sites-available/000-default.conf
alter to:
```
Alias /static /var/www/html/static
    <Directory /var/www/html/static>
        Require all granted
    </Directory>
```