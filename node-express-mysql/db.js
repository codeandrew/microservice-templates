const mysql = require('mysql');

class MySQLDB {
    constructor(config) {
        this.connection = mysql.createConnection(config);
    }

    connect() {
        this.connection.connect(err => {
            if (err) {
                console.error('Error connecting to MySQL database:', err);
                return;
            }
            console.log('Connected to MySQL database.');
        });
    }

    createUser(user, callback) {
        const sql = 'INSERT INTO user SET ?';
        this.connection.query(sql, user, callback);
    }

    getUser(id, callback) {
        const sql = 'SELECT * FROM user WHERE id = ?';
        this.connection.query(sql, [id], callback);
    }

    getAllUsers(callback) {
        const sql = 'SELECT * FROM user';
        this.connection.query(sql, callback);
    }

    updateUser(id, user, callback) {
        const sql = 'UPDATE user SET ? WHERE id = ?';
        this.connection.query(sql, [user, id], callback);
    }

    deleteUser(id, callback) {
        const sql = 'DELETE FROM user WHERE id = ?';
        this.connection.query(sql, [id], callback);
    }

    close() {
        this.connection.end();
    }
}

module.exports = MySQLDB;
