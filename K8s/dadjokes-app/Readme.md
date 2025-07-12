# Build and push Docker image
docker build -t docker-hub-username/dadjokes-app . <br>
docker push docker-hub-username/dadjokes-app

# Deploy to Kubernetes
kubectl apply -f k8s/dadjokes-config.yaml <br>
kubectl apply -f k8s/flask-deployment.yaml <br>
kubectl apply -f k8s/flask-service.yaml <br>
kubectl apply -f k8s/curl-pod.yaml

# curl from pod:
kubectl exec -it curl -- sh <br>
curl http://dadjokes-service
