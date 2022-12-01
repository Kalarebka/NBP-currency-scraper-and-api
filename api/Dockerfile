FROM python:3.10

RUN useradd --create-home fastapi
USER fastapi
ENV PATH="/home/fastapi/.local/bin:${PATH}"

WORKDIR /home/fastapi

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./api ./api

CMD ["uvicorn", "api.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]