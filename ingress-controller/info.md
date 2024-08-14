github: https://github.com/dhij/cluster-demo

ingress-nginx: https://github.com/kubernetes/ingress-nginx
ingress doc: https://kubernetes.io/docs/concepts/services-networking/ingress/
ingress rewrite-target annotation doc: https://kubernetes.github.io/ingress-nginx/examples/rewrite/

cert-manager release: https://github.com/cert-manager/cert-manager/releases/tag/v1.14.4
cert-manager ACME (letsencrypt) issuer example: https://cert-manager.io/docs/configuration/acme/#creating-a-basic-acme-issuer
cert-manager certificate example: https://cert-manager.io/v1.2-docs/concepts/certificate/
cert-manager ACME challenge lifecycle: https://cert-manager.io/docs/concepts/acme-orders-challenges/#challenges

letsencrypt ACME directory URL: https://letsencrypt.org/getting-started/
how letsencrypt works: https://letsencrypt.org/how-it-works/


https://www.youtube.com/watch?v=N7W_nsEA-Ao

https://www.youtube.com/watch?v=9EVs5LcaUcs


helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx

helm template ingress-nginx ingress-nginx \
  --repo https://kubernetes.github.io/ingress-nginx \
  --version 1.10.0 \
  --namespace ingress-nginx \
  > ./ingress-controller/ingress-nginx/ingress-nginx-1-10.0.yaml