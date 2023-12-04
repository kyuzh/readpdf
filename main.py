import PyPDF2
import re
import csv

list_pages = [[55,57], [86,91], [123,127], [159,163],[185,190],[210,212],[249,254],[277,281],[304,308],[323,325],[366,371], [425,430], [446,450], [483,488]]
list_lettre =["A", "B", "C", "D", "E"]
list_question = []
list_answer = []
for lettre in list_lettre:
    list_answer.append("\n"+lettre+"\n.")
for i in range(1,21):
    list_question.append("\n" + str(i) + "\n.")

list_delimiters = list_question + list_answer
print(list_delimiters)
# creating a pdf reader object
file_path = r"C:\Users\MAO\Downloads\AWS Certified Solutions Architect Official Study Guide - PDF Room.pdf"
reader = PyPDF2.PdfReader(file_path )

number = 0
# print the text of the first page
for pages in list_pages:
    number += 1
    text = ""
    for page in range(pages[0], pages[1]):
        text = text + reader.pages[page].extract_text()

    for delimiter in list_question:
        text = text.replace(delimiter, "\ndelimiter_question\n")

    text = text.split("\ndelimiter_question\n")
    if 'Review\tQuestions' in text:
        text.remove('Review\tQuestions')


    list = []
    for question in text:
        for delimiter in list_answer:
            question = question.replace(delimiter, "\ndelimiter_answer\n")
        list.append(question.split("\ndelimiter_answer\n"))

    print(list[0])
    for element in list[0]:
        print(element)


    with open("aws" + str(number) + ".csv", "w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL, delimiter=",")
        writer.writerows(list)
