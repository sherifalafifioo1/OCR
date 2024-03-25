FROM python:3.9-slim-buster

RUN apt-get update && \
    apt-get -qq -y install tesseract-ocr && \
    apt-get -qq -y install libtesseract-dev

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Install OpenCV (alternatively, add it to requirements.txt)
RUN apt-get update && apt-get install -y libopencv-dev python3-opencv


# Install Tesseract-OCR libraries
RUN apt-get install -y tesseract-ocr libtesseract-dev

# Set environment variable for Tesseract data path (adjust path if needed)
ENV TESSDATA_PREFIX=/usr/share/tesseract-ocr/tessdata

COPY . .

CMD ["gunicorn", "main:app"]
