# HELP
-------------------

# LOGGING
-------------------
LOGGER.warning('message')
LOGGER.info('message')
LOGGER.debug('message')
LOGGER.error('message')

debug: error, warning info, debug
info: error, warning, info,
warning: error, warning,
error: error

# ENV
-------------------
export MONGODB_USERNAME=


# DEV
python3 manage.py runserver



sudo apt install mysql-server 
sudo mysql_secure_installation - nocpass 

sudp mysql 
SELECT user,authentication_string,plugin,host FROM mysql.user; 
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password'; 
mysql -u root -p CREATE USER 'sammy'@'localhost' IDENTIFIED BY 'password';

GRANT ALL PRIVILEGES ON . TO 'sammy'@'localhost' WITH GRANT OPTION;

systemctl status mysql.service 
sudo systemctl start mysql


















sudo systemctl restart postgresql

sudo -u postgres psql postgres
ALTER USER postgres PASSWORD 'postgres';

db - dev_nocturne
u - postgres
p - postgres



pip install django psycopg2
 sudo apt-get install libpq-dev
 pip install psycopg2-binary


........................................................
Table:
nusers - 
	url - /api-auth-users : POST : (username , password) ret - (status , profile)


users
	id, username, email, password, mobile, 
patients
	id, username, email, dob, mobile, fname, lname, mname, profile, dor, status






........................................................................
