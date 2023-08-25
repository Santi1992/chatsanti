FROM python:3.11

#RUN apt-get update && apt-get install -y

COPY . /app
WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

ENV PATH="/usr/bin/tesseract:${PATH}"
ENV TESSDATA_PREFIX=/usr/share/tesseract-ocr/5/tessdata

CMD ["gunicorn","--chdir","/app","-c","/app/confgunicorn.py","configApp:create_app('dev')"]
