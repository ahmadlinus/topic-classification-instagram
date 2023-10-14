FROM python:3.9.7-slim
WORKDIR /
EXPOSE 8000:8000
COPY . .
RUN python3 -m venv venv
# activating python environment
ENV PATH="venv/bin:$PATH"

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# installing requirements
RUN pip install -r requirements.txt

# run the final app
ENTRYPOINT python app.py