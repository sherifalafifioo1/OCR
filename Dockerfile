FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt


# Install Tesseract-OCR libraries
RUN apt-get install -y tesseract-ocr libtesseract-dev

# Set environment variable for Tesseract data path (adjust path if needed)
ENV TESSDATA_PREFIX=/usr/share/tesseract-ocr/tessdata

COPY . .

CMD ["gunicorn", "main:app"]
