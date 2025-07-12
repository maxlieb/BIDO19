# Build and push Docker image
docker build -t maxlieb/dadjokes-app .
docker push maxlieb/dadjokes-app

# Deploy to Kubernetes
kubectl apply -f k8s/dadjokes-config.yaml
kubectl apply -f k8s/flask-deployment.yaml
kubectl apply -f k8s/flask-service.yaml
kubectl apply -f k8s/curl-pod.yaml

# curl from pod:
kubectl exec -it curl -- sh
curl http://dadjokes-service
