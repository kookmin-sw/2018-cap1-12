#fiel location '/var/www/flask/2018-cap1-12/flask_server/'
#path connection flask app.py and apache2
import sys

sys.path.insert(0, '/var/www/flask/2018-cap1-12/flask_server/')

from app import app as application
