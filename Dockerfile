FROM python:3.12-bookworm

WORKDIR /bot

COPY req.txt ./

RUN pip install -r req.txt

COPY . ./

CMD ["python", "main.py"]

# docker build -t my_bot_image .  
# docker run  -d -it my_bot_image 
# docker ps 
# docker stop id
# docekr remover id