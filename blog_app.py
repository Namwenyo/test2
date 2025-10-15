from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, event
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker, joinedload
import logging
import time

# Set up logging to see SQL queries
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

Base = declarative_base()

class Author(Base):
    __tablename__ = 'authors'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    
    # Relationship with posts
    posts = relationship("Post", back_populates="author", lazy='select')  # Default lazy loading

class Post(Base):
    __tablename__ = 'posts'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    content = Column(String(1000), nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'))
    
    # Relationship with author
    author = relationship("Author", back_populates="posts")

# Create database and tables
engine = create_engine('sqlite:///blog.db', echo=True)  # Set echo=True to see queries
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def seed_data():
    """Insert sample authors and posts"""
    # Create authors
    author1 = Author(name="Alice Johnson")
    author2 = Author(name="Bob Smith")
    
    session.add_all([author1, author2])
    session.commit()
    
    # Create posts
    posts = [
        Post(title="Python Programming", content="Introduction to Python...", author_id=author1.id),
        Post(title="Web Development", content="Building web applications...", author_id=author1.id),
        Post(title="Data Science", content="Data analysis techniques...", author_id=author1.id),
        Post(title="Machine Learning", content="ML algorithms explained...", author_id=author2.id),
        Post(title="Database Design", content="SQL and database design...", author_id=author2.id),
    ]
    
    session.add_all(posts)
    session.commit()
    print("Sample data inserted: 2 authors, 5 posts")

def lazy_loading_demo():
    """Demonstrate lazy loading (N+1 query problem)"""
    print("\n" + "="*60)
    print(" LAZY LOADING DEMO")
    print("="*60)
    
    # Create a new session for this demo
    demo_session = Session()
    
    # Start timing
    start_time = time.time()
    
    # Get all authors (1 query)
    print("1. Fetching authors...")
    authors = demo_session.query(Author).all()
    
    print("2. Accessing posts for each author (this triggers N+1 queries)...")
    # Access posts for each author (N additional queries - N+1 problem!)
    for author in authors:
        print(f"\nAuthor: {author.name}")
        print(f"Number of posts: {len(author.posts)}")
        for post in author.posts:
            print(f"  - {post.title}")
    
    elapsed_time = time.time() - start_time
    
    demo_session.close()
    
    print(f"\n LAZY LOADING RESULTS:")
    print(f"Time taken: {elapsed_time:.4f} seconds")
    print("Note: Check the SQL logs above to see the N+1 queries!")
    
    return elapsed_time

def eager_loading_demo():
    """Demonstrate eager loading with joinedload"""
    print("\n" + "="*60)
    print(" EAGER LOADING DEMO (joinedload)")
    print("="*60)
    
    # Create a new session for this demo
    demo_session = Session()
    
    # Start timing
    start_time = time.time()
    
    # Get all authors with their posts in a single query using JOIN
    print("1. Fetching authors with posts using JOIN...")
    authors = demo_session.query(Author).options(joinedload(Author.posts)).all()
    
    print("2. Accessing posts (no additional queries needed)...")
    # Access posts for each author (NO additional queries!)
    for author in authors:
        print(f"\nAuthor: {author.name}")
        print(f"Number of posts: {len(author.posts)}")
        for post in author.posts:
            print(f"  - {post.title}")
    
    elapsed_time = time.time() - start_time
    
    demo_session.close()
    
    print(f"\n EAGER LOADING RESULTS:")
    print(f"Time taken: {elapsed_time:.4f} seconds")
    print("Note: Only ONE query was executed (check logs above)!")
    
    return elapsed_time

def simple_query_counter():
    """Alternative method to count queries"""
    print("\n" + "="*60)
    print(" SIMPLE QUERY COUNT COMPARISON")
    print("="*60)
    
    # Count queries for lazy loading
    print("LAZY LOADING query pattern:")
    lazy_session = Session()
    authors = lazy_session.query(Author).all()
    print(f"1. Initial query to get authors: 1 query")
    
    query_count = 1
    for i, author in enumerate(authors, 1):
        posts_count = len(author.posts)  # This triggers additional query
        print(f"   {i+1}. Query for {author.name}'s posts: {posts_count} posts")
        query_count += 1
    
    print(f"Total queries with lazy loading: {query_count} (N+1 problem)")
    lazy_session.close()
    
    # Count queries for eager loading
    print("\nEAGER LOADING query pattern:")
    eager_session = Session()
    authors = eager_session.query(Author).options(joinedload(Author.posts)).all()
    print("1. Single JOIN query to get authors + posts: 1 query")
    
    for author in authors:
        posts_count = len(author.posts)  # No additional query - data already loaded
        print(f"   Accessed {author.name}'s posts: {posts_count} posts (no query)")
    
    print("Total queries with eager loading: 1 (N+1 problem solved)")
    eager_session.close()
    
    return query_count, 1

def main():
    print("🧪 Blogging App - Eager vs Lazy Loading Demonstration")
    print("="*60)
    
    # Seed the database
    seed_data()
    
    print("\n TURN ON SQL LOGGING TO SEE THE QUERIES EXECUTED!")
    print("You should see multiple SELECT statements for lazy loading")
    print("and only one SELECT with JOIN for eager loading")
    
    # Run both demonstrations
    lazy_time = lazy_loading_demo()
    eager_time = eager_loading_demo()
    
    # Simple query counter
    lazy_queries, eager_queries = simple_query_counter()
    
    # Performance comparison
    print("\n" + "="*60)
    print("PERFORMANCE COMPARISON SUMMARY")
    print("="*60)
    print(f"Lazy Loading:  {lazy_queries} queries, {lazy_time:.4f} seconds")
    print(f"Eager Loading: {eager_queries} queries, {eager_time:.4f} seconds")
    print(f"Query reduction: {lazy_queries - eager_queries} queries")
    print(f"Time improvement: {lazy_time - eager_time:.4f} seconds")
    
    print("\n" + "="*60)
    print("💡 KEY INSIGHTS:")
    print("="*60)
    print("1. LAZY LOADING causes N+1 query problem:")
    print("   - 1 query to get authors + N queries to get posts for each author")
    print("   - 3 total queries for 2 authors (1 + 2)")
    
    print("\n2. EAGER LOADING solves this with JOIN:")
    print("   - Single query using JOIN to get authors and their posts")
    print("   - Eliminates the N+1 problem completely")
    
    print("\n3. Performance impact:")
    print("   - Fewer queries = less database round trips")
    print("   - Better performance, especially with many related objects")
    print("   - Use eager loading when you know you'll need related data")

if __name__ == "__main__":
    main()