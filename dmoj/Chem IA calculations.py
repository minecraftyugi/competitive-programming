volume = input("Enter the boric acid volume in mL:")/1000.0
concentration = input("Enter the boric acid concentration:")
moles = volume * concentration
ratios = [1,2,4,2,5]

hclMol = ratios[1] / float(ratios[2]/moles)
hclVol = hclMol / 5.96
print "Litres of HCl needed:", hclVol
print "Millilitres of HCl needed:", hclVol * 1000

boraxMol = ratios[0] / float(ratios[2]/moles)
boraxMass = boraxMol * 381.42
print "Grams of borax needed:", boraxMass
