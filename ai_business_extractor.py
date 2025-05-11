import json
import codecs

# The input JSON string from the previous step is available in input_data['json_output']
json_string_raw = input_data['json_output']

# --- Aggressive Cleaning ---
# Try to decode with potential errors and remove leading/trailing whitespace
try:
    # Attempt to decode, replace errors with '?' or similar if encoding is the issue
    json_string_decoded = codecs.decode(json_string_raw.encode('utf-8', 'ignore'), 'utf-8')
except Exception as e:
    # If decoding itself fails, fall back to raw string for now
    json_string_decoded = json_string_raw

# Remove leading/trailing whitespace again
json_string_stripped = json_string_decoded.strip()

# Find the index of the first opening curly brace '{'
json_start_index = json_string_stripped.find('{')

# Find the index of the last closing curly brace '}'
json_end_index = json_string_stripped.rfind('}')

if json_start_index != -1 and json_end_index != -1 and json_end_index > json_start_index:
    # If both '{' and '}' are found in the correct order,
    # assume the JSON object is between them and slice the string
    json_string_to_parse = json_string_stripped[json_start_index : json_end_index + 1]

    try:
        # Attempt to parse the sliced string
        data = json.loads(json_string_to_parse)

        # Prepare the output data (same as before)
        output = [{
            'business_official_name': data.get('business_official_name', ''),
            'business_name_used_with_customers': data.get('business_name_used_with_customers', ''),
            'public_email': data.get('public_email', ''),
            'public_phone_number': data.get('public_phone_number', ''),
            'business_address': data.get('business_address', ''),
            'service_areas': json.dumps(data.get('service_areas', [])),
            'business_hours': json.dumps(data.get('business_hours', {})),
            'warranty_information': data.get('warranty_information', ''),
            'services_offerings': json.dumps(data.get('services_offerings', [])),
            'faqs': json.dumps(data.get('faqs', [])),
            'rules_to_follow': json.dumps(data.get('rules_to_follow', [])),
            'objection_handling': json.dumps(data.get('objection_handling', [])),
            'preferred_appointment_booking_times_days_general': data.get('preferred_appointment_booking_times_days_general', ''),
            'preferred_ai_persona_characteristics': json.dumps(data.get('preferred_ai_persona_characteristics', [])),
            'preferred_ai_name': data.get('preferred_ai_name', ''),
            'initial_greeting_script': data.get('initial_greeting_script', '')
        }]

    except json.JSONDecodeError as e:
        # Handle cases where the AI output was not valid JSON *after* slicing
        output = [{
            'parse_error_after_slice': f'JSON Parse Error after slicing: {e}',
            'string_after_slice': json_string_to_parse,
            'raw_json_output': json_string_raw
        }]
    except Exception as e:
        # Handle other potential errors after slicing
        output = [{
            'other_error_after_slice': f'An error occurred after slicing: {e}',
            'raw_json_output': json_string_raw
        }]

else:
    # Handle case where '{' or '}' were not found in the expected structure
    output = [{
        'error': 'Could not find expected JSON object boundaries ({ or }).',
        'raw_string_after_strip': json_string_stripped,
        'raw_json_output': json_string_raw
    }]
