'use strict';
const { Model } = require('sequelize');

module.exports = (sequelize, DataTypes) => {
  class Student extends Model {
    static associate(models) {
      // associations (agar koi ho to yaha likh sakte ho)
    }
  }

  Student.init({
    id: {
      type: DataTypes.INTEGER,
      primaryKey: true,
      autoIncrement: true
    },
    name: {
      type: DataTypes.STRING,
      allowNull: false
    },
    age: {
      type: DataTypes.INTEGER,
      allowNull: false
    },
    std: {
      type: DataTypes.STRING,
      allowNull: false
    },
    rollnumber: {
      type: DataTypes.INTEGER,
      allowNull: false,
      unique: true
    },
    mobilenumber: {
      type: DataTypes.STRING,
      allowNull: false,
      validate: {
        len: [10, 15]  // optional: mobile number length check
      }
    }
  }, {
    sequelize,
    modelName: 'Student',
    tableName: 'students',
    timestamps: true
  });

  return Student;
};
