'use strict';
const { Model } = require('sequelize');

module.exports = (sequelize, DataTypes) => {
  class Menu extends Model {
    static associate(models) {
      // Each menu belongs to one restaurant
      Menu.belongsTo(models.restaurants, {
        foreignKey: 'restaurantId',
        onDelete: 'CASCADE',
      });
    }
  }

  Menu.init({
    name: DataTypes.STRING,
    description: DataTypes.STRING,
    foodType: DataTypes.STRING,
    price: DataTypes.STRING,
    restaurantId: {              // 👈 add FK here too
      type: DataTypes.INTEGER,
      allowNull: false
    }
  }, {
    sequelize,
    modelName: 'Menu',
  });

  return Menu;
};
