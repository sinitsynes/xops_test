FROM python:3.12
WORKDIR /watcher
COPY ./.env /watcher/.env
COPY ./requirements.txt /watcher/requirements.txt
RUN pip install --no-cache-dir -r /watcher/requirements.txt
COPY ./ /watcher
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]