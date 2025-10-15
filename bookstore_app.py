from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    price = Column(Float, nullable=False)
    # published_date will be added later via migration
    
    def __repr__(self):
        return f"<Book(id={self.id}, title='{self.title}', price={self.price})>"

# Database setup
engine = create_engine('sqlite:///bookstore.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

def initialize_database():
    session = Session()
    # Clear existing data
    session.query(Book).delete()
    
    # Add some initial books (without published_date)
    books = [
        Book(title="The Great Gatsby", price=12.99),
        Book(title="To Kill a Mockingbird", price=10.50),
        Book(title="1984", price=9.99),
    ]
    
    session.add_all(books)
    session.commit()
    session.close()
    print("Initial database setup completed!")

if __name__ == "__main__":
    initialize_database()