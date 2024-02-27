php
<?php
// Connect to SQLite database
$db = new SQLite3('database.db');

// Get data from the form
$name = $_POST['name'];
$email = $_POST['email'];

// Insert data into the database
$query = "INSERT INTO users (name, email) VALUES ('$name', '$email')";
$db->exec($query);

// Close the database connection
$db->close();

echo "Data saved successfully!";
?>
