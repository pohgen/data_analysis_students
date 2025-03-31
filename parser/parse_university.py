import requests
import csv
from bs4 import BeautifulSoup
from dataclasses import dataclass, astuple


URLS = [
    "https://prestonuniversity.ac.uk/students",
    "https://prestonuniversity.ac.uk/personals",
    "https://prestonuniversity.ac.uk/university",
    "https://prestonuniversity.ac.uk/parents",
]


@dataclass
class StudentAcademic:
    Student_ID: str
    Study_Hours_per_Week: float
    Extracurricular_Activities: bool
    Stress_Level_1_to_10: int
    Sleep_Hours_per_Night: float


@dataclass
class StudentFamily:
    Student_ID: str
    Internet_Access_at_Home: bool
    Parent_Education_Level: str
    Family_Income_Level: str


@dataclass
class StudentPersonal:
    Student_ID: str
    First_Name: str
    Last_Name: str
    Email: str
    Gender: str
    Age: int


@dataclass
class StudentPerformance:
    Student_ID: str
    Department: str
    Attendance_in_percent: float
    Midterm_Score: float
    Final_Score: float
    Assignments_Avg: float
    Quizzes_Avg: float
    Participation_Score: float
    Projects_Score: float
    Total_Score: float
    Grade: str


def extract_data(url: str) -> list:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    data = []

    if "students" in url:
        rows = soup.select("table tr")
        for row in rows[1:]:
            cols = row.find_all("td")
            data.append(StudentAcademic(*[col.text.strip() for col in cols]))

    elif "personals" in url:
        rows = soup.select("table tr")
        for row in rows[1:]:
            cols = row.find_all("td")
            data.append(StudentPersonal(*[col.text.strip() for col in cols]))

    elif "university" in url:
        rows = soup.select("table tr")
        for row in rows[1:]:
            cols = row.find_all("td")
            data.append(StudentPerformance(*[col.text.strip() for col in cols]))

    elif "parents" in url:
        rows = soup.select("table tr")
        for row in rows[1:]:
            cols = row.find_all("td")
            data.append(StudentFamily(*[col.text.strip() for col in cols]))

    return data


def save_to_csv(filename: str, data: list, headers: list) -> None:
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows([astuple(row) for row in data])


def main():
    academic_data = extract_data(URLS[0])
    personal_data = extract_data(URLS[1])
    performance_data = extract_data(URLS[2])
    family_data = extract_data(URLS[3])

    save_to_csv(
        "parsed_csv/Students_Home_Info_Dataset.csv",
        academic_data,
        [
            "Student_ID",
            "Study_Hours_per_Week",
            "Extracurricular_Activities",
            "Stress_Level_1_to_10",
            "Sleep_Hours_per_Night",
        ],
    )
    save_to_csv(
        "parsed_csv/Students_Personal_info_Dataset.csv",
        personal_data,
        ["Student_ID", "First_Name", "Last_Name", "Email", "Gender", "Age"],
    )
    save_to_csv(
        "parsed_csv/Students_Univercity_Dataset.csv",
        performance_data,
        [
            "Student_ID",
            "Department",
            "Attendance_in_percent",
            "Midterm_Score",
            "Final_Score",
            "Assignments_Avg",
            "Quizzes_Avg",
            "Participation_Score",
            "Projects_Score",
            "Total_Score",
            "Grade",
        ],
    )
    save_to_csv(
        "parsed_csv/Students_Parents_Info_Dataset.csv",
        family_data,
        [
            "Student_ID",
            "Internet_Access_at_Home",
            "Parent_Education_Level",
            "Family_Income_Level",
        ],
    )


if __name__ == "__main__":
    main()
