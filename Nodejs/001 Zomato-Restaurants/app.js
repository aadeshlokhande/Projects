const express = require('express');
const app = express();
const { sequelize } = require('./models');
const restaurantRoutes = require('./routes/restaurantRoutes');

app.use(express.json()); // to parse JSON body
app.use('/restaurants', restaurantRoutes); // base route

app.listen(3000, () => {
  console.log('Server is running on port 3000');
  sequelize.authenticate().then(() => {
    console.log("DB Connected");
  }).catch((err) => {
    console.log("Error: ", err);
  });
});
