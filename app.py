import PyPDF2
import streamlit as st
import pandas as pd

def extract_pdf_content(pdf_path):
    data = []
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page_num in range(3):
            page = reader.pages[page_num]
            text = page.extract_text()
            # Parse the extracted text to get the data
            lines = text.split("\n")
            for line in lines:
                # Assuming each line follows the format: "ID Name Group Seat Block Hall Period"
                elements = line.split()
                if len(elements) == 16:  # Check if line has all required elements
                    data.append({
                        "رقم القيد": elements[0],
                        "الاسم": " ".join(elements[1:5]),
                        "المجموعة": elements[6],
                        "رقم المقعد": elements[7],
                        "رقم القاطع": elements[8:10],
                        "المدرج": elements[11:13],
                        "مكان المدرج": elements[14:15],
                        "الفترة": elements[15]  # Adjusted index to 7
                    })
                if len(elements) ==15:  # Check if line has all required elements
                    data.append({
                        "رقم القيد": elements[0],
                        "الاسم": " ".join(elements[1:5]),
                        "المجموعة": elements[5],
                        "رقم المقعد": elements[6],
                        "رقم القاطع": elements[8],
                        "المدرج": elements[10:12],
                        "مكان المدرج": elements[13],
                        "الفترة": elements[14]  # Adjusted index to 7
                    })
                if len(elements) ==17:  # Check if line has all required elements
                    data.append({
                        "رقم القيد": elements[0],
                        "الاسم": " ".join(elements[1:6]),
                        "المجموعة": elements[7],
                        "رقم المقعد": elements[8],
                        "رقم القاطع": elements[9:11],
                        "المدرج": elements[10:12],
                        "مكان المدرج": elements[15],
                        "الفترة": elements[16]  # Adjusted index to 7
                    })
    return data

def search_student_by_id(student_id, df):
    student_data = df[df["رقم القيد"] == str(student_id)]
    return student_data

def main():
    st.title("Search for Student Data")
    st.write("Enter your student ID:")
    student_id = st.text_input("Student ID", "")

    if st.button("Search"):
        if student_id:
            student_data = search_student_by_id(student_id, df)

            if not student_data.empty:
                st.write("Student Data:")
                st.write(student_data)
            else:
                st.write("Student ID not found!")

if __name__ == "__main__":
    pdf_path = r"C:\Users\seyf2\Downloads\Documents\idnum.pdf"  # Use raw string literal
    data = extract_pdf_content(pdf_path)
    df = pd.DataFrame(data)
    main()
