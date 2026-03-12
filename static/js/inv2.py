import re, sys
sys.stdout = open(sys.stdout.fileno(), mode="w", encoding="utf-8", buffering=1)

mj = open("main.a9d594912cedc955c1c0.js","r",encoding="utf-8").read()

# 1. modules.stat context
for pos in [764281, 813583]:
    print(f"=== modules.stat @{pos} ===")
    print(repr(mj[pos-200:pos+400]))
    print()

# 2. appready + initBoundsWatching — full block to insert after
pos = 778575
print("=== appready block ===")
print(repr(mj[pos-50:pos+500]))
print()

# 3. Find main settings navbar template with startWithDashboard
pos2 = 74131
print("=== settings template @74131 ===")
print(repr(mj[pos2-800:pos2+400]))
print()

# 4. Find getBaseUrl
hits = [m.start() for m in re.finditer("getBaseUrl", mj)]
print("getBaseUrl hits:", hits[:3])
if hits:
    print(repr(mj[hits[0]-50:hits[0]+200]))
    print()

# 5. Find hasMobile / hasModule / isStat
for kw in ["hasMobile", "hasModule", "hasStat"]:
    hits2 = [m.start() for m in re.finditer(kw, mj)]
    print(f"{kw} hits:", hits2[:3])
    if hits2:
        print(repr(mj[hits2[0]-30:hits2[0]+200]))
    print()

# 6. Find the navbar HTML in index.html (new project)
idx = open("C:/Users/xDeBian/Desktop/georitm-client-2.45.1/index.html","r",encoding="utf-8").read()
m = re.search(r"navbar[^\n]{0,500}", idx)
print("index.html navbar:", repr(m.group()[:400]) if m else "not found")
print()
m2 = re.search(r"main-hdr[^\n]{0,500}", idx)
print("index.html main-hdr:", repr(m2.group()[:400]) if m2 else "not found")
