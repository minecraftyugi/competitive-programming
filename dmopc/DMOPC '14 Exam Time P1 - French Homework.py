verb = raw_input()
obj = raw_input()
out = [verb+"-tu", "", obj, "?"]

if obj[-1] == "e":
    out[1] = "la"
elif obj[-1] == "s":
    out[1] = "les"
else:
    out[1] = "le"

print " ".join(out)
