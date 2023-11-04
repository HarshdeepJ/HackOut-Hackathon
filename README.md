# HackOut-Hackathon
All the codes were written and pipelined during the course of the hackathon.

# Project Description
### Aim : To generate a summarized infographics from the given pdf to enhance the visual experience of the user.
### Problem : Texts that are visually unattractive and difficult to read can be transformed into a more interactive and concise format, making it easier for the reader to grasp and providing motivation for engagement. This approach not only enhances readability but also proves highly valuable for revision purposes.
### Working : The user inputs a pdf which is converted into a readable text format using the pdfminer library (https://pypi.org/project/pdfminer/). It is then pre-processed using NLTK and given to the PaLM API (https://developers.generativeai.google/) for generating the required features of the infographics using tailored promts to fit the needs. Once the features are extracted from the text, they are then fit onto a premade .docx template file using the docxtpl library (https://pypi.org/project/docxtpl/). This template is standard for the output. A final .docx file is generated and is converted into .pdf or .jpg format. 

