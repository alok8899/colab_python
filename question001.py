list1=[[['Hydrabad','alok','balasore_odisha'],['Hydrabad','ashok','ghghghgh'],['banglore','dipti','cccgcg'],['mum','rasmi','bbs']]]
finallist_loc=[]
finallist_name=[]
finallist_address=[]

for subindex in list1[0]:
	finallist_loc.append(subindex[0])


	finallist_name.append(subindex[1])


	finallist_address.append(subindex[2])


print("the data in tabular form")
print("\n\tjob_loc\t\tname\t\taddress")
print("\t-------\t\t--------\t--------")
for indexnoloc,indexnoname,indexnoaddr in zip(finallist_loc,finallist_name,finallist_address):

	print("\t",indexnoloc,"\t",indexnoname,"\t\t",indexnoaddr)

