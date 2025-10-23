class Document:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def print_preview(self):
        return f"{self.name} turi {self.species} formatda"
    
class WordDocument(Document):
    pass

class PdfDocument(Document):
    pass

r = WordDocument("Hujatlar", "txt")
r1 = PdfDocument("Fayl", "pdf")

print(r.print_preview())
print(r1.print_preview())