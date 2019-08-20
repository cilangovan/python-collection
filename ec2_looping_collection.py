# collection meathod : all() , limit()  filter

import boto3
import pprint

session=boto3.session.Session(profile_name="chrz_aws_s3_mac")

#session.get_available_resources() -- resource object
#session.get_available_services() -- client object
#ec2 connection types for ec2 console
ec2_con_re=session.resource(service_name="ec2",region_name="us-east-1")

ec2_con_client=session.client(service_name="ec2",region_name="us-east-1")

#  ...
#for each_in in  ec2_con_re.instances.all():
#    print each_in.instance.id , each_in.instance_type

# print   each_in.intance_id

# pprint.pprint (ec2_con_client.describe_instances()['Reservations'])
for each_info in ec2_con_client.describe_instances()['Reservations']:

    print each_info
for each_inst in each_info['Instances']:

    print each_inst['InstanceId'], each_inst['InstanceType']