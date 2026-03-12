import sys, re
sys.stdout = open(sys.stdout.fileno(), mode="w", encoding="utf-8", buffering=1)

c = open("gridsVendor.a9d594912cedc955c1c0.js", "r", encoding="utf-8").read()
print("gridsVendor size:", len(c))

# Find the scroll drawing function "fe" (nScrollBody) - get 3000 chars context
m = re.search(r'nScrollBody', c)
if m:
    start = max(0, m.start() - 200)
    print("=== nScrollBody function context ===")
    print(c[start:start+4000])




