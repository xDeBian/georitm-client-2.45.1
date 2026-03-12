import re

files = [
    r'static/js/statV.a9d594912cedc955c1c0.js',
    r'static/js/main.a9d594912cedc955c1c0.js',
    r'static/js/commonViewsV.a9d594912cedc955c1c0.js',
]

patterns = ['pop-obj-card', 'objName', 'win-stat-editor', 'StatEditor', 'name.*obj.*input', 'ObjName', 'obj_name', 'objectName']

for fpath in files:
    try:
        with open(fpath, encoding='utf-8') as f:
            content = f.read()
        for p in patterns:
            matches = list(re.finditer(p, content))
            if matches:
                print(f'\n=== {fpath}: "{p}" ({len(matches)} matches) ===')
                m = matches[0]
                print(content[max(0,m.start()-300):m.end()+400])
    except Exception as e:
        print(f'Error {fpath}: {e}')
