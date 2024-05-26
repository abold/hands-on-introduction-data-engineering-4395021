# webserver_config.py

# import redis  # Comment this line if Redis is not needed

# Example configuration for Airflow Webserver
import os

# Base URL to access the Airflow webserver
base_url = 'http://localhost:8080'

# The IP address to bind the web server to
web_server_host = '0.0.0.0'

# The port on which to run the web server
web_server_port = 8080

# Secret key used by Flask to encrypt session cookies
secret_key = 'your_secret_key_here'

# Number of workers to run the Gunicorn web server with
workers = 4

# Web server access log file
access_logfile = os.path.join(os.getenv('AIRFLOW_HOME', '/root/airflow'), 'logs/webserver_access.log')

# Web server error log file
error_logfile = os.path.join(os.getenv('AIRFLOW_HOME', '/root/airflow'), 'logs/webserver_error.log')

# Authentication configuration (if needed)
# Uncomment the following line to enable password-based authentication
# auth_backend = 'airflow.contrib.auth.backends.password_auth'

# Session timeout settings
session_lifetime_days = 7

# Expose Prometheus metrics (optional)
# Uncomment the following line if you have Prometheus installed and want to use it
# from prometheus_flask_exporter import PrometheusMetrics
# metrics = PrometheusMetrics(app=None)

# Example: Enable or disable certain UI features
# flask_app.config['SHOW_DAG_UPDATES'] = True
# flask_app.config['SHOW_WARNINGS'] = False

# Any other custom configurations
# You can add more custom configurations below
