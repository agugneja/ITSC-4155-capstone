#Jacob Nyborg
from fileinput import close
from CCI import *
from belk import *
from dataScience import *
from ArtsAndArch import *
from Engineering.Dean import *
from Engineering.Civil import *
from Engineering.Student_Development import *
from Engineering.Motorsports import *
from Engineering.MOSAIC import *
from Engineering.Mechanical import *
from Engineering.EPIC import *
from Engineering.Engineering_Tech import *
from Engineering.Electrical import *
from Engineering.Systems import *
from Education.k_12 import *
from Education.Reading_and_Elementary_Education import *
from Education.Special_Ed_and_Child_dev import *
from Education.counseling import *
from Education.Education_Leadership import *
from Education.School_and_Community_Partnerships import *
from LiberalScience.Anthropology import *
from LiberalScience.Biological_Sciences import *
from LiberalScience.Chemisty import *
from LiberalScience.Criminal_Justice_and_Criminology import *
from LiberalScience.English import *
from LiberalScience.Mathematics import *
from LiberalScience.Philosophy import *
from LiberalScience.History import *
from LiberalScience.GlobalStudies import *
from LiberalScience.Sociology import *
from LiberalScience.Writing import *
from LiberalScience.Geography import *
from LiberalScience.Communication import *
from LiberalScience.ReligiousStudies import *
from LiberalScience.PoliticalScience import *
from LiberalScience.Languages import *
from LiberalScience.Physics import *
from LiberalScience.AfricanaStudies import *
from LiberalScience.PsychologicalScience import *
from CHHS.Appl_Phys_Hlth_Clin_Sci_and_Kinesiology import *
from CHHS.CHHS import *
from CHHS.Public_Health_Sciences import *
from CHHS.School_of_Nursing import *
from CHHS.School_of_Social_Work import *

import csv

def main():

    # Engineering Sub Departments
    deanObj = Dean() #good
    civilObj = Civil() #good
    studentDevObj = Student_Development() #good
    motorsportsObj = Motorsports() #good
    mosaicObj = MOSAIC() #good
    mechanicalObj = Mechanical() #good
    epicObj = EPIC() #good
    engineeringTechObj = Engineering_Tech() #good
    electricalObj = Electrical() #good
    systemsObj = Systems() #good
    
    # Education Sub Departments
    k12Obj = K_12() #good
    readingObj = Reading_and_Elementary_Education() #good
    specialObj = Special_Ed_and_Child_dev() #good
    counselingObj = Counseling() #good
    leadershipObj = Education_Leadership() #good
    communityObj = School_and_Community_Partnerships() #good
    
    # Liberal Science Sub Departments
    anthropologyObj = Anthropology() #good but might be an issue
    biologyObj = Biological_Sciences() #good
    chemistryObj = Chemisty() #good
    criminalObj = Criminal_Justice_and_Criminology() #good (had to check which site it directed to)
    englishObj = English() #good 
    mathematicsObj = Mathematics() #good
    philoObj = Philosophy() #good
    historyObj = History() #good
    globalStudiesObj = GlobalStudies() #good
    sociologyObj = Sociology() #good
    writingObj = Writing() #good
    geographyObj = Geography() #good
    communicationObj = Communication() #good
    religiousObj = ReligiousStudies() #good
    politicalScienceObj = PoliticalScience() #good
    languageObj = Languages() #good
    physicsObj = Physics() #good
    africanaObj = AfricanaStudies() #good
    psychologicalObj = PsychologicalSciences() #good

    # CHHS Sub Departments
    kinsiologyObj = Appl_Phys_Hlth_Clin_Sci_and_Kinesiology() #good
    chhsObj = CHHS() #good but utf formatting might be wrong
    pubHealthObj = Public_Health_Sciences() #might need to add to it
    nursingObj = School_of_Nursing() #good
    socialObj = School_of_Social_Work() #good

    # Computing and Informatics Department
    compSciObj = CCI() # utf formatting might currently be wrong

    # Belk College Department
    belkObj = Belk() #good

    # Data Science Department
    dataScienceObj = DataScience() #good

    # Arts and Architecture Department
    artsObj = ArtsAndArch() #good

    profileList = [] # List for Profile Page Content
    urlList = [] # List for URLs to the faculty profiles

    #---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # All Directories(CCI and CHHS have utf formatting issues on windows)
    profileList = (compSciObj.profilePages + belkObj.profilePages + belkObj.profilePages + dataScienceObj.profilePages + artsObj.profilePages + deanObj.profiles + 
    civilObj.profiles + studentDevObj.profiles + motorsportsObj.profiles + mosaicObj.profiles + mechanicalObj.profiles + epicObj.profiles + engineeringTechObj.profiles +
    electricalObj.profiles + systemsObj.profiles + k12Obj.profiles + readingObj.profiles + specialObj.profiles + counselingObj.profiles + leadershipObj.profiles + 
    communityObj.profiles + anthropologyObj.profiles + biologyObj.profiles + chemistryObj.profiles + criminalObj.profiles + englishObj.profiles + mathematicsObj.profiles + 
    philoObj.profiles + historyObj.profiles + globalStudiesObj.profiles + sociologyObj.profiles + writingObj.profiles + geographyObj.profiles + communicationObj.profiles + 
    religiousObj.profiles + politicalScienceObj.profiles + languageObj.profiles + physicsObj.profiles + africanaObj.profiles + psychologicalObj.profiles + 
    kinsiologyObj.profiles + chhsObj.profiles + pubHealthObj.profiles + nursingObj.profiles + socialObj.profiles)

    urlList = (compSciObj.facultyURLs + belkObj.facultyURLs + belkObj.facultyURLs + dataScienceObj.facultyURLs + artsObj.facultyURLs + deanObj.facultyURLs + 
    civilObj.facultyURLs + studentDevObj.facultyURLs + motorsportsObj.facultyURLs + mosaicObj.facultyURLs + mechanicalObj.facultyURLs + epicObj.facultyURLs + 
    engineeringTechObj.facultyURLs + electricalObj.facultyURLs + systemsObj.facultyURLs + k12Obj.facultyURLs + readingObj.facultyURLs + specialObj.facultyURLs + 
    counselingObj.facultyURLs + leadershipObj.facultyURLs + communityObj.facultyURLs + anthropologyObj.facultyURLs + biologyObj.facultyURLs + chemistryObj.facultyURLs + 
    criminalObj.facultyURLs + englishObj.facultyURLs + mathematicsObj.facultyURLs + philoObj.facultyURLs + historyObj.facultyURLs + globalStudiesObj.facultyURLs + 
    sociologyObj.facultyURLs + writingObj.facultyURLs + geographyObj.facultyURLs + communicationObj.facultyURLs + religiousObj.facultyURLs + politicalScienceObj.facultyURLs + 
    languageObj.facultyURLs + physicsObj.facultyURLs + africanaObj.facultyURLs + psychologicalObj.facultyURLs + kinsiologyObj.facultyURLs + chhsObj.facultyURLs + 
    pubHealthObj.facultyURLs + nursingObj.facultyURLs + socialObj.facultyURLs) 
    #---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    # Loop to remove unnecessary URLs
    for i in range(len(urlList)-1,-1,-1):
        try:
            requests.get(urlList[i])
        except:
            print("Removed URL: ", urlList[i])
            del urlList[i]
    
    #site, type, action, title, excerpt, content, date, author, slug, status, menu-order, password, categories, tags, taxonomy-{name}, meta-{name}
    header = ["site", "type","action", "title", "excerpt", "content", "date", "author", "slug", "status", "menu-order", "password", 
    "categories", "tags", "taxonomy-{name}", "meta-{name}"]

    f = open("post.csv", "a", newline="", encoding='utf-8')
    
    writer = csv.writer(f)
    writer.writerow(header)

    # Writes to CSV based on specfic formatting defined in header list
    for i in range(len(profileList)):
        listy = [urlList[i], "post", "update", profileList[i]["Title"], "", profileList[i]["Content"], "", "", "", "" , ""]
        writer.writerow(listy)
    
    f.close()

if __name__ == '__main__':
    main()
