This project was made for Database programming(CMP3872) prctical test 2.
below is what was it all about:

**Question 1: Indexing Strategies (B-trees vs Hash Indexes)**

In this task, a simple Student Records App was created using SQLAlchemy with PostgreSQL.

A Student model was defined with the fields: id, name, email, and grade.

10 dummy student records were inserted.

Two queries were executed:

Retrieve students by name

Retrieve students by email

A B-tree index was defined on the name field, and a Hash index on the email field using SQLAlchemy’s Index construct.

Both queries were analyzed using EXPLAIN ANALYZE to compare performance.

**Reflection:**

B-tree indexes are preferred for range and sorted lookups (e.g., names, grades), while hash indexes are ideal for exact-match lookups such as email addresses.

**Question 2: Migration Workflow with Alembic**

This task extends a Bookstore App by demonstrating database schema migrations using Alembic.

Alembic was initialized to manage migrations.

A new migration revision added a published_date column to the Book table.

The Book model was updated to include this field.

A script was created to insert 3 books with their published dates and query all books ordered by publication date.

**Note:**

Migration workflows are crucial in production applications because they allow safe, version-controlled schema changes without losing existing data or breaking the application.

**Question 3: Eager Loading with Relationships**

This task implements a Blogging App using SQLAlchemy with Author and Post models.

Two models were created:

Author(id, name)

Post(id, title, content, author_id)

A one-to-many relationship was established between Author and Post.

2 authors and 5 posts were inserted.

Two queries were tested:

Lazy loading – fetches posts per author as needed (multiple queries)

Eager loading (joinedload) – fetches all authors and posts in one query.

The number of SQL queries executed was printed and compared.
