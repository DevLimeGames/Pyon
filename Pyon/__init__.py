__version__ = "1.0.0"

def decode_value(value):
    value = value.strip()

    if value.startswith("--"):
        return None  

    value = value.lower()

    if value == "null":
        return None
    if value == "true":
        return True
    if value == "false":
        return False
    if value.isdigit():
        return int(value)
    if value.startswith("[") and value.endswith("]"):
        return [decode_value(v) for v in value[1:-1].split(",") if v.strip()]
    if value.startswith("{") and value.endswith("}"):
        items = value[1:-1].split(",")
        return {k.strip(): decode_value(v) for k, v in (item.split(":") for item in items if ":" in item)}
    if value.startswith("(") and value.endswith(")"):
        return tuple(decode_value(v) for v in value[1:-1].split(",") if v.strip())

    return value

def encode_value(value):
    if isinstance(value, str) and value.startswith("--"):
        return value  
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, int):
        return str(value)
    if isinstance(value, list):
        return "[" + ",".join(encode_value(v) for v in value) + "]"
    if isinstance(value, dict):
        return "{" + ",".join(f"{k}:{encode_value(v)}" for k, v in value.items()) + "}"
    if isinstance(value, tuple):
        return "(" + ",".join(encode_value(v) for v in value) + ")"

    return str(value)

def load(file, target=None):
    try:
        groupData = {}

        for line in file:
            line = line.strip()
            if line.startswith("--") or not line:
                continue  

            parts = line.split(":")
            if len(parts) < 2:
                continue  

            group = parts[0]
            key = parts[1]
            value = ":".join(parts[2:]) if len(parts) > 2 else ""  

            if target is None or group == target:
                if group not in groupData:
                    groupData[group] = {}
                decoded_value = decode_value(value)
                if decoded_value is not None:
                    groupData[group][key] = decoded_value

        return groupData
    except IOError:
        print("Cannot read file.")

def save(file, data, category, overwrite=False, indent=4):
    try:
        lines = file.readlines()
        file.seek(0)
        file.truncate()

        existing_data = {}
        for line in lines:
            line = line.strip()
            if line.startswith("--") or not line:
                file.write(line + "\n")
                continue  

            parts = line.split(":")
            if len(parts) < 2:
                continue

            group = parts[0]
            key = parts[1]
            value = ":".join(parts[2:]) if len(parts) > 2 else ""

            if group not in existing_data:
                existing_data[group] = {}
            existing_data[group][key] = decode_value(value)

        if overwrite:
            existing_data = {category: data.get(category, {})}
        else:
            if category not in existing_data:
                existing_data[category] = {}

            old_data = existing_data[category]
            new_data = data.get(category, {})

            merged_data = {**old_data, **new_data}
            existing_data[category] = merged_data

        for group, keys in existing_data.items():
            file.write(f"{group}:\n")
            for key, value in keys.items():
                file.write(" " * indent + f"{key}:{encode_value(value)}\n")
    except IOError:
        print("Cannot read file.")

__all__ = ["decode_value", "encode_value", "load", "save"]