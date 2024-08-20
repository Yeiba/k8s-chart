Prerequisites

**Boto3 and Botocore Installed**: Python libraries needed for Ansible to interact with AWS.

```
pip install boto3 botocore
```

### 

#### Step 2: Configure Ansible Dynamic Inventory

1. **Download AWS EC2 Dynamic Inventory Plugin**: Use the Ansible dynamic inventory plugin for AWS EC2. Ensure you have the `amazon.aws` collection installed

```
ansible-galaxy collection install amazon.aws
```

Step 1: Create AWS Dynamic Inventory Script

**Create an inventory file** (`inventory.yml`):

```
plugin: amazon.aws.aws_ec2
regions:
  - us-west-2

filters:
  instance-state-name: running
  tag:aws:eks:cluster-name: my-cluster  # Replace with your EKS cluster name tag

keyed_groups:
  - key: tags.Name
    prefix: tag_Name
    separator: '_'
  - key: placement.region
    prefix: aws_region
  - key: vpc_id
    prefix: vpc_id

hostnames:
  - tag:Name
  - public_ip_address
  - private_ip_address

compose:
  ansible_host: public_ip_address

aws_profile: default


```

**Make the script executable**:

```
chmod +x ./inventory.yml
```

Step 4: Configure the Dynamic Inventory

**Create or update `ansible.cfg`** to point to the dynamic inventory script:

```
[defaults]
inventory = ./inventory.yml

```

**Set up AWS environment variables**:

```
export AWS_REGION=us-west-2
export AWS_PROFILE=default
```

### Step 5: Write Ansible Playbooks

Create an Ansible playbook to deploy your Kubernetes resources. For example, deploy a sample Nginx application:

```
---
- name: Deploy to EKS Cluster
  hosts: all
  tasks:
    - name: Create Kubernetes Deployment
      kubernetes.core.k8s:
        kubeconfig: /path/to/kubeconfig
        state: present
        definition:
          apiVersion: apps/v1
          kind: Deployment
          metadata:
            name: nginx-deployment
            labels:
              app: nginx
          spec:
            replicas: 2
            selector:
              matchLabels:
                app: nginx
            template:
              metadata:
                labels:
                  app: nginx
              spec:
                containers:
                - name: nginx
                  image: nginx:1.14.2
                  ports:
                  - containerPort: 80

```

### Step 6: Run the Playbook

Execute the Ansible playbook:

```
ansible-playbook -i aws_ec2.yaml deploy.yml

```

### Step 7: Access the Deployed Application

1. **Retrieve the `kubectl` configuration**:

```
aws eks --region us-west-2 update-kubeconfig --name my-cluster

```

**Check the deployment**:

```
kubectl get deployments
```

**Expose the service**:

```
kubectl expose deployment nginx-deployment --type=LoadBalancer --name=nginx-service
```

**Get the external IP**:

```
kubectl get svc nginx-service
```

<pre><div class="dark bg-gray-950 rounded-md border-[0.5px] border-token-border-medium"><div class="flex items-center relative text-token-text-secondary bg-token-main-surface-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span></span></div></div></pre>

<pre><div class="dark bg-gray-950 rounded-md border-[0.5px] border-token-border-medium"><div class="flex items-center relative text-token-text-secondary bg-token-main-surface-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span></span></div></div></pre>
