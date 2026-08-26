FROM python:3.11-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    VIRTUAL_ENV=/opt/venv \
    PATH="/opt/venv/bin:$PATH"

RUN apt-get update \
    && apt-get install -y --no-install-recommends ca-certificates git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /opt/robustocs

COPY . /opt/robustocs

RUN python -m venv /opt/venv \
    && pip install --upgrade pip \
    && pip install "numpy<2" robustocs==0.2.1

RUN git clone --depth 1 https://github.com/Foggalong/RobustOCS.git /opt/robustocs-upstream

COPY robustocs-cli.py /usr/local/bin/robustocs
RUN chmod +x /usr/local/bin/robustocs

ENTRYPOINT ["robustocs"]
CMD ["--help"]
