<?php
$target_dir = "./";
$target_file = $target_dir . basename($_FILES["fileToUpload"]["dosprawdzenia"]);
$uploadOk = 1;
$csvFileType = strtolower(pathinfo($target_file,PATHINFO_EXTENSION));

if (file_exists($target_file)) {
    echo "Sorry, file already exists.";
    $uploadOk = 0;
}

// Check file size
if ($_FILES["fileToUpload"]["size"] > 400000) {
    echo "Sorry, your file is too large.";
    $uploadOk = 0;
}

if($csvFileType != "csv") {
    echo "Sorry, only CSV files are allowed.";
    $uploadOk = 0;
}

if ($uploadOk == 0) {
    echo "Sorry, your file was not uploaded.";
} 

else {
    if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file)) {
        echo "The file ". basename( $_FILES["fileToUpload"]["dosprawdzenia"]). " has been uploaded.";
    } 
    
    else {
        echo "Sorry, there was an error uploading your file.";
    }
}

?>
