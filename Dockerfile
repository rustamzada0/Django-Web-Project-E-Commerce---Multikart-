FROM python:3.11.6

WORKDIR /code

RUN apt update -y

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt


# RUN python manage.py makemigrations

# RUN python manage.py migrate

COPY . .

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]

# sudo chmod -R 777 /home/tunay/Documents/TECH/E-commerce-Multikart-PyA3-new_Tunay/database