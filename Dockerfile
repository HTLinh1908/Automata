FROM python:3.10.11

ADD Rename.py . 

RUN pip install bs4

CMD ["Python", "./Rename.py"]