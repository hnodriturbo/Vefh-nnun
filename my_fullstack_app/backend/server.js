


const express = require('express');
const { sequelize } = require("./models");
const app = express();
const port = 5000;


app.use(express.json());

app.get('/', (req, res) => {
    res.send('Hello World !');
});

sequelize.authenticate().then(() => {
    console.log('Connection to the databse has been established successfully.');

    app.listen(port, () => {
        console.log(`Server is running  on http://localhost:${port}`);
    });
}).catch(error => {
    console.error('Unable to connect to the database:', error);
});




