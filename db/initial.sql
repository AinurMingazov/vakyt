DO
$$
BEGIN
   IF NOT EXISTS (SELECT FROM pg_catalog.pg_roles WHERE rolname = '${POSTGRES_USER}')
    THEN CREATE ROLE ${POSTGRES_USER} WITH LOGIN PASSWORD '${POSTGRES_PASSWORD}';
   END IF;
END
$$;

GRANT ALL PRIVILEGES ON DATABASE ${POSTGRES_DB} TO ${POSTGRES_USER};
GRANT ALL ON SCHEMA public TO ${POSTGRES_USER};
GRANT ALL ON SCHEMA public TO public;
ALTER ROLE ${POSTGRES_USER} CREATEDB;