SELECT usename FROM pg_user WHERE usename = 'school_user';
GRANT ALL PRIVILEGES ON DATABASE school_portal TO school_user;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO school_user;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO school_user;