FROM python:3.8

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  POETRY_VIRTUALENVS_CREATE=0 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_NO_INTERACTION=1 \
  VENV_PATH="/opt/pysetup/.venv" \
  POETRY_VERSION=1.4.2

ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"
# System deps:
RUN pip install "poetry==$POETRY_VERSION"



#RUN apt-get update && apt-get install make

WORKDIR /app

#COPY pyproject.toml poetry.lock ./
COPY . .
#RUN poetry config virtualenvs.create false --local
RUN poetry install

# RUN touch README.md

# RUN poetry install --no-interaction --no-root && rm -rf $POETRY_CACHE_DIR
# RUN poetry add mkdocs
RUN ls .
WORKDIR /app/docs
#RUN pip install mkdocs
# ENTRYPOINT ["mkdocs", "serve"]
CMD ["mkdocs", "serve", "--dev-addr", "0.0.0.0:8000"]
