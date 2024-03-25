FROM python:3.9

# Update package repositories
RUN apt-get update

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

# Install Tesseract-OCR and related packages
RUN apt-get install -y tesseract-ocr libtesseract-dev

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . .

# Expose the port on which the Flask app will run
EXPOSE 8000

# Set the entry point command for the container
CMD ["python", "main.py"]
