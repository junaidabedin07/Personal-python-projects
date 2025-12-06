import json

filename = "device_config.json"
with open(filename,"r") as f:
    config_data = json.load(f)
    errors = 0
    for field in ["device_id","location","sampling_rate","broker_url","topic"]:
        if field not in config_data:
            print(f"{filename} field {field} invalidated")
            errors += 1
        else:
            print("validated")

if type(config_data["device_id"]) == str and type(config_data["location"]) == str and type(config_data["sampling_rate"]) == int and (config_data["broker_url"].startswith("mqtt://") or config_data["broker_url"].startswith("tcp://")):
    print("The configuration file checks out")
else:
    print("error in json file")