import boto3
import json

client = boto3.client('lambda', region_name='ap-southeast-2', aws_access_key_id='AKIARIYOVXDKL6P3HVCS',  aws_secret_access_key='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')
result = client.invoke(FunctionName='getBankingData', InvocationType='RequestResponse',Payload=json.dumps({"key":"value"}))

f = open("testing2.txt", "w")
for transaction in json.loads(json.load(result['Payload'].read().decode('utf-8'))['body']):
    input(transaction)
   
##with open("testing.txt") as json_file:
##    data = json.load(json_file)
##    user = json.loads(data['body'])
##    with open("output.txt", "a") as output:
##        for transaction in user:
##            output.write(transaction['data'] + "\n")

        

