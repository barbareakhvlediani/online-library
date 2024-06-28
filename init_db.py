from app import create_app, db
from app.models import Book

app = create_app()

books_data = [
    {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'genre': 'Fiction', 'description': 'Classic novel set in the American South during the 1930s.'},
    {'title': '1984', 'author': 'George Orwell', 'genre': 'Science Fiction', 'description': 'Dystopian novel depicting a totalitarian regime.'},
    {'title': 'Pride and Prejudice', 'author': 'Jane Austen', 'genre': 'Romance', 'description': 'Regency-era novel about love and society.'},
    {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'genre': 'Fiction', 'description': 'American novel exploring themes of decadence and idealism.'},
    {'title': 'Moby-Dick', 'author': 'Herman Melville', 'genre': 'Adventure', 'description': 'Epic tale of a sea captain\'s obsession with a great white whale.'},
    {'title': 'The Catcher in the Rye', 'author': 'J.D. Salinger', 'genre': 'Fiction', 'description': 'Coming-of-age novel narrated by a disenchanted teenager.'},
    {'title': 'Harry Potter and the Philosopher\'s Stone', 'author': 'J.K. Rowling', 'genre': 'Fantasy', 'description': 'First book in the Harry Potter series.'},
    {'title': 'The Hobbit', 'author': 'J.R.R. Tolkien', 'genre': 'Fantasy', 'description': 'Classic fantasy adventure novel.'},
    {'title': 'Brave New World', 'author': 'Aldous Huxley', 'genre': 'Science Fiction', 'description': 'Dystopian novel exploring a future society controlled by technology.'},
    {'title': 'Jane Eyre', 'author': 'Charlotte Brontë', 'genre': 'Romance', 'description': 'Gothic novel following the life of an orphaned girl.'},
    {'title': 'War and Peace', 'author': 'Leo Tolstoy', 'genre': 'Historical Fiction', 'description': 'Epic novel set during the Napoleonic Wars.'},
    {'title': 'The Lord of the Rings', 'author': 'J.R.R. Tolkien', 'genre': 'Fantasy', 'description': 'Epic high fantasy trilogy.'},
    {'title': 'Crime and Punishment', 'author': 'Fyodor Dostoevsky', 'genre': 'Psychological Fiction', 'description': 'Novel exploring morality and redemption.'},
    {'title': 'Frankenstein', 'author': 'Mary Shelley', 'genre': 'Gothic Fiction', 'description': 'Classic science fiction novel about a scientist who creates a sentient creature.'},
    {'title': 'The Picture of Dorian Gray', 'author': 'Oscar Wilde', 'genre': 'Gothic Fiction', 'description': 'Novel about a young man who makes a pact to remain young and handsome while his portrait ages.'},
    {'title': 'The Odyssey', 'author': 'Homer', 'genre': 'Epic Poetry', 'description': 'Ancient Greek epic poem attributed to Homer, chronicling the adventures of Odysseus.'},
    {'title': 'The Road', 'author': 'Cormac McCarthy', 'genre': 'Post-apocalyptic Fiction', 'description': 'Novel following a father and son\'s journey across a desolate landscape.'},
    {'title': 'Alice\'s Adventures in Wonderland', 'author': 'Lewis Carroll', 'genre': 'Fantasy', 'description': 'Children\'s novel about a girl who falls down a rabbit hole into a whimsical world.'},
    {'title': 'The Brothers Karamazov', 'author': 'Fyodor Dostoevsky', 'genre': 'Philosophical Fiction', 'description': 'Russian novel exploring themes of faith, reason, and morality.'},
    {'title': 'Gone with the Wind', 'author': 'Margaret Mitchell', 'genre': 'Historical Fiction', 'description': 'Epic novel set in the American South during the Civil War and Reconstruction era.'}
]

with app.app_context():
    db.create_all()
    for book_data in books_data:
        book = Book(title=book_data['title'], author=book_data['author'], genre=book_data['genre'], description=book_data['description'])
        db.session.add(book)
    db.session.commit()