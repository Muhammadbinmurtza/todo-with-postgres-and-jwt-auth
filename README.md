install 
    -uv run alembic
    - uv add psycopg2-binary
    
new project setup 
    - uv run alembic init {project name}
    - change sqlalchemy.url in alembic.ini with the url of database connect url
    -create sqlalchemy model for your table
    -change target metadata in env file in alembic
every change in models run following commands:
    -uv run alembic revision --autogenerate -m "create todos table"
    - uv run alembic upgrade head