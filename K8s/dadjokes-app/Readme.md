**# Build and push Docker image**

docker build -t docker-hub-username/dadjokes-app . <br>

docker push docker-hub-username/dadjokes-app

**# Deploy to Kubernetes**

kubectl apply -f k8s/dadjokes-config.yaml <br>

kubectl apply -f k8s/flask-deployment.yaml <br>

kubectl apply -f k8s/flask-service.yaml <br>

kubectl apply -f k8s/curl-pod.yaml

**# for minikube, create a tunnel**

minikube tunnel (open new terminal, leave this running)

**# Get the IP**
kubectl get svc dadjokes-service
note the **external IP**
example:

```jsx
NAME               TYPE           CLUSTER-IP       **EXTERNAL-IP**    PORT(S)
dadjokes-service   LoadBalancer   10.104.217.198   **192.168.49.2**   80:XXXXX/TCP
```

**# curl from pod:**

kubectl exec -it curl -- sh <br>

curl http://dadjokes-service
or

curl http://192.168.49.2

**# curl outside pod:**

minikube service dadjokes-service --url
and curl to the returned URL