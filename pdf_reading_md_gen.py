from pypdf import PdfReader

DEST_PATH_MD = "input.md"

reader = PdfReader("source.pdf")

pdf_text = ""

for i in range(len(reader.pages)):
    curr_page = reader.pages[i]
    text = curr_page.extract_text()
    pdf_text += text

pdf_text = pdf_text.replace("\\n", "\n")

with open(DEST_PATH_MD, "w") as md_f:
    md_f.write(pdf_text)
