FROM python:3           

RUN git clone https://github.com/javicercasi/Sudoku.git

WORKDIR /Sudoku/58004-Cercasi Javier

RUN pip freeze > requirements.txt

RUN pip install requests

RUN pip install -r requirements.txt


CMD ["python", "./ingreso.py"]