FROM  jupyter/base-notebook

COPY code /code

WORKDIR /code

COPY  requirements.txt  requirements.txt

RUN  pip install  -r requirements.txt