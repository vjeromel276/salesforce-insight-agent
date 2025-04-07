# extract/metadata_api.py

def summarize_fields(fields):
    field_summaries = []
    for f in fields:
        summary = {
            "name": f["name"],
            "label": f.get("label"),
            "type": f.get("type"),
            "relationshipName": f.get("relationshipName"),
            "referenceTo": f.get("referenceTo"),
            "custom": f.get("custom")
        }
        field_summaries.append(summary)
    return field_summaries

def fetch_object_schema(sf, object_names, include_fields=False):
    schema = {}
    for name in object_names:
        try:
            desc = sf.__getattr__(name).describe()
            if include_fields:
                desc["field_summary"] = summarize_fields(desc["fields"])
            schema[name] = desc
            print(f"Fetched schema for: {name}")
        except Exception as e:
            print(f"Error fetching {name}: {e}")
    return schema
