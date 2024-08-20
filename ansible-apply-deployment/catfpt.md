For managing an EKS cluster with Ansible's dynamic inventory, you typically don't need to inventory the Kubernetes nodes directly because Ansible can interact with the Kubernetes API to deploy applications. However, if you want to manage or inventory EC2 instances running in your EKS cluster or other related resources, you can set up a dynamic inventory for AWS EC2 instances that belong to the EKS cluster.

Certainly! To provision a Kubernetes (K8s) deployment on AWS EKS using Ansible with dynamic inventory scripts and an alternative approach, you can follow these steps. This method will use the `aws_ec2` plugin for Ansible dynamic inventory and will involve creating a Kubernetes deployment with Ansible.

### Step-by-Step Guide

#### Prerequisites

1. **AWS Account**: Ensure you have an AWS account with permissions to create and manage EKS clusters.
2. **Ansible Installed**: Ensure Ansible is installed on your local machine.
3. **AWS CLI and eksctl Installed**: Install and configure the AWS CLI and `eksctl` tool.
4. **Boto3 and Botocore Installed**: Python libraries for interacting with AWS.

#### Step 1: Create EKS Cluster with `eksctl`

Create your EKS cluster using `eksctl`:

```bash
eksctl create cluster --name=my-cluster --region=us-west-2 --nodegroup-name=my-nodes --node-type=t3.medium --nodes=3
```

#### Step 2: Configure Ansible Dynamic Inventory

1. **Download AWS EC2 Dynamic Inventory Plugin**: Use the Ansible dynamic inventory plugin for AWS EC2. Ensure you have the `amazon.aws` collection installed:

   ```bash
   ansible-galaxy collection install amazon.aws
   ```
2. **Create `inventory.yml`**: Define your dynamic inventory configuration file. Here’s a simplified example:

   ```yaml
   plugin: amazon.aws.aws_ec2
   regions:
     - us-west-2

   filters:
     instance-state-name: running

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
3. **Create `ansible.cfg`**: Configure Ansible to use your dynamic inventory file:

   ```ini
   [defaults]
   inventory = ./inventory.yml
   ```

#### Step 3: Create a Kubernetes Deployment with Ansible

1. **Update `kubeconfig`**: Ensure your local `kubeconfig` is set up to interact with the EKS cluster:

   ```bash
   aws eks --region us-west-2 update-kubeconfig --name my-cluster
   ```
2. **Write Ansible Playbook**: Create a playbook to deploy your application. For example, create a `deploy.yml`:

   ```yaml
   ---
   - name: Deploy to EKS Cluster
     hosts: localhost
     tasks:
       - name: Create Kubernetes Deployment
         community.kubernetes.k8s:
           kubeconfig: ~/.kube/config
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

   Note: Ensure you have the `community.kubernetes` collection installed:

   ```bash
   ansible-galaxy collection install community.kubernetes
   ```
3. **Run Ansible Playbook**: Execute the playbook to deploy the application:

   ```bash
   ansible-playbook deploy.yml
   ```

#### Step 4: Access the Deployed Application

1. **Expose the Service**: You may want to expose your deployment using a Kubernetes service:

   ```bash
   kubectl expose deployment nginx-deployment --type=LoadBalancer --name=nginx-service
   ```
2. **Retrieve the External IP**: Get the external IP or DNS name of the service:

   ```bash
   kubectl get svc nginx-service
   ```

### Summary

This alternative method uses Ansible’s dynamic inventory for AWS EC2 and interacts with AWS EKS to deploy a Kubernetes application. You create the EKS cluster using `eksctl`, configure Ansible with dynamic inventory, and use a playbook to manage Kubernetes resources. Make sure to adjust configurations and playbook details to suit your specific needs and environment.

Here's a real example of an `inventory.yml` file for dynamically querying EC2 instances using the `aws_ec2` plugin from the `amazon.aws` collection. This file can be used to inventory EC2 instances that may be part of your EKS cluster or other resources.

### Example `inventory.yml`

```yaml
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

### Key Sections Explained

- **plugin**: Specifies the Ansible dynamic inventory plugin to use (`amazon.aws.aws_ec2`).
- **regions**: Lists the AWS regions to query for EC2 instances. Adjust this to match your region(s).
- **filters**: Filters the EC2 instances to include only those that are in the "running" state and have a specific tag that identifies them as part of your EKS cluster. Replace the `tag:aws:eks:cluster-name` with the actual tag used for your EKS cluster.
- **keyed_groups**: Defines how to group instances based on their attributes:

  - **key**: The attribute used for grouping.
  - **prefix**: The prefix for the group names.
  - **separator**: The separator between values in group names.
- **hostnames**: Determines which instance metadata to use for hostnames. In this example, it tries the `Name` tag first, followed by the public and private IP addresses.
- **compose**: Defines additional host variables. In this case, it sets `ansible_host` to the public IP address of the instances.
- **aws_profile**: Specifies the AWS CLI profile to use. Make sure this profile has the necessary permissions.

### How to Use This Inventory File

1. **Save the Configuration**: Save the YAML configuration as `inventory.yml`.
2. **Configure Ansible**: Update your `ansible.cfg` to use this dynamic inventory file:

   ```ini
   [defaults]
   inventory = ./inventory.yml
   ```
3. **Run Ansible Commands**: Use the dynamic inventory with Ansible commands or playbooks:

   ```bash
   ansible-inventory -i inventory.yml --graph
   ```

   Or run a playbook:

   ```bash
   ansible-playbook -i inventory.yml deploy.yml
   ```

### Notes

- **EKS Nodes**: If you want to specifically manage nodes or other resources related to EKS, ensure that the filters and tagging accurately reflect your infrastructure.
- **Permissions**: Ensure that your AWS profile or credentials have appropriate permissions to list EC2 instances and their metadata.

This setup helps you dynamically manage and organize your EC2 instances based on their attributes and tags, which can be useful for managing infrastructure that interacts with or supports your EKS cluster.
