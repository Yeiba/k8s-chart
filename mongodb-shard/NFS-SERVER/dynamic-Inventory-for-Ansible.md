### Steps to Set Up AWS Dynamic Inventory for Ansible

#### 1. **Install `boto3` and `botocore` (if not already installed):**

These Python packages are required for Ansible to interact with AWS service

```pip
pip install boto3 botocore
```

#### 2. **Download the AWS Dynamic Inventory Script:**

Ansible provides a dynamic inventory script for AWS that you can use. Download the `ec2.py` script and the `ec2.ini` configuration file.

```curl
curl -O https://raw.githubusercontent.com/ansible/ansible/devel/contrib/inventory/ec2.py
curl -O https://raw.githubusercontent.com/ansible/ansible/devel/contrib/inventory/ec2.ini
chmod +x ec2.py

```

#### 3. **Configure the `ec2.ini` File:**

* Open the `ec2.ini` file in a text editor and configure it to match your AWS environment. Key configurations include:

  * `regions`: Specify the AWS regions you want to query.
  * `destination_variable`: Set this to `public_ip_address`, `private_ip_address`, or `dns_name` depending on how you connect to the instances.
  * `vpc_destination_variable`: If your instances are in a VPC, you might want to set this to `private_ip_address`.

```ini
regions = us-east-1,us-west-2
destination_variable = public_ip_address
vpc_destination_variable = private_ip_address
```

```
ansible-playbook -i ec2.py install_nfs_common.yml
```
