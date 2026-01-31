import json

def read_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
    
def flatten(data, path="", result=None):
    if result is None:
        result = {}
        
    if isinstance(data, dict):
        for key, value in data.items():
            new_path = f"{path}.{key}" if path else key
            if (type(value) == list):
                result[new_path] = value[0]
                for i in range(len(value) - 1):
                    result[new_path] = value[i]
            else:
                result[new_path] = value
            
            flatten(value, new_path, result)
            
    elif isinstance(data, list):
        new_path = f"{path}[]"
        for item in data:
            flatten(item, new_path, result)
            
    else:
        result[path] = data
        
    return result

if __name__ == "__main__":
    data = read_json("sample.json")
    flat = flatten(data)
    
    for key, value in flat.items():
        print(f"{key}: {value}")