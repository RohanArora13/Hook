import urllib2
import time,os,shutil,re,sys
import zipfile

#the intro and info
print """
________________________________________________________________________________________________________

  _    _  ____   ____  _  __    _____ _   _  _____ _______       _      _      _      ______ _____  
 | |  | |/ __ \ / __ \| |/ /   |_   _| \ | |/ ____|__   __|/\   | |    | |    | |    |  ____|  __ \ 
 | |__| | |  | | |  | | ' /      | | |  \| | (___    | |  /  \  | |    | |    | |    | |__  | |__) |
 |  __  | |  | | |  | |  <       | | | . ` |\___ \   | | / /\ \ | |    | |    | |    |  __| |  _  / 
 | |  | | |__| | |__| | . \     _| |_| |\  |____) |  | |/ ____ \| |____| |____| |____| |____| | \ \ 
 |_|  |_|\____/ \____/|_|\_\   |_____|_| \_|_____/   |_/_/    \_\______|______|______|______|_|  \_\
                                                                                                    
                                                                                                    
      Made By - Rohan Arora                 More Info - https://github.com/RohanArora13/Hook

-disclaimer-
All This Mods Belong To Their Respective Owners. This Program only makes installation of this mods bit easier
More info about mods at:
https://www.gta5-mods.com/tools/script-hook-v
https://www.gta5-mods.com/tools/scripthookv-net
https://www.gta5-mods.com/scripts/simple-trainer-for-gtav

-Features-
-Installs latest Updates
-Fool Proof ! One Click Install
-An Open Source Project
________________________________________________________________________________________________________
"""
# Get url and version from a text host used for editing if files get updated
# hence this is for checking update
# very silly method but works for me which is made by me

try:
    response = urllib2.urlopen('http://freetexthost.com/gxgc5ymqh4')
    txt = response.read()
    t1=re.findall(r'<div id="contentsinner">(.*?)<div style="clear: both;"><!-- --></div>',txt,re.DOTALL)
    t1=t1[0]
    t1=t1.strip()
    t1=re.findall(r'&quot;(.*?)&quot;<br />',txt,re.DOTALL)

    url=t1[0].strip()
    SH=t1[1].strip()
    SHN=t1[2].strip()
    ST=t1[3].strip()
    try:
        url2=t1[4].strip()
    except:
        url2=None
except:
    print "cant reach download server ... Try to close firewall or check internet connection..."
    time.sleep(5)
    quit()


#print the version of script hooks
print"Script Hook V "+str(SH)+"             "+"Script Hook V .NET "+str(SHN)+"             "+" Simple Trainer "+str(ST)


print"________________________________________________________________________________________________________\n"


# get file path

me=os.getcwd() # exe directory


# asking and checking loaction of gta 5
global path
path=""
rar="data.zip" # downloaded zip name

def ask():
    global path
    no=""
    path=raw_input(u"GTA 5 directory loaction =")
    path=path.strip()
    print "Specifed = "+path
    try:
        for file in os.listdir(path):
            if file.endswith(".rpf"):
                no=(os.path.join(path, file))
    except:
        print "Please Enter Valid Location     Example -   C:\Program Files\Rockstar Games\Grand Theft Auto V"
        ask()
    if(len(no)>=1):
        print"\n"
        print "GTA 5 Is Installed! :) \n"
    else:
        print"GTA 5 Not Found In Given Directory ! :( "
        print"please Enter location Where .rdf files are installed \n"
        ask()

ask()


print "Downloading Zip Files..... \n"
# method 1 for downloading
try:
    t1=time.time()
    f = urllib2.urlopen(url)
    data = f.read()
    with open(rar, "wb") as code:
       code.write(data)
    t2=time.time()
    print "Time Taken ="+ str(t2-t1)+" sec\n"
except:
    print "can't reach server ... Try to close firewall or check internet connection..."
    time.sleep(5)
    quit()


if(os.path.getsize("data.zip")>=2000000):
    pass
else:
    if(url2!=None):
        url=url2
    else:
        pass


print "Extracting Files.... \n"

def D2():  # method 2 for downloading..
    print "Downloading Zip Files again..... \n"
    try:
        t1=time.time()
        f = urllib2.urlopen(url)
        data = f.read()
        with open(rar, "wb") as code:
           code.write(data)
        t2=time.time()
        print "Time Taken ="+ str(t2-t1)+" sec\n"
    except:
        print ""
    try:
        t1=time.time()
        f = urllib2.urlopen(url)
        data = f.read()
        with open(rar, "wb") as code:
           code.write(data)
        t2=time.time()
        print "Time Taken ="+ str(t2-t1)+" sec\n"
    except:
        print "can't reach server ... Try to close firewall or check internet connection..."
        time.sleep(5)
        quit()

# unzipping
try:
    zip_ref = zipfile.ZipFile(me+"\\"+rar, 'r')
    zip_ref.extractall(me+"\data")
    zip_ref.close()
except:
    print"Zip File not downloaded properly!"
    print"Trying To download again \n"
    D2()

print "Installing... \n"

# copying files to gta 5 folder
def copy():
    src=me+"\data"
    dest=path
    src_files = os.listdir(src)
    for file_name in src_files:
        full_file_name = os.path.join(src, file_name)
        if (os.path.isfile(full_file_name)):
            shutil.copy(full_file_name,dest)

copy()
print "Verifying Installation.... \n"

def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return True


if(find("ScriptHookVDotNet.asi",path) and find("ScriptHookV.dll",path) and
   find("dinput8.dll",path) ==True):
    os.remove(me+"\\"+rar)
    print "Finished... \n"
else:
    print "Trying Again..."
    copy()
time.sleep(5)

