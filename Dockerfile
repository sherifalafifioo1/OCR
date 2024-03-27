FROM python:3.9-slim-buster

RUN apt-get update && \
    apt-get -qq -y install tesseract-ocr && \
    apt-get -qq -y install libtesseract-dev

WORKDIR /app/tessdata

COPY requirements.txt requirements.txt

# Copy the downloaded 'ara_numbers' data filedocker build -t my-app-image .
COPY ara_number.traineddata ./ara_number.traineddata


# Install Tesseract-OCR libraries
RUN apt-get install -y tesseract-ocr libtesseract-dev

RUN apt-get install libgl1

# Set environment variable for Tesseract data path (adjust path if needed)
ENV TESSDATA_PREFIX=/usr/share/tesseract-ocr/tessdata

RUN pip3 install -r requirements.txt

COPY . .

CMD ["python", "main.py"]
