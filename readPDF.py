from pypdf import PdfReader

reader = PdfReader("LG 유플러스 이메일 청구서입니다_.pdf")
page = reader.pages[0]
print(page.extract_text())