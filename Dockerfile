# Secret Box by Jordan
FROM python:3.12-slim

WORKDIR /box

# bring in my programs
COPY box.py caesar.py hints.txt ./

# bring in the secret message and lock it with a Caesar shift
COPY message.txt ./
RUN mkdir locks && python3 caesar.py encrypt 11 message.txt > locks/secret1.txt && rm message.txt

CMD ["python3", "box.py"]
