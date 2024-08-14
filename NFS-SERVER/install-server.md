youtube tutorial
https://www.youtube.com/watch?v=3BjczAl-bd4

###############################################################
ubuntu:
sudo apt-get update
sudo apt install nfs-kernel-server
sudo systemctl start nfs-kernel-server

mkdir --mode=777 /k8sdata
vim  /etc/exports 

/k8sdata *(rw,async,no_subtree_check,no_root_squash)
exportfs -a
exportfs -r
sudo systemctl restart nfs-kernel-server
sudo systemctl status nfs-kernel-server
showmount -e localhost

run node-installer-ubuntu

###############################################################
CentOs:
yum install -y nfs-utils
systemctl start nfs-server rpcbind
systemctl enable nfs-server rpcbind

mkdir --mode=777 /k8sdata
vi /etc/exports

/k8sdata *(rw,async,no_subtree_check,no_root_squash)
exportfs -a
exportfs -r
systemctl restart nfs-server rpcbind
systemctl status nfs-server rpcbind
showmount -e localhost

run node-installer-linux

helm repo add nfs-subdir-external-provisioner https://kubernetes-sigs.github.io/nfs-subdir-external-provisioner/

kubectl create ns storagenfs


helm install nfs-subdir-external-provisioner \
nfs-subdir-external-provisioner/nfs-subdir-external-provisioner \
    --set nfs.server=x.x.x.x \
    --set nfs.path=/k8sdata
    --et storageClass.onDelete-true -n storagenfs
