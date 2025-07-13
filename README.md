# python-app
Simple flask application that will be used to test devops flow


## Dockerbuild and deploy:

### build
```bash
 docker build -t python-app:v1 .
 docker run -p 8080:5001 python-app:v1
```

### login
```bash
docker login -u jaysuzi5
```


### push
```bash
docker build --platform linux/amd64 -t jaysuzi5/python-app:v1 .
docker tag python-app:v1 jaysuzi5/python-app:v1
docker push jaysuzi5/python-app:v1
```

## K8S deployment

### Use the mainfests 
from within k8s folder
```bash
k apply -f deploy.yaml
k apply -f service.yaml
k apply -f ingress.yaml
```

cleanup before installing via helm
```bash
kubectl delete -f ingress.yaml
kubectl delete -f service.yaml
kubectl delete -f deploy.yaml
```


## Apply using Helm
from within charts/python-app
```bash
helm install python-app -n python . --create-namespace
```
uninstalling helm before moving onto argo
```bash
helm uninstall python-app -n python
```