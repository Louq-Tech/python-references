# Reverse engineering refers to the process of generating Python code (models) from an existing database schema.

This is particularly useful when you have a legacy database and you want to create models that reflect its structure without having to manually write them

## Library needed
`pip install sqlacodegen`

## Command to reverse engineer
`sqlacodegen --outfile models.py postgresql://username:password@hostname:port/databasename`
