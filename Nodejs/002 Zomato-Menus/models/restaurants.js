'use strict';
const { Model } = require('sequelize');

module.exports = (sequelize, DataTypes) => {
  class restaurants extends Model {
    static associate(models) {
      // define association here (agar foreign key lage to)
      restaurants.hasMany(models.Menu, {
      foreignKey: 'restaurantId',
      onDelete: 'CASCADE',
      });
    }
  }
  restaurants.init({
    name: {
      type: DataTypes.STRING,
      allowNull: false
    },
    address: {
      type: DataTypes.STRING,
      allowNull: false
    },
    openTime: {
      type: DataTypes.STRING,
      allowNull: false
    },
    closeTime: {
      type: DataTypes.STRING,
      allowNull: false
    },
    contactNo: {
      type: DataTypes.STRING,
      allowNull: false
    },
    cuisine: {
      type: DataTypes.STRING,
      allowNull: false
    },
    topDishes: {
      type: DataTypes.STRING,
      allowNull: true
    },
    averageCost: {
      type: DataTypes.INTEGER,
      allowNull: false
    }
  }, {
    sequelize,
    modelName: 'restaurants',
  });
  return restaurants;
};
