


const { Sequelize } = require('sequelize'); // Import Sequelize

// Initialize Sequelize with your database credentials
const sequelize = new Sequelize('IPTV', 'postgres', '8655', {
    host: 'localhost',
    dialect: 'postgres',
});

const User = require('./User')(sequelize); // Pass sequelize instance to the user Model

// Synchronize models with the databse
sequelize.sync({ force: true }).then(() => {
    console.log('Database & Tables created!');
}).catch(error => {
    console.error('Error creating database & tables:', error);
});

// Exort the Sequelize instance and the models
module.exports = {
    sequelize,
    User,
};