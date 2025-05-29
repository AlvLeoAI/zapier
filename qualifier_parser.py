import json

# Parse the raw_body string from Zapier into a Python dictionary
data = json.loads(input['raw_body'])

# Function to flatten nested dictionaries
def flatten(d, parent_key='', sep='_'):
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten(v, new_key, sep=sep).items())
        else:
            if isinstance(v, str):
                v = v.replace('\\n', '<br>').replace('\n', '<br>')
            items.append((new_key, v))
    return dict(items)

# Flatten the JSON structure
flat_data = flatten(data)

# Determine lead status
email = flat_data.get("email", "")
tag = flat_data.get("tags", "").lower()

if email.endswith("@gmail.com") or tag == "vip":
    flat_data["lead_status"] = "hot"
else:
    flat_data["lead_status"] = "cold"

# Return processed data
output = flat_data
