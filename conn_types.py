import boto3

session=boto3.session.Session(profile_name="chrz_aws_s3_mac")

#session.get_available_resources() -- resource object
#session.get_available_services() -- client object
#ec2 connection types for ec2 console
ec2_con_re=session.resource(service_name="ec2",region_name="us-east-1")

ec2_con_client=session.client(service_name="ec2",region_name="us-east-1")


#s3 connection types for  s3 consoles

s3_con_re=session.resource(service_name="s3",region_name="us-east-1")

s3_con_client=session.client(service_name="s3",region_name="us-east-1")


