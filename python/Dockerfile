FROM python:3.11-slim

# Evitar prompts interactivos
ENV DEBIAN_FRONTEND=noninteractive     PIP_NO_CACHE_DIR=1

# Paquetes de sistema mínimos (y build tools por si se compila algo)
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        curl \
        ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Librerías de clase + utilidades
COPY requirements.txt /tmp/requirements.txt
RUN python -m pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt

# Directorio de trabajo y usuario no-root
WORKDIR /work
RUN useradd -ms /bin/bash student && chown -R student:student /work
USER student

# Exponer Jupyter
EXPOSE 8888

# Correr JupyterLab sin token/contraseña, útil para clase local
CMD ["bash", "-lc", "jupyter lab --ip=0.0.0.0 --port=8888 --NotebookApp.token='' --NotebookApp.password='' --no-browser --NotebookApp.allow_origin='*' --NotebookApp.allow_remote_access=True"]
