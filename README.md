## docker-compose to spin up a Backend and Frontend service built on Flask 
### Building and Starting both services    

We can spin up both the fontend and backend service using: `> docker-compose up`  
  <br />
### Building and Starting individual services  
  
We can spin up the frontend service using: `> docker-compose up frontend-service`  
to spin up the backend service we can use: `> docker-compose up backend-service`  
  <br />
### Starting individual services (if the service has already been built)
  
We can spin up the frontend service using: `> docker-compose start frontend-service`  
to spin up the backend service we can use: `> docker-compose start backend-service`  
  <br />

### Stopping individual services  
  
We can spin up the frontend service using: `> docker-compose stop frontend-service`  
to spin up the backend service we can use: `> docker-compose stop backend-service`  
  <br />

### Accessing these services on the browser  

The host for both these services run on **IP 0.0.0.0**  
The frontend service is using **PORT 5000**  
The backend service is using **PORT 5001**  
  
The access frontend service http://0.0.0.0:5000  
The access backend service http://0.0.0.0:5001
  <br />
  
  
### Stops and removes all docker containers, images, volumes and networks created
  
We can stop and remove the frontend and backend service using: `> docker-compose down`
