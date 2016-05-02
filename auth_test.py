with open('authz_test_input.txt', 'r+') as input_file:
        content = input_file.read()
        input_file.seek(0)
        input_file.truncate()
        input_file.write(content.replace("is not a valid member. Please remove the user from the 'developers' group."," "))


with open('authz_test_input.txt', 'r+') as input_file:
        content = input_file.read()
        input_file.seek(0)
        input_file.truncate()
        input_file.write(content.replace("is not a valid member. Please remove the user from the 'scm' group."," "))

    
with open('authz_test_input.txt', 'r+') as input_file:
        content = input_file.read()
        input_file.seek(0)
        input_file.truncate()
        input_file.write(content.replace("is not a valid member. Please remove the user from the '/' path."," "))

f = open('authz_test_input.txt', 'r')
lines = f.readlines()
mystr = '\t'.join([line.strip() for line in lines])
#print mystr

l = mystr.split( )
#print l

words = [x.replace('\t',' ') for x in l]
#print words
to_be_removed = [x.replace("' '","','") for x in words]
#print to_be_removed

authz_file_ids = "sp4243,sn041p,kk457h,sk7560,pr345p,sv183w,st5374,ss6105,gc4993,ga668p,nm502p,nj547s,st4239,up1306,st660k,ss213g"
#authz_file_ids = "kp5201,br102r,hs9071,rt523a,am143p,vm836p,sj851v,ns836p,ak0291,kp538k,ys890g,bp538k,yr345u,bp097h,vl1320,pa4929,rx128j,pa3339,nb8528,dd200d,dd213k,tj327w,ps310j,df1061,tj327w,sp411t,rc2101,ns1557,ec4614,sj851v,sp717x,Ar4921,Rs870v,br102r,ps820v,bp637q"
#authz_file_ids = "pa9491,am143p,sp717x,rx128j,ks332e,ns836p,pa4929,am143p,kv538k,ps310j,dd213k,pa3339,tj327w,ps1320,sp411t,ns1557,ec4614,ab384u,br102r,as494f,vr6363,py543u,Zk1540,ps820v,pe900p"
#authz_file_ids = "mf636n,pa9491,hs9071,rt523a,am143p,vm836p,sj851v,ns836p,cd3825,yr345u,ks332e,bp097h,vl1320,pa4929,pa9491,rx128j,ps310j,ec4614,ps1320,dd213k,tj327w,sp411t,ns1557,sb577a,Ar4921,py543u,sp717x,vr6363,nn9928,mm893w,br102r,as494f,ps820v,pe900p"
authz_file_ids = authz_file_ids.split(',')
#print authz_file_ids


z = [x.replace("'","") for x in to_be_removed]
#print z
    
list_to_be_retained = [x for x in authz_file_ids if x not in z]
print list_to_be_retained












