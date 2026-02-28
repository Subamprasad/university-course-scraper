import requests
from bs4 import BeautifulSoup
import pandas as pd

# -----------------------------
# Helper function to clean text
# -----------------------------
def clean_text(text):
    if text:
        return text.strip()
    return "Not Available"

# -----------------------------
# Universities List
# -----------------------------
universities = [
    {
        "university_id": 1,
        "university_name": "Harvard University",
        "country": "USA",
        "city": "Cambridge",
        "website": "https://www.harvard.edu",
        "courses_url": "https://pll.harvard.edu/catalog"
    },
    {
        "university_id": 2,
        "university_name": "Stanford University",
        "country": "USA",
        "city": "Stanford",
        "website": "https://www.stanford.edu",
        "courses_url": "https://online.stanford.edu/courses"
    },
    {
        "university_id": 3,
        "university_name": "University of Oxford",
        "country": "UK",
        "city": "Oxford",
        "website": "https://www.ox.ac.uk",
        "courses_url": "https://www.ox.ac.uk/admissions/graduate/courses"
    },
    {
        "university_id": 4,
        "university_name": "MIT",
        "country": "USA",
        "city": "Cambridge",
        "website": "https://www.mit.edu",
        "courses_url": "https://catalog.mit.edu/degree-charts/"
    },
    {
        "university_id": 5,
        "university_name": "University of Toronto",
        "country": "Canada",
        "city": "Toronto",
        "website": "https://www.utoronto.ca",
        "courses_url": "https://future.utoronto.ca/academics/undergraduate-programs/"
    }
]

courses_data = []
course_id_counter = 1

# -----------------------------
# Scrape Courses
# -----------------------------
for uni in universities:
    try:
        response = requests.get(uni["courses_url"], timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract course titles (generic approach)
        course_titles = soup.find_all(["h2", "h3", "a"])

        count = 0

        for tag in course_titles:
            title = clean_text(tag.get_text())

            if title and len(title) > 5:
                courses_data.append({
                    "course_id": course_id_counter,
                    "university_id": uni["university_id"],
                    "course_name": title,
                    "level": "Not Available",
                    "discipline": "Not Available",
                    "duration": "Not Available",
                    "fees": "Not Available",
                    "eligibility": "Not Available"
                })

                course_id_counter += 1
                count += 1

            if count >= 5:
                break

    except Exception as e:
        print(f"Error scraping {uni['university_name']}: {e}")

# -----------------------------
# Create DataFrames
# -----------------------------
universities_df = pd.DataFrame(universities).drop(columns=["courses_url"])
courses_df = pd.DataFrame(courses_data)

# Remove duplicates
courses_df = courses_df.drop_duplicates()

# -----------------------------
# Export to Excel
# -----------------------------
with pd.ExcelWriter("university_course_data.xlsx") as writer:
    universities_df.to_excel(writer, sheet_name="Universities", index=False)
    courses_df.to_excel(writer, sheet_name="Courses", index=False)

print("Assignment completed successfully!")
print("Excel file created: university_course_data.xlsx")