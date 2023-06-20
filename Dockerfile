# base image  
FROM python:3.11 
# setup environment variable  
ENV DockerHOME=/mangaserver


# set work directory  
RUN mkdir -p $DockerHOME  

RUN mkdir $DockerHOME/static
RUN mkdir $DockerHOME/media

# where your code lives  
WORKDIR $DockerHOME  

RUN chmod -R +rx static
RUN chmod -R +rx media

# set environment variables  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  

# install dependencies  
RUN pip install --upgrade pip  

# copy whole project to your docker home directory. 
COPY . $DockerHOME
RUN file="$(ls -1 /mangaserver)" && echo $file
# run this command to install all dependencies  
RUN pip install -r requirements.txt  
# port where the Django app runs  
#EXPOSE 8970
# start server  
CMD python manage.py createsuperuser --no-input
