import json

class JsonFile:
    def __init__(self, filename):
        self.filename = filename

    def save(self, data):
        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=2)  # Indentación para una mejor legibilidad

    def read(self):
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []
        return data
     
    def find(self, attribute, value):
        try:
            with open(self.filename, 'r') as file:
                datas = json.load(file)
                data = [item for item in datas if item.get(attribute) == value]
        except FileNotFoundError:
            data = []
        return data

    def delete(self, item_to_delete, key):
        items = self.read()
        updated_items = [item for item in items if item[key] != item_to_delete[key]]
        self.save(updated_items)  # Utiliza el método save para guardar los datos actualizados
