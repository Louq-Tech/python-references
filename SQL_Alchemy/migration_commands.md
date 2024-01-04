# How to migrate from SQLAlchemy to PostgreSQL or any database

## Library needed
`pip install alembic`

### Steps to start migration
1. Create init file
   `alembic init alembic`
2. Create initial migration
   `alembic revision --autogenerate -m "Initial migration"`
3. Run migration
   `alembic upgrade head`

### Steps to downgrade
1. Review all revisions
   `alembic history`
2. Downgrade to specific revision
   `alembic downgrade <revision_id>`
