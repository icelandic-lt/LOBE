FROM python:3.10-slim-buster
# Install ffmpeg for audio processing and clean the apt cache
RUN apt-get update && apt-get install -y ffmpeg && rm -rf /var/lib/apt/lists/*
# create a virtual environment
RUN python -m venv /venv
# setup the directory for the project in /lobe
RUN mkdir /lobe
# set the working directory
WORKDIR /lobe
# add the necessary files
ADD migrations migrations
ADD src src
ADD pyproject.toml pyproject.toml
# install the dependencies from the pyproject.toml file and the production dependencies
# We also install the project in editable mode so that the templates are available
# We might want to change this in the future
RUN /venv/bin/pip install -e .[prod]
# set the entrypoint
ENTRYPOINT ["/venv/bin/python", "-m", "gunicorn", "-w", "4", "lobe:create_app()"]
