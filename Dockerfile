FROM python:3.9-slim

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt

# Change the working directory to ensure proper module imports
WORKDIR /app/app

# Update the CMD to run from the correct directory
CMD ["python", "__init__.py"]