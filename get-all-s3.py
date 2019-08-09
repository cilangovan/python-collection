import boto3

my_session = boto3.session.Session(profile_name="root")

s3_re=my_session.resource(service_name="s3",region_name="us-east-1")

 # print(s3_re.buckets.all())


#
#for each_bucke_info in s3_re.all():

   # print(each_bucke_info)


for bucket in s3.buckets.all():
    if bucket.name.startswith("myapp-"):
        print bucket.name