use('octofit_db');
db.users.createIndex({ "email": 1 }, { unique: true });
