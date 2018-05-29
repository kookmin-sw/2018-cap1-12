#fiel location '/var/www/flask'
#path connection flask app.py and apache2
import sys

sys.path.insert(0, '/home/ubuntu/sw/test/flask_server/')

from app import app as application