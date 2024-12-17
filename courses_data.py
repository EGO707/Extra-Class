# data mainly used in search results 
COURSES = {
    'cs': {
        1: ['Programming for Problem Solving', 'Mathematics I'],
        2: ['Mathematics 2', 'Fundamental of Mechanical engineering'],
        3: ['Data Structures', 'Mathematics 3', 'Digital Electronics'],
        # Add more semesters
    },
    'electronics': {
        1: ['Basic Electronics', 'Physics'],
        2: ['Mathematics ll', 'Fundamental of electrical engineering'],
        3: ['Digital system design', 'Electronic Devices'],
        # Add more semesters
    },
    'electrical': {
        1: ['Soft skills', 'Mathematics I'],
        2: ['Environment and ecology'],
        3: ['Electromagnetic Theory', 'Cybersecurity'],
        # Add more semesters
    }
}

PDF_MAPPING = {}

# Add "data_structures.pdf" for every subject
for course in COURSES.values():
    for sem_subjects in course.values():
        for subject in sem_subjects:
            PDF_MAPPING[subject] = "example.pdf"
