from fpdf import FPDF

name = input("Name: ")

class FinalPDF():
    def __init__(self, name):
        self._pdf = FPDF()
        self._pdf.add_page()

        self._pdf.set_font("Helvetica", "B", 40)
        self._pdf.cell(0, 50, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align="c")

        self._pdf.image("shirtificate.png", w=self._pdf.epw)
        self._pdf.set_text_color(255,255,255)
        self._pdf.set_font_size(23)
        self._pdf.text(x=60, y=130, text=f"{name} took CS50")

    def print(self, name):
        self._pdf.output(name)

pdf = FinalPDF(name)
pdf.print("shirtificate.pdf")
