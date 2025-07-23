'use strict';

module.exports = {
  up: async (queryInterface, Sequelize) => {
    await queryInterface.createTable('restaurants', {
      id: {
        allowNull: false,
        autoIncrement: true,
        primaryKey: true,
        type: Sequelize.INTEGER
      },
      name: {
        type: Sequelize.STRING,
        allowNull: false
      },
      address: {
        type: Sequelize.STRING,
        allowNull: false
      },
      openTime: {
        type: Sequelize.STRING,
        allowNull: false
      },
      closeTime: {
        type: Sequelize.STRING,
        allowNull: false
      },
      contactNo: {
        type: Sequelize.STRING,
        allowNull: false
      },
      cuisine: {
        type: Sequelize.STRING,
        allowNull: false
      },
      topDishes: {
        type: Sequelize.STRING,
        allowNull: true
      },
      averageCost: {
        type: Sequelize.INTEGER,
        allowNull: false
      },
      createdAt: {
        allowNull: false,
        type: Sequelize.DATE,
        defaultValue: Sequelize.literal('CURRENT_TIMESTAMP')
      },
      updatedAt: {
        allowNull: false,
        type: Sequelize.DATE,
        defaultValue: Sequelize.literal('CURRENT_TIMESTAMP')
      }
    });
  },

  down: async (queryInterface, Sequelize) => {
    await queryInterface.dropTable('restaurants');
  }
};
