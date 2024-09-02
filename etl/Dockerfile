# Use the official MySQL image as a base
FROM mysql:8.0

# Copy the SQL script to initialize the database
COPY ./init.sql /docker-entrypoint-initdb.d/

# Expose port 3306 to allow external applications to connect to the database
EXPOSE 3306