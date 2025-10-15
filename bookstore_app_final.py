from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import date

Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    price = Column(Float, nullable=False)
    published_date = Column(Date)  # New column added via migration
    
    def __repr__(self):
        return f"<Book(id={self.id}, title='{self.title}', price={self.price}, published_date={self.published_date})>"

# Database setup
engine = create_engine('sqlite:///bookstore.db')
Session = sessionmaker(bind=engine)

def insert_new_books():
    session = Session()
    
    # Insert 3 new books with published dates
    new_books = [
        Book(title="The Hobbit", price=14.99, published_date=date(1937, 9, 21)),
        Book(title="Dune", price=16.50, published_date=date(1965, 8, 1)),
        Book(title="The Martian", price=13.75, published_date=date(2011, 1, 1)),
    ]
    
    session.add_all(new_books)
    session.commit()
    print("3 new books inserted with published dates!")

def query_books_ordered_by_date():
    session = Session()
    
    # Query all books ordered by published_date
    books = session.query(Book).order_by(Book.published_date).all()
    
    print("\nAll books ordered by published_date:")
    print("-" * 50)
    for book in books:
        pub_date = book.published_date.strftime("%Y-%m-%d") if book.published_date else "Unknown"
        print(f"Title: {book.title:<25} | Price: ${book.price:<6} | Published: {pub_date}")
    
    session.close()

if __name__ == "__main__":
    insert_new_books()
    query_books_ordered_by_date()