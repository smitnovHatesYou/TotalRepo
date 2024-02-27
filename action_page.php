php
<?php
// Connect to SQLite database
$db = new SQLite3('database.db');

// Get form data
$first_name = $_POST['first_name'];
$last_name = $_POST['last_name'];
$email = $_POST['email'];
$dob = $_POST['dob'];

// Insert data into the database
$query = "INSERT INTO users (first_name, last_name, email, dob) VALUES ('$first_name', '$last_name', '$email', '$dob')";
$db->exec($query);

// Close the database connection
$db->close();

echo "Data saved successfully!";
?>
