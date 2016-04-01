import elasticsearch
import csv
import random
import unicodedata
import pprint
import json
from csv import DictWriter
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
#replace with the IP address of your Elasticsearch node
es = elasticsearch.Elasticsearch(["localhost:9200"])

# Replace the following Query with your own Elastic Search Query
res = es.search(index="logstash-*", body={
    "query": {
        "match": {
            "event_id":{"query":"4725", "operator":"and"}
        }
    }
},size=1)
#this is the number of rows to return from the query... to get all queries, run script, see total number of hits, then set euqual to number >= total hits

random.seed(1)
sample = res['hits']['hits']
fields = ['caller_computer','caller_domain','caller_logon_id','caller_sid','user_account_control','account_expire','action_flags','allow_to_delegate_to','caller_user','display_name','domain','event_category','event_id','event_log','event_source','event_type','generated_time','group','group_name','home_directory','home_drive','host','log_ts','logon_hour','logon_id','machine','member','member_sid','message','msg','new_account_name','new_uac_value','old_account_name','old_uac_value','os','password_last_set','path','primary_group_id','profile_path','receive_time','repeat_count','sam_account_name','script_path','sequence_number','serial_number','sid_history','source_address','source_user','target_domain','target_sid','target_user','user','user_parameter','user_principal_name','user_workstation','virtual_system']

def filter_data(d):
    for k in d.keys():
        if k not in fields:
            d.pop(k, None)

with open("/Users/prashantthakur/Desktop/windows.csv", 'wb') as csvfile:
    writer = DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    for data in res['hits']['hits']:
        source = data['_source']
        source['_id'] = data['_id']
        filter_data(source)
        writer.writerow(source)
def sendmail(file_name):
    fromaddr = "pkt.usc@gmail.com" #sender
    toaddr = "pkt.usc@gmail.com" #receiver
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "TESTING ALERT"
    body = "Alert Regarding Windows Server Events"
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.ehlo()
    server.login(fromaddr, 'xxxxxxxxxx')#password here
    fp = file(file_name)
    attachment = MIMEText(fp.read())
    attachment.add_header('Content-Disposition', 'attachment', filename=filename)           
    msg.attach(attachment)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

filename = "/Users/prashantthakur/Desktop/windows.csv"
sendmail(filename)