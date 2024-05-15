FROM python:3.10-slim
ENV TOKEN='6992353388:AAFlB4nOx4fe8JEN070n9vUOTEAfi3wolns'
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "Latbot.py"]