
CAREER_SKILLS = {
    "Python Developer": [
        "Python", "SQL", "Git", "Flask", "APIs"
    ],
    "Data Analyst": [
        "Python", "SQL", "Excel", "Power BI", "Statistics"
    ],
    "Machine Learning Engineer": [
        "Python", "Statistics", "NumPy",
        "Pandas", "Scikit-learn", "SQL"
    ],
    "Web Developer": [
        "HTML", "CSS", "JavaScript", "Python", "Git"
    ]
}


def analyze_skills(career, student_skills):

    if career not in CAREER_SKILLS:
        raise ValueError("Unsupported career")

    required_skills = CAREER_SKILLS[career]

    student_skills = {
        skill.strip().casefold()
        for skill in student_skills.split(",")
        if skill.strip()
    }

    matched = [
        skill for skill in required_skills
        if skill.casefold() in student_skills
    ]

    missing = [
        skill for skill in required_skills
        if skill.casefold() not in student_skills
    ]

    percentage = round(
        len(matched) / len(required_skills) * 100, 2
    )

    return {
        "matched": matched,
        "missing": missing,
        "percentage": percentage
    }
