def feldolgoz(outp,mit):
    tomb=mit.split()
    kihagy=0;
    for item in tomb:
        print(item)
        print("kovi")
        if kihagy==0:
            if(item=="C"):
                kihagy=2
            else:
                if (item!="M") and (item!="L") and (item!="z"):
                    outp.write("        tmp.push([%s]);\n" % (item,))
        else:
            #we skip this item
                kihagy-=1
inp=open("duna.txt","r")
outp=open("torolj.txt","w")
for line in inp:
    outp.write("        tmp=Array();\n");
    feldolgoz(outp,line);
    outp.write("    duna.push(tmp);\n");
outp.close();
inp.close();
