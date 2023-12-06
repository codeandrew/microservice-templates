const express = require('express');
const SQLiteDB = require('./db');
const app = express();
const db = new SQLiteDB('./mydb.sqlite');

app.use(express.json());

// API Endpoints
app.post('/users', (req, res) => {
    db.createUser(req.body, (err, data) => {
        if (err) {
            res.status(400).send(err.message);
        } else {
            res.status(201).send(data);
        }
    });
});

app.get('/users/:id', (req, res) => {
    db.getUser(req.params.id, (err, row) => {
        if (err) {
            res.status(400).send(err.message);
        } else {
            res.status(200).send(row);
        }
    });
});

app.put('/users/:id', (req, res) => {
    db.updateUser(req.params.id, req.body, (err, data) => {
        if (err) {
            res.status(400).send(err.message);
        } else {
            res.status(200).send(data);
        }
    });
});

app.delete('/users/:id', (req, res) => {
    db.deleteUser(req.params.id, (err, data) => {
        if (err) {
            res.status(400).send(err.message);
        } else {
            res.status(200).send(data);
        }
    });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
