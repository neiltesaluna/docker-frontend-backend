# Docker Compose using Flask to spin up a Backend and Frontend service

We can spin up both the fontend and backend service using: `> docker-compose up`

### Starting individual services

We can spin up the frontend service using: `> docker-compose up frontend-service`
to spin up the backend service we can use: `> docker-compose up backend-service`


### Accessing these services on the browser

The host for both these services run on IP 0.0.0.0
The frontend service is using port 5000
The backend service is using PORT 5001


The access frontend service http://0.0.0.0:5000
The access backend service http://0.0.0.0:5001
