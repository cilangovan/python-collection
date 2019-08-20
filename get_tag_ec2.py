import boto3

my_session = boto3.session.Session(profile_name="chrz_root")

ec2_console_resource=my_session.resource(service_name="ec2",region_name="us-east-1")

in_id=raw_input("enter instance id:")

my_in_ob=ec2_console_resource.Instance(id=in_id)

print dir(my_in_ob)

print my_in_ob.tags