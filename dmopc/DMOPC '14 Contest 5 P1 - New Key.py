a="0123456789ABCDEFGHIJKLMNOP"
print raw_input().translate(__import__("string").maketrans(a,a[9:]+"QRSTUVWXY"))
