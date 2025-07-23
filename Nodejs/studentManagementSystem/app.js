const express = require('express');
const bodyParser = require('body-parser');
const path = require('path');
const { Student } = require('./models');

const app = express();

// EJS setup
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));


// Middleware to parse form data
app.use(bodyParser.urlencoded({ extended: false }));

// Serve HTML file
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'views/form.html'));
});

// Route to handle form submission
app.post('/students', async (req, res) => {
  try {
    const { name, age, std, rollnumber, mobilenumber } = req.body;

    // Insert into MySQL using Sequelize
    await Student.create({
      name,
      age,
      std,
      rollnumber,
      mobilenumber
    });

    // res.send("Student inserted successfully!");
    const students = await Student.findAll();
    res.render('students', { students });
  } catch (error) {
    console.error(error);
    res.status(500).send("Error inserting student");
  }
});

// Show all students
app.get('/students', async (req, res) => {
  try {
    const students = await Student.findAll();
    res.render('students', { students }); // render EJS
  } catch (err) {
    res.status(500).send("Error fetching students");
  }
});

// Show edit form
app.get('/students/edit/:id', async (req, res) => {
  const student = await Student.findByPk(req.params.id);
  if (!student) return res.status(404).send('Student not found');
  res.render('editStudent', { student });
});

// Handle form submission to update student
app.post('/students/edit/:id', async (req, res) => {
  const { name, age, std, rollnumber, mobilenumber } = req.body;
  try {
    await Student.update(
      { name, age, std, rollnumber, mobilenumber },
      { where: { id: req.params.id } }
    );
    res.redirect('/students');
  } catch (err) {
    console.error(err);
    res.status(500).send("Error updating student");
  }
});


// Delete student by ID
app.post('/students/delete/:id', async (req, res) => {
  try {
    await Student.destroy({
      where: { id: req.params.id }
    });
    res.redirect('/students');
  } catch (err) {
    console.error(err);
    res.status(500).send("Error deleting student");
  }
});



// Start server
app.listen(3000, () => {
  console.log('Server started at http://localhost:3000');
});
