# Pull from docker public registery the lastest python image
FROM python:latest

# Set app aa a directory for the aplication
WORKDIR /app

# create a copy of the requirement localy and install them with the pip module of python
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy the file of the project in te iworking directory
COPY . .

#start the rogram with the comande python app.py
CMD ["python", "app.py"]
