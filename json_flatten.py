import json

def read_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
    
def flatten(data, path="", result=None):
    if result is None:
        result = {}
        
    if isinstance(data, dict):
        for key, value in data.items():
            dict_path = f"{path}.{key}"
            flatten(value, dict_path, result)
    
    elif isinstance(data, list):
        for item in data:
            list_path = f"{path}[]"
            flatten(item, list_path, result)
            
    else:
        if path not in result:
            result[path] = data
        else:
            if not isinstance(result[path], list):
                result[path] = [result[path]]
            result[path].append(data)
        
    return result

if __name__ == "__main__":
    data = read_json("sample.json")
    flat = flatten(data)
    
    for key, value in flat.items():
        print(f"{key}: {value}")