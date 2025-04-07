# extract_metadata.py

import argparse
import json
from auth.sf_auth import connect_salesforce
from extract.metadata_api import fetch_object_schema

def main():
    parser = argparse.ArgumentParser(description="Extract Salesforce object schema.")
    parser.add_argument('--field_level', action='store_true', help='Include field-level relationships and details')
    parser.add_argument('--objects', type=str, help='Comma-separated list of object API names')
    args = parser.parse_args()

    sf = connect_salesforce()

    object_names = (
        [o.strip() for o in args.objects.split(',')]
        if args.objects else
        ['Account', 'Opportunity', 'Lead', 'Contact']
    )

    schema = fetch_object_schema(sf, object_names, include_fields=args.field_level)
    output_file = "sf_schema_detailed.json" if args.field_level else "sf_schema.json"

    with open(output_file, "w") as f:
        json.dump(schema, f, indent=2)

    print(f"✅ Saved schema to {output_file}")

if __name__ == "__main__":
    main()
