import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'teams_integration.settings')
import django
django.setup()

from django.core.management import call_command

from bot.models.model_intents import Intent, Bot

b=Bot.objects.get(id=6)
data=[
    {
        'name':'SOP_For_Discovery_Adding_New_Probe_Scan_Schedule',
        'response':None,
        'webhook':{"webhook_url": "http://220.227.107.72:8020/webhook/service"},
        'bot_id':b
    },
    {
        'name':'SOP_For_Distribute_File',
        'response':None,
        'webhook':{"webhook_url": "http://220.227.107.72:8020/webhook/service"},
        'bot_id':b
    },
    {
        'name':'SOP_For_Linux_Agent_Installation',
        'response':None,
        'webhook':{"webhook_url": "http://220.227.107.72:8020/webhook/service"},
        'bot_id':b
    },
    {
        'name':'SOP_For_Logs',
        'response':None,
        'webhook':{"webhook_url": "http://220.227.107.72:8020/webhook/service"},
        'bot_id':b
    },
    {
        'name':'SOP_For_Machine_Changes_Report',
        'response':None,
        'webhook':{"webhook_url": "http://220.227.107.72:8020/webhook/service"},
        'bot_id':b
    },
    {
        'name':'SOP_For_Machine_Summary',
        'response':None,
        'webhook':{"webhook_url": "http://220.227.107.72:8020/webhook/service"},
        'bot_id':b
    },
    {
        'name':'SOP_For_New_Procedures',
        'response':None,
        'webhook':{"webhook_url": "http://220.227.107.72:8020/webhook/service"},
        'bot_id':b
    },
    {
        'name':'SOP_For_Pending_Procedure',
        'response':None,
        'webhook':{"webhook_url": "http://220.227.107.72:8020/webhook/service"},
        'bot_id':b
    },
    {
        'name':'SOP_For_Remote_Control_Machine_Policy',
        'response':None,
        'webhook':{"webhook_url": "http://220.227.107.72:8020/webhook/service"},
        'bot_id':b
    },
    {
        'name':'SOP_For_Remote_Control_Message_with_Users',
        'response':None,
        'webhook':{"webhook_url": "http://220.227.107.72:8020/webhook/service"},
        'bot_id':b
    },
    {
        'name':'SOP_For_Rename_Custom_Field',
        'response':None,
        'webhook':{"webhook_url": "http://220.227.107.72:8020/webhook/service"},
        'bot_id':b
    },
    {
        'name':'SOP_For_Report_Creation',
        'response':None,
        'webhook':{"webhook_url": "http://220.227.107.72:8020/webhook/service"},
        'bot_id':b
    },
    {
        'name':'SOP_For_Scheduling_Reports',
        'response':None,
        'webhook':{"webhook_url": "http://220.227.107.72:8020/webhook/service"},
        'bot_id':b
    },
    {
        'name':'SOP_To_Export_Procedures',
        'response':None,
        'webhook':{"webhook_url": "http://220.227.107.72:8020/webhook/service"},
        'bot_id':b
    },     
    {
        'name':'SOP_To_Import_Procedures',
        'response':None,
        'webhook':{"webhook_url": "http://220.227.107.72:8020/webhook/service"},
        'bot_id':b
    }            
]
for i in data:
     print(i['name'])
     obj=Intent.objects.create(name=i['name'],response=None,webhook=i['webhook'],bot_id=i['bot_id'])
     obj.save()

