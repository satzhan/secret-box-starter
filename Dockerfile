# Secret Box by Jordan
FROM python:3.12-slim

WORKDIR /box

# bring in my programs
COPY box.py caesar.py hints.txt ./

# bring in the secret message and lock it with a Caesar shift
COPY message.txt ./
RUN mkdir locks && python3 caesar.py encrypt 11 message.txt > locks/secret1.txt && rm message.txt

# extra security!! only the owner can read the lock, and we don't run as root
RUN chmod 600 locks/secret1.txt
USER nobody

CMD ["python3", "box.py"]
