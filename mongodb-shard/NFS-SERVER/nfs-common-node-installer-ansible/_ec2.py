#!/usr/bin/env python

import boto3
import os
import argparse
import json


def get_instances(filters=None):
    ec2 = boto3.resource(
        'ec2', region_name=os.getenv('AWS_REGION', 'us-east-1'))
    instances = ec2.instances.filter(Filters=filters)
    return instances


def main():
    parser = argparse.ArgumentParser(description='EC2 Inventory Script')
    parser.add_argument('--list', action='store_true',
                        help='List all instances')
    args = parser.parse_args()

    filters = [{'Name': 'instance-state-name', 'Values': ['running']}]
    instances = get_instances(filters=filters)

    if args.list:
        inventory = {}
        for instance in instances:
            inventory[instance.id] = [instance.private_ip_address]
        print(json.dumps(inventory, indent=2))


if __name__ == '__main__':
    main()
