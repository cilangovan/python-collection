import boto3

my_session = boto3.session.Session(profile_name="chrz_root")

ec2_console_resource=my_session.resource(service_name="ec2",region_name="us-east-1")

#print dir(ec2_console_resource)

#for each_in in  ec2_console_resource.instances.all():

# print each_in.state,each_in.id

# f1={"Name": "instance-state-name" ,"Values":['stopped','running']}
#
# for each_in in  ec2_console_resource.instances.filter(Filters=[f1]):
#
#  print each_in.state,each_in.id
#
#
# f2={"Name": "availability-zone" ,"Values":['us-east-1a']}
#
# for each_in in  ec2_console_resource.instances.filter(Filters=[f2]):
#
#  print each_in.state,each_in.id
#
#
#
# for each_in in  ec2_console_resource.instances.filter(Filters=[f1,f2]):
#
#  print each_in.state,each_in.id

# ftags={'Name': 'tag:env_value', 'Values':['dev','test']}
# for each_in in  ec2_console_resource.instances.filter(Filters=[ftags]):
#
#  print each_in.state,each_in.id

ftags={'Name': 'tag:env_value', 'Values':['dev','test']}
for each_in in  ec2_console_resource.instances.filter(Filters=[ftags],InstanceIds=['i-0944f5045fef1d9d3','i-0b36060f1d712f5ad']):

  print each_in.state,each_in.id
