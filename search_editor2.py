import re
import sys

# Use utf-8 output
sys.stdout.reconfigure(encoding='utf-8')

# Focus on finding the object settings save mechanism
# and the form template with "name" field
files = [
    (r'static/js/statV.a9d594912cedc955c1c0.js', 'statV'),
    (r'static/js/main.a9d594912cedc955c1c0.js', 'main'),
]

patterns = [
    r'VRC_OWNER',
    r'PHONE1',
    r'ContractNumber',
    r'ContractDate',
    r'"name".*input.*type.*text',
    r'input.*name.*name.*value',
    r'settings\[',
    r'settings\.',
    r'_saveSettings',
    r'saveSettings',
    r'settings.*post',
    r'objects/obj',
    r'obj/save',
    r'saveObj',
    r'_getFormData',
    r'getFormData',
    r'serializeForm',
    r'_processAndValidateData',
    r'_activateSetup',
    r'input.*name.*"name"',
    r'name.*placeholder.*objName',
    r'"name"\].*val\(',
    r'\[name=name\]',
]

for fpath, label in files:
    try:
        with open(fpath, encoding='utf-8') as f:
            content = f.read()
        for p in patterns:
            matches = list(re.finditer(p, content))
            if matches:
                print(f'\n=== {label}: "{p}" ({len(matches)} matches) ===', flush=True)
                m = matches[0]
                print(content[max(0,m.start()-150):m.end()+350])
                print()
    except Exception as e:
        print(f'Error {fpath}: {e}')
