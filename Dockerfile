# Pull base image
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Set work directory
WORKDIR /code
# Install dependencies
# set work directory
WORKDIR /app

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN yum install -y https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm
COPY --from=build /opt/headless-chromium /opt/
COPY --from=build /opt/chromedriver /opt/

COPY requirements.txt .
RUN pip install -r requirements.txt


# copy project
COPY . .