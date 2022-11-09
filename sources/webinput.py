import json
import os
import getpass
import sys
import time

c_nul="\u0000"
c_del="\u007F"
c_stx="\u0002"
c_soh="\u0001"
c_eot="\u0004"
c_ack="\u0006"
c_a="\u00E0"
c_ytwodot="\u00FF"
c_d ="\u00D0"
c_otitle="\u00F2"
c_otwodot="\u00F6"
c_degree="\u00B0"
c_ititle="\u00EC"

data=dict()


try:

    user=getpass.getuser()

    fread_filename=os.path.abspath(os.sep)+"/users/"+user+"/AppData/Local/NDI/Application.Network.WebCam.dat"
    app=os.path.abspath(os.sep) + "/Program Files/NDI/NDI 5 Tools/Webcam Input/"

    os.chdir(app)

    #print(os.getcwd())

    if  True==True:


        if(len(sys.argv)%2==0):
            print("Syntax error. Check documentation for more details.")
            os._exit(0)

        else:

            for i in range(1,len(sys.argv),2):
                data[sys.argv[i]]=sys.argv[i+1]



        finaltxt="NTKWF000"


        if "-src" in data:

            finaltxt=finaltxt+chr(len(data['-src']))+c_nul+c_nul+c_nul+data['-src']
            
            
        else:
            finaltxt=finaltxt+c_nul+c_nul+c_nul+c_nul

            

        if "-al" in data:

            value= int(data['-al'])

            if(value==0):
                finaltxt=finaltxt+c_ytwodot+c_ytwodot+c_ytwodot+c_del

            elif(value==1):
                finaltxt=finaltxt+c_nul+c_nul+c_nul+c_nul+c_nul

            elif (value==2):
                finaltxt=finaltxt+c_otwodot+c_ytwodot+c_ytwodot+c_ytwodot

            elif(value==3):
                finaltxt=finaltxt+c_otitle+c_ytwodot+c_ytwodot+c_ytwodot

            elif(value==4):
                finaltxt=finaltxt+c_ititle+c_ytwodot+c_ytwodot+c_ytwodot

            elif (value==5):
                finaltxt=finaltxt+c_degree+c_ytwodot+c_ytwodot+c_ytwodot

        else:
            finaltxt=finaltxt+c_ytwodot+c_ytwodot+c_ytwodot+c_del






        if "-ac" in data:

            value= int(data['-ac'])

            if(value==0):
                finaltxt=finaltxt+c_ytwodot+c_ytwodot+c_ytwodot+c_ytwodot

            elif(value==1):
                finaltxt=finaltxt+c_nul+c_nul+c_nul+c_nul

            elif (value==2):
                finaltxt=finaltxt+c_stx+c_nul+c_nul+c_nul

            elif(value==3):
                finaltxt=finaltxt+c_eot+c_nul+c_nul+c_nul

            elif(value==4):
                finaltxt=finaltxt+c_ack+c_nul+c_nul+c_nul


        else:
            finaltxt=finaltxt+c_ytwodot+c_ytwodot+c_ytwodot+c_ytwodot





        if "-v" in data:

            value= int(data['-v'])

            if(value==0):
                finaltxt=finaltxt+c_nul+c_nul+c_nul+c_nul

            elif(value==1):
                finaltxt=finaltxt+"8"+c_eot+c_nul+c_nul

            elif (value==2):
                finaltxt=finaltxt+c_d+c_stx+c_nul+c_nul

            elif(value==3):
                finaltxt=finaltxt+c_a+c_soh+c_nul+c_nul


        else:
            finaltxt=finaltxt+c_d+c_stx+c_nul+c_nul

       
        finaltxt=finaltxt+c_soh+c_soh

       # print(finaltxt)
        f= open(fread_filename,"w" )
        f.write(finaltxt)
        f.close()
        print("launch: success")

        
   



    finalcmd='start "" "Webcam Input.exe"'
    os.system(finalcmd)
    os._exit(0)

except Exception  as e :
    print('Syntax error. Check documentation for more details.')
    
