import boto3

my_session = boto3.session.Session(profile_name="chrz_root")

ec2_console_resource=my_session.resource(service_name="ec2",region_name="us-east-1")

#print dir(ec2_console_resource)

#my_instance=ec2_console_resource.Instance(id="i-0944f5045fef1d9d3") -- static for one instance

#dynamic prompting
instance_id=raw_input("enter ur instance id")
my_instance=ec2_console_resource.Instance(id=instance_id)
print my_instance.state['Name']