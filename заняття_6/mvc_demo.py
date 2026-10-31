class BooksModel:
    def __init__(self):
        self.books = []

    def add_book(self, title):
        title = title.strip()
        if not title:
            raise ValueError("Порожня назва")
        self.books.append(title)

    def get_books(self):
        return self.books.copy()


class BooksTemplateList:
    def render(self, books):
        if not books:
            return "Книг поки немає"
        return "\n".join(f"- {title}" for title in books)


class BooksPageView:
    def __init__(self, model):
        self.model = model

    def render(self, template):
        books = self.model.get_books()
        return template.render(books)



model = BooksModel()
page = BooksPageView(model)

print(page.render(BooksTemplateList()))
model.add_book("Кобзар")
model.add_book("Місто")
print(page.render(BooksTemplateList()))