# Reverse engineering the database refers to the process of analyzing an existing database to understand its structure, relationships, constraints, and other attributes.

## Tool needed
`pip install sqlacodegen`

## Command to reverse engineer
`sqlacodegen --outfile models.py postgresql://username:password@hostname:port/databasename`
