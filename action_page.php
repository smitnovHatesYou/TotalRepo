<!-- action_page.php -->

<?php
// Get the form data 
$firstName = $_POST['fname']; 
$lastName = $_POST['lname'];
$email = $_POST['email'];
$birthday = $_POST['birthday'];

// save to database

// in action_page.php

header("Location: Untitled-1.html");

// in action_page.php
$firstName = getSubmittedFirstNameFromForm();

//then pass $firstname to Untitled-1.html
?>