import requests
import json

url = "http://220.227.107.72:8020/webhook/service"

payload = json.dumps({
  "intent_name": "get_user_info",
  "parameters": {
    "form_data": {
      "intent_name": "get_user_info",
      "parameters": {
        "new_user": True,
        "user_identity": "170226374276739925",
        "form_data": {
          "Code": "8446ZVZW"
        }
      },
      "flow_name": "get_user_info"
    }
  },
  "form_data": {
    "intent_name": "get_user_info",
    "parameters": {
      "new_user": True,
      "user_identity": "170226374276739925",
      "form_data": {
        "Code": "8446ZVZW"
      }
    },
    "flow_name": "get_user_info"
  },
  "flow_name": "get_user_info"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

