dwarfs = []
for _ in range(9):
	dwarfs.append(int(input()))

dwarfs.sort()
rest = sum(dwarfs) - 100

no_dwarf = []
for i,a in enumerate(dwarfs):
	if len(no_dwarf)==2:
		break

	for b in dwarfs[i+1:]:
		if a+b == rest:
			no_dwarf.append(a)
			no_dwarf.append(b)
			break

for dwarf in dwarfs:
	if dwarf in no_dwarf:
		continue
	print(dwarf)