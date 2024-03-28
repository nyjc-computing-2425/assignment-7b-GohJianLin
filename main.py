# Built-in imports
import math

# Your code below
GRADE = {}
for num in range(101):
    if num >= 70:
        GRADE[num] = 'A'
    elif num <70 and num >= 60:
        GRADE[num] = 'B'
    elif num <60 and num >= 55:
        GRADE[num] = 'C'
    elif num <55 and num >= 50:
        GRADE[num] = 'D'
    elif num <50 and num >= 45:
        GRADE[num] = 'E'
    elif num <45 and num >= 40:
        GRADE[num] = 'S'
    else:
        GRADE[num] = 'U'
def read_testscores(filename):
    """
    reads data from filename and returns list of dicts with class, name, overall marks and grade of each student

    Parameters
    ----------
    filename
        name of the file

    Returns
    -------
    flist
        list containing class, name, overall score and grade of the student

    Example:
    >>> studentdata = read_testscores('testscores.csv')
    >>> studentdata[0]['class']
    'Class1'
    >>> studentdata[0]['name']
    'Student1'
    >>> studentdata[0]['overall']
    51
    >>> studentdata[0]['grade']
    'D'
    """
    flist = []
    with open(filename, 'r') as file:
        first_line = file.readline()
        for i in file:
            fdict = {}
            if i != first_line:
                ilist = i.strip().split(',')
                fdict['class'] = ilist[0]
                fdict['name'] = ilist[1]
                ftuple = (int(ilist[2]),int(ilist[3]),int(ilist[4]),int(ilist[5]))
                fdict['overall'] = math.ceil(ftuple[0]/30 * 15 + ftuple[1]/40 *30 + ftuple[2]/80 * 35 + ftuple[3]/30 * 20)
                fdict['grade'] = GRADE[fdict['overall']]
                flist.append(fdict)
    return flist
def analyze_grades(studentdata):#studentdata is the list of dicts
    """
    takes student data and returns a dict representing count of each grade

    Parameters
    ----------
    studentdata
        list of dicts consisting class, name, overall score and grade of each student

    Return
    ------
    classdict
        dict of dicts consisting of classes and number of each grade in each class

    Example:
    >>> analysis = analyze_grades(studentdata)
    >>> analysis['Class1']['A']
    4
    >>> analysis['Class18']['U']
    0
    """
    classdict = {}
    for classes in classdict:
        gradedict = {}
        for grades in studentdata:#for the grades          
            if grades['grade'] not in gradedict:
                gradedict[grades['grade']] = 1
            else:
                gradedict[grades['grade']] += 1
            classdict[grades['class']] = gradedict
    return classdict