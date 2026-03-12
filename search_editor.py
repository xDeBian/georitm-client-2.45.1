import re

# Look for the object editor form template - specifically where "name" field and other fields are rendered
with open(r'static/js/statV.a9d594912cedc955c1c0.js', encoding='utf-8') as f:
    content = f.read()

# Search for win-stat-editor or the editor form template
patterns = [
    r'win-stat-editor',
    r'name.*StatEditor',
    r'StatEditor',
    r'StatEditorModule',
    r'1246',
    r'_activateSetup',
    r'processAndValidate',
    r'_executeRequests',
    r'settings_key',
    r'PHONE1',
    r'VRC_OWNER',
    r'shortDescription',
    r'ContractNumber',
    r'ContractDate',
    r'actionurl.*obj',
    r'saveSettings',
    r'serializeObject',
    r'settings.*save',
    r'save.*settings',
]

for p in patterns:
    matches = list(re.finditer(p, content))
    if matches:
        print(f'\n=== "{p}" ({len(matches)} matches) ===')
        m = matches[0]
        print(content[max(0,m.start()-200):m.end()+300])
        print()
