const { restaurants } = require('../models');

// add restaurant
const createRestaurant = async (req, res) => {
  try {
    const restaurant = await restaurants.create(req.body);
    res.status(201).json({StatusCode:200,restaurant});
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
};

// get all restaurant
const getAllRestaurants = async (req, res) => {
  try {
    const allRestaurants = await restaurants.findAll();
    res.status(200).json({StatusCode:200, allRestaurants});
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};


const getRestaurantById = async (req, res) => {
  try {
    const id = req.params.id;
    const restaurant = await restaurants.findByPk(id); // Primary key lookup

    if (!restaurant) {
      return res.status(404).json({ message: "Restaurant not found" });
    }

    res.status(200).json({StatusCode:200,restaurant});
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};

// update by id
const updateRestaurant = async (req, res) => {
  try {
    const id = req.params.id;
    const restaurant = await restaurants.findByPk(id);

    if (!restaurant) {
      return res.status(404).json({ message: "Restaurant not found" });
    }

    await restaurant.update(req.body); // update with new values
    res.status(200).json({StatusCode:200, message: "Restaurant updated successfully", restaurant });
    console.log(`Restaurant updated successfully of ID = ${id}`)
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};

const deleteRestaurant = async (req, res) => {
  try {
    const id = req.params.id;
    const restaurant = await restaurants.findByPk(id);

    if (!restaurant) {
      return res.status(404).json({ message: "Restaurant not found" });
    }

    await restaurant.destroy();
    res.status(200).json({StatusCode:200, message: "Restaurant deleted successfully" });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};


const { Op } = require('sequelize'); // Sequelize operators

const searchRestaurantByName = async (req, res) => {
  try {
    const name = req.query.name;

    if (!name) {
      return res.status(400).json({ message: "Name query is required" });
    }

    const results = await restaurants.findAll({
      where: {
        name: {
          [Op.like]: `%${name}%` // partial match
        }
      }
    });

    if (results.length === 0) {
      return res.status(404).json({ message: "No restaurants found" });
    }

    res.status(200).json(results);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};

module.exports = {
  createRestaurant,
  getAllRestaurants,
  getRestaurantById,
  updateRestaurant,
  deleteRestaurant,
  searchRestaurantByName,
};
