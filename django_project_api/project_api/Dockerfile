# Pull base image
FROM python:3

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
COPY ./requirements.txt /code
RUN pip install -r requirements.txt
COPY ./setup.py /code
RUN pip install -e .

# Copy project
COPY . /code