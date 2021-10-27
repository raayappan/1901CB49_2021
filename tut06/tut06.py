import re
import os
import shutil 
os.system('cls')

def regex_renamer(): 
    print("1. Breaking Bad")
    print("2. Game of Thrones")
    print("3. Lucifer")

    webseries_num = int(input("Enter the number of the web series that you wish to rename. 1/2/3: "))
    season_padding = int(input("Enter the Season Number Padding: "))
    episode_padding = int(input("Enter the Episode Number Padding: "))
    name_of_series = ""
    if webseries_num==1:
        name_of_series = "Breaking Bad"
    elif webseries_num ==2:
        name_of_series="Game of Thrones"
    else:
        name_of_series ="Lucifer"
       
    if name_of_series=='Breaking Bad':
        f= os.listdir(os.getcwd()+"\\wrong_srt\\"+name_of_series)
        for series in f:
            bb_sub= re.split(' ',series)
            info_bb=re.split('[se]',bb_sub[2])
            newpath=os.getcwd()
            shutil.copyfile(os.getcwd()+"\\wrong_srt\\"+name_of_series+"\\"+series,newpath+"\\corrected_srt\\Breaking Bad\\Breaking Bad - Season "+str('{:' + '0' + '>' + str(season_padding) + '}').format(info_bb[1])+" Episode "+str('{:' + '0' + '>' + str(episode_padding) + '}').format(info_bb[2])+"."+re.split('\.',bb_sub[3])[3]) 
    
    elif name_of_series=='Game of Thrones':
        f= os.listdir(os.getcwd()+"\\wrong_srt\\"+name_of_series)
        for series in f:
            got_main= re.split('.WEB',series)
            got_sub=re.split("-",got_main[0])
            info_got=re.split('[x]',got_sub[1])
            newpath=os.getcwd()
            shutil.copyfile(os.getcwd()+"\\wrong_srt\\"+name_of_series+"\\"+series,newpath+"\\corrected_srt\\Game of Thrones\\Game of Thrones - Season "+str('{:' + '0' + '>' + str(season_padding) + '}').format(info_got[0].strip())+" Episode "+str('{:' + '0' + '>' + str(episode_padding) + '}').format(info_got[1])+"-"+ got_sub[2] +"."+re.split('\.',got_main[1])[4])          
    
    elif name_of_series=='Lucifer':
        f= os.listdir(os.getcwd()+"\\wrong_srt\\"+name_of_series)
        for series in f:
            luc_main= re.split('.HDTV',series)
            luc_sub=re.split("-",luc_main[0])
            info_luc=re.split('[x]',luc_sub[1])
            newpath=os.getcwd()+"\\corrected_srt\\Lucifer\\Lucifer - Season "
            shutil.copyfile(os.getcwd()+"\\wrong_srt\\"+name_of_series+"\\"+series,newpath+str('{:' + '0' + '>' + str(season_padding) + '}').format(info_luc[0].strip())+" Episode "+str('{:' + '0' + '>' + str(episode_padding) + '}').format(info_luc[1])+"-"+luc_sub[2]+"."+re.split('\.',luc_main[1])[3])          

if os.path.isdir("corrected_srt") == 0:
    os.mkdir("corrected_srt")
if os.path.isdir("corrected_srt\Breaking Bad") == 0:
	os.mkdir("corrected_srt\Breaking Bad")	    
if os.path.isdir("corrected_srt\Game of Thrones") == 0:
    os.mkdir("corrected_srt\Game of Thrones")
if os.path.isdir("corrected_srt\Lucifer") == 0:
	os.mkdir("corrected_srt\Lucifer")

regex_renamer()