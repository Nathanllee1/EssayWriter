import os
import docx
import docx2txt
#text = []


def getter(file):
    '''
    doc = docx.Document(files)
    fullText = []
    for para in doc.paragraphs:
        #txt = para.text.encode('ascii', 'ignore')
        fullText.append(str(para))
    return '\n'.join(fullText)
    '''
    return docx2txt.process(file)

text = []

for files in os.listdir(r"C:/Users/Nathan Lee/Workspace/EssayWriter/trainingdata"):
    text.append(getter(files))

file = open("training_data.txt", "w")
text = ''.join(text)
file.write(text)
file.close()
