import json

with open('resources/settings.json') as f:
    settingsFile = f.read()
settings = json.loads(settingsFile)
imageClass = settings.get('imageClass')
print(imageClass)
