# 🎓 University & Course Data Scraper

## 📌 Internship Assignment Submission  
**Position:** AI/ML & Web Scraping Data Entry Intern (Remote)

---

## 🎯 Project Objective

This project automates the extraction of university and course data from official university websites using Python.

The collected data is cleaned, structured, and exported into a professional Excel file while maintaining relational integrity between universities and their courses.

---

## 🚀 Features

- Automated web scraping using Python
- Data cleaning and formatting
- Unique ID generation for relational mapping
- Duplicate record removal
- Missing value handling
- Structured Excel output with two sheets
- Professional project organization

---

## 🛠 Technologies Used

- Python
- requests
- BeautifulSoup
- pandas
- openpyxl
- Git & GitHub

---

## 📂 Output File Structure

The generated Excel file:

`university_course_data.xlsx`

### Sheet 1: Universities

| Column Name       | Description |
|------------------|------------|
| university_id    | Unique identifier |
| university_name  | Official university name |
| country          | Country |
| city             | City |
| website          | Official website URL |

---

### Sheet 2: Courses

| Column Name     | Description |
|----------------|------------|
| course_id      | Unique identifier |
| university_id  | Foreign key linking to university |
| course_name    | Name of the course |
| level          | Degree level |
| discipline     | Field of study |
| duration       | Course duration |
| fees           | Tuition fees |
| eligibility    | Admission requirements |

---

## 🔗 Relational Integrity

- Each course is linked to its university using `university_id`.
- All IDs are unique.
- No duplicate entries.
- Missing values handled as "Not Available".

---



