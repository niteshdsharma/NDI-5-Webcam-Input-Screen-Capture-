import json
import os
import getpass
import sys
import time
import struct
from decimal import Decimal



data=dict()

null="\u0000"
a_curly='ã'
soh="\u0001"
c_e="€"


pos1=[null,'`','`','P','0','0','¨']
pos2=[null,'ê','ê','Ã','u','u','a']
pos5=[null,'è','é','è','è','é','è']
pos6=[null,'','','','','','']


res1=[null," ","8","Ð","Ð"]
res2=[null,"","","",""]
res3=[null,null,null,null,null]
res4=[null,null,null,null,null]


bq1=[null,null,null,null]
bq2=[null,null,null,null]
bq3=[null,"€",null,"€"]
bq4=["@","?","?",">"]



try:

    user=getpass.getuser()

    fread_filename=os.path.abspath(os.sep)+"/users/"+user+"/AppData/Local/NDI/Application.Network.ScanConverterHX.dat"
    app=os.path.abspath(os.sep) + "/Program Files/NDI/NDI 5 Tools/Screen Capture"

    os.chdir(app)

    if  True==True:


        if(len(sys.argv)%2==0):
            print("Syntax error. Check documentation for more details.")
            os._exit(0)

        else:

            for i in range(1,len(sys.argv),2):
                data[sys.argv[i]]=sys.argv[i+1]



        finaltxt="2CSN"


        if "-fr" in data:
            
            index = int(data['-fr'])
            finaltxt=finaltxt+pos1[index]+pos2[index]+null+null+pos5[index]+pos6[index]+null+null
          
        else:
            finaltxt=finaltxt+null+null+null+null+null+null+null+null



        if "-res" in data:
            
            index = int(data['-res'])
            finaltxt=finaltxt+res1[index]+res2[index]+res3[index]+res4[index]
          
        else:
            finaltxt=finaltxt+null+null+null+null


        if "-bandq" in data:
            
            index = int(data['-bandq'])
            finaltxt=finaltxt+bq1[index]+bq2[index]+bq3[index]+bq4[index]          
        else:
            finaltxt=finaltxt+null+null+null+null



        if "-mouse" in data:
            index=int(data['-mouse'])
            if(index==0):
                finaltxt=finaltxt+null

            else:
                finaltxt=finaltxt+soh
        else:
            
            finaltxt=finaltxt+null




        if "-kvm" in data:
            index=int(data['-kvm'])
            if(index==0):
                finaltxt=finaltxt+null

            else:
                finaltxt=finaltxt+soh
        else:
            
            finaltxt=finaltxt+null


        if "-hevc" in data:
            index=int(data['-hevc'])
            if(index==0):
                finaltxt=finaltxt+null

            else:
                finaltxt=finaltxt+soh
        else:
            
            finaltxt=finaltxt+null



        if "-audio" in data:
            index=len(data['-audio'])
            bytes_val = index.to_bytes(4, 'little')
            val1=[]
            for i in bytes_val:
                val1.append(chr(i))
                
            finaltxt=finaltxt+"".join(val1)+data['-audio']
        
        else:
            finaltxt=finaltxt+""+null+null+null+"Default Audio Output"




        
        finaltxt=finaltxt+"2CSN"
        #print(finaltxt)
        f= open(fread_filename,"w")
        f.write(finaltxt)
        f.close()
        print("launch: success")

        


    finalcmd='start "" "Application.Network.ScanConverterHX.x64.exe"'
    os.system(finalcmd)
    os._exit(0)

except Exception  as e :
    print('Syntax error. Check documentation for more details.')
    
