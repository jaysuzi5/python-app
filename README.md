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

## Installing ArgoCD
```bash
helm repo add argo https://argoproj.github.io/argo-helm
helm upgrade --install argocd argo/argo-cd -n argocd --create-namespace -f values-argo.yaml
```

ArgoCD CLI
```bash
brew install argocd
```

## Setting Up GitHub Runners from within K8S cluser
See documentation at: https://github.com/actions/actions-runner-controller

### Prerequisites
certificate manager
```bash
kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.8.2/cert-manager.yaml
sudo install -m 555 argocd-darwin-amd64 /usr/local/bin/argocd
```

helm installation
```bash
helm repo add actions-runner-controller https://actions-runner-controller.github.io/actions-runner-controller

helm upgrade --install --namespace actions-runner-system --create-namespace\
  --set=authSecret.create=true\
  --set=authSecret.github_token="REPLACE_YOUR_TOKEN_HERE"\
  --wait actions-runner-controller actions-runner-controller/actions-runner-controller
```

run the deployment under k8s/actions-runner
```bash
k apply -f actions-runner-deployment.yaml
```

## Working with ArgoCD CLI
Login to the server:
```bash
argocd login argocd.home.com --insecure --grpc-web --username admin --password <<argocd-password>>
```

List apps
```bash
argocd app list
```

Sync an app
```bash
argocd app sync python-app
```

Debug in the pod
```bash
kubectl run -it debug --rm --image=nicolaka/netshoot -n actions-runner-system -- bash
```