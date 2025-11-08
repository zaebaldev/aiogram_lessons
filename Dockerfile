FROM python:3.12-bookworm

WORKDIR /bot

COPY req.txt ./

RUN pip install -r req.txt

COPY . ./

CMD ["python", "main.py"]
