# flask-testing

An example repository of a Python Flask based webapp running in docker.

## Docker

To run the project locally, install [Docker](https://docs.docker.com/get-docker/).

### Dev

Prior to starting the project, create a `.env-dev` file with the following variables:

```
ENV_NAME=dev
FLASK_APP=app.py
FLASK_DEBUG=1
```

Then run `docker compose up`. This will start the flask app in development mode and should be available
at http://localhost:5000.

In the development build, code changes will automatically reload so there is no need to restart the docker container
after making a change.

### Prod

If you would like to run the production version of the project locally, create a file named `.env-prod` with the
following contents:

```
ENV_NAME=production
FLASK_APP=app/app.py
```

Next build the docker image with `docker-compose build`, then run `docker compose -f docker-compose.yml up`.

Unlike the development build, changes to the source code will not auto reload. To see your new changes, you must bring
the containers down, rebuild the container and launch it again. In a perfect world, you will never have to run the
production version locally.

### Helpful tips

You may append a `-d` to docker-compose start commands to release the shell after starting the project. To bring the
container down after starting it, run `docker-compose down`. If you start the container without the `-d` flag, press
CTRL-C in the terminal to shutdown the containers.