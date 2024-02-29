import json

class JsonFileManager:
    """Handles the simple loading and saving of json files"""
    
    @staticmethod
    def save_obj(path, obj):
        with open(path, 'w') as file:
            json.dump(obj, file, indent=4)
    
    @staticmethod
    def load_json(path):
        with open(path, 'r') as file:
            return json.load(file)
    
    @staticmethod
    def add_to_json(path, header: str, obj: dict):
        o = JsonFileManager.load(path)
        o[header] = obj
        JsonFileManager.save(path, obj)

    def __init__(self, json_path: str):
        self.__filename__ = json_path.split('/')[0]
        self.path = json_path
        
        self.obj = {}
        self.load()
        
    def load(self):
        with open(self.path, 'r') as file:
            self.obj = json.load(file)

    def save(self):
        with open(self.path, 'w') as file:
            json.dump(self.obj, file, indent=4)

    def find(self, filter: str) -> dict:
        return self.obj[filter]
    
    def find_in_obj(self, header: str, filter: str, value):
        obj = self.find(header)
        for k, v in obj:
            if filter == k or value == v:
                return obj[k]
            
    def set_key(self, header, key, value):
        self.obj[header][key] = value
        JsonFileManager.save_obj(self.path, self.obj)
    
    def add(self, header: str, obj: dict):
        self.load()
        self.obj[header] = obj
        self.save()