timeout=120
bind = '0.0.0.0:8080'
worker_class = 'gthread'
workers = 1
threads = 2
worker_tmp_dir = "/dev/shm"  #Si lo corrremos con docker
max_requests = 1000
accesslog = "-"  # Muestra los registros en la consola
errorlog = "-"   # Muestra los errores en la consola

# PARA CORRER
#gunicorn -c 'confgunicorn.py' 'configApp:create_app(env="homo")'