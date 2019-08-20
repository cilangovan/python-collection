import boto3
import pprint
my_session = boto3.session.Session(profile_name="chrz_root")

ec2_console_resource=my_session.resource(service_name="ec2",region_name="us-east-1")

ec2_con_client=my_session.client(service_name="ec2",region_name="us-east-1")


# pprint.pprint(dir(ec2_console_resource.instances))
#
# ec2_console_resource.instances.start()

ftags={'Name': 'tag:env_value', 'Values':['dev']}
InIds=[]

for each_in in  ec2_console_resource.instances.filter(Filters=[ftags]):
    InIds.append(each_in.id)
    # print(each_in.id)
print("All req e2 instances :",InIds)

# waiter=ec2_con_client.get_waiter('instance_stopped')
# ec2_console_resource.instances.stop(InstanceIds=InIds)


waiter=ec2_con_client.get_waiter('instance_running')
ec2_con_client.start_instances(InstanceIds=InIds)

# ec2_console_resource.instances.start(InstanceIds=InIds)

# ec2_con_client.start_instances(InstanceIds=InIds)

waiter.wait(InstanceIds=InIds)


