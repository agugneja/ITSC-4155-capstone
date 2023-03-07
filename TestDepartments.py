import pytest
from belk import *
from dataScience import *
from CCI import *
from ArtsAndArch import *
from LiberalScience.Writing import *
from LiberalScience.ReligiousStudies import *
from LiberalScience.Sociology import *
from LiberalScience.PsychologicalScience import *
from LiberalScience.PoliticalScience import *
from LiberalScience.Physics import *

# Testing if data science urls are equal to expected
@pytest.fixture()
def dataSciencUrls():
    dataObj = DataScience()
    return dataObj.facultyURLs

def test_dataScienceDepartment(dataSciencUrls):
    assert len(dataSciencUrls) == 94

# Testing if belk urls are equal to expected
@pytest.fixture()
def belkUrls():
    belkObj = Belk()
    return belkObj.facultyURLs

def test_BelkDepartment(belkUrls):
    assert len(belkUrls) == 205

# Testing if CCI urls are equal to expected
@pytest.fixture()
def CCIURLs():
    CCIObj = CCI()
    return CCIObj.facultyURLs

def test_ComputingInformatics(CCIURLs):
    assert len(CCIURLs) == 109

# Testing if arts and architecture urls are equal to expected
@pytest.fixture()
def artsAndArchURLs():
    artsAndArchObj = ArtsAndArch()
    return artsAndArchObj.facultyURLs

def test_ArtsAndArch(artsAndArchURLs):
    assert len(artsAndArchURLs) == 205

# Testing if Writing Lib Science urls are equal to expected
@pytest.fixture()
def WritingURLs():
    writingObj = Writing()
    return writingObj.facultyURLs

def test_WritingDepartment(WritingURLs):
    assert len(WritingURLs) == 36

# Testing if Religious Studies Lib Science urls are equal to expected
@pytest.fixture()
def ReligiousStudiesURLs():
    religiousObj = ReligiousStudies()
    return religiousObj.facultyURLs

def test_ReligiousStudies(ReligiousStudiesURLs):
    assert len(ReligiousStudiesURLs) == 45

# Testing if Sociology Lib Science urls are equal to expected
@pytest.fixture()
def SociologyURLs():
    sociologyObj = Sociology()
    return sociologyObj.facultyURLs

def test_SociologyDepartment(SociologyURLs):
    assert len(SociologyURLs) == 23

# Testing if Psychological Sciences Lib Science urls are equal to expected
@pytest.fixture()
def PsychologyURLs():
    psychologyObj = PsychologicalSciences()
    return psychologyObj.facultyURLs

def test_PsychologyDepartment(PsychologyURLs):
    assert len(PsychologyURLs) == 55

# Testing if Political Science Lib Science urls are equal to expected
@pytest.fixture()
def PoliticalScienceURLs():
    politicalObj = PoliticalScience()
    return politicalObj.facultyURLs

def test_PoliticalScienceDepartment(PoliticalScienceURLs):
    assert len(PoliticalScienceURLs) == 25

# Testing if Physics Lib Science urls are equal to expected
@pytest.fixture()
def PhysicsURLs():
    physicsObj = Physics()
    return physicsObj.facultyURLs

def test_PhysicsDepartment(PhysicsURLs):
    assert len(PhysicsURLs) == 32
