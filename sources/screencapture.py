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



try:

    user=getpass.getuser()

    fread_filename=os.path.abspath(os.sep)+"/users/"+user+"/AppData/Local/NDI/Application.Network.ScanConverter2.dat"
    app=os.path.abspath(os.sep) + "/Program Files/NDI/NDI 5 Tools/Screen Capture"

    os.chdir(app)


    if  True==True:


        if(len(sys.argv)%2==0):
            print("Syntax error. Check documentation for more details.")
            os._exit(0)

        else:

            for i in range(1,len(sys.argv),2):
                data[sys.argv[i]]=sys.argv[i+1]



        finaltxt="7CGN"


        if "-fr" in data:
            
            index = int(data['-fr'])
            finaltxt=finaltxt+pos1[index]+pos2[index]+null+null+pos5[index]+pos6[index]+null+null
          
        else:
            finaltxt=finaltxt+null+null+null+null+null+null+null+null



        if "-kvm" in data:
            index=int(data['-kvm'])
            if(index==0):
                finaltxt=finaltxt+null

            else:
                finaltxt=finaltxt+soh
        else:
            
            finaltxt=finaltxt+null



        if "-config" in data:

            
            items=data['-config'].split(',')

            val1=[]
            val2=[]
            val3=[]
            val4=[]
           
            bytes_val = int(items[0]).to_bytes(4, 'little')
            for i in bytes_val:
                val1.append(chr(i))


            bytes_val = int(items[1]).to_bytes(4,'little')
            for i in bytes_val:
                val2.append(chr(i))

            bytes_val = int(items[2]).to_bytes(4, 'little')
            for i in bytes_val:
                val3.append(chr(i))

            bytes_val = int(items[3]).to_bytes(4, 'little')
            for i in bytes_val:
                val4.append(chr(i))
                
            finaltxt=finaltxt+"".join(val1)+"".join(val2)+"".join(val3)+"".join(val4)
            
    
        else:
            
            finaltxt=finaltxt+"ã"+null+null+null+"€"+null+null+null+"r"+null+null+"€"+null+null


        if "-roi" in data:
            index=int(data['-roi'])
           
            if(index==0):
                finaltxt=finaltxt+null
            else:
                finaltxt=finaltxt+soh
        else:
            finaltxt=finaltxt+null




        if "-wvideo" in data:
            index=len(data['-wvideo'])
            bytes_val = index.to_bytes(4, 'little')
            val1=[]
            for i in bytes_val:
                val1.append(chr(i))
                
            finaltxt=finaltxt+"".join(val1)+data['-wvideo']
        
        else:
            finaltxt=finaltxt+""+null+null+null+"None"



        if "-wvideosetting" in data:
            index=len(data['-wvideosetting'])
            bytes_val = index.to_bytes(4, 'little')

            val1=[]
            for i in bytes_val:
                val1.append(chr(i))
                
            finaltxt=finaltxt+"".join(val1)+data['-wvideosetting']
        
        else:
            finaltxt=finaltxt+''+null+null+null+"Auto Detect"





        if "-waudio" in data:
            index=len(data['-waudio'])
            bytes_val = index.to_bytes(4, 'little')

            val1=[]
            for i in bytes_val:
                val1.append(chr(i))
            
            finaltxt=finaltxt+"".join(val1)+data['-waudio']
        
        else:
            finaltxt=finaltxt+null+null+null+null



        if "-as" in data:
            index=len(data['-as'])
            bytes_val = index.to_bytes(4, 'little')

            val1=[]
            for i in bytes_val:
                val1.append(chr(i))
                
            finaltxt=finaltxt+"".join(val1)+data['-as']
        
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
                    
        
        finaltxt=finaltxt+"7CGN"
  
        f= open(fread_filename,"w")
        f.write(finaltxt)
        f.close()
        print("launch: success")

        


    finalcmd='start "" "Application.Network.ScanConverter2.x64.exe"'
    os.system(finalcmd)
    os._exit(0)

except Exception  as e :
    print('Syntax error. Check documentation for more details.')
    
