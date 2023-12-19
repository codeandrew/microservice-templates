const express = require('express');
const MySQLDB = require('./db');

const app = express();
app.use(express.json());

// Database configuration
const dbConfig = {
    host: 'localhost',
    user: 'root',
    password: 's3cure_th1s_sh1t',
    database: 'node0'
};

// Create database connection
const db = new MySQLDB(dbConfig);
db.connect();

// API endpoints
app.post('/users', (req, res) => {
    db.createUser(req.body, (err, result) => {
        if (err) res.status(500).send(err);
        else res.status(201).send({ id: result.insertId });
    });
});

app.get('/users/:id', (req, res) => {
    db.getUser(req.params.id, (err, result) => {
        if (err) res.status(500).send(err);
        else res.status(200).send(result[0]);
    });
});

app.get('/users', (req, res) => {
    db.getAllUsers((err, result) => {
        if (err) res.status(500).send(err);
        else res.status(200).send(result);
    });
});

app.put('/users/:id', (req, res) => {
    db.updateUser(req.params.id, req.body, (err, result) => {
        if (err) res.status(500).send(err);
        else res.status(200).send({ affectedRows: result.affectedRows });
    });
});

app.delete('/users/:id', (req, res) => {
    db.deleteUser(req.params.id, (err, result) => {
        if (err) res.status(500).send(err);
        else res.status(200).send({ affectedRows: result.affectedRows });
    });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});

process.on('SIGINT', () => {
    db.close();
    process.exit();
});
