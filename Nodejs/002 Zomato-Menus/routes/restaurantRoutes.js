const express = require('express');
const router = express.Router();
const { 
    createRestaurant,
    getAllRestaurants,
    getRestaurantById,
    updateRestaurant,
    deleteRestaurant,
    searchRestaurantByName
} = require('../controllers/restaurantController');

router.post('/add', createRestaurant);
router.get('/', getAllRestaurants);  
router.get('/:id', getRestaurantById); 
router.put('/:id', updateRestaurant); 
router.delete('/:id', deleteRestaurant);
router.get('/search/name', searchRestaurantByName);

module.exports = router;
