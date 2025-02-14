// PHP code (check-folder.php) to scan folder and return images
<?php
if (isset($_GET['folder'])) {
    $folder = $_GET['folder'];
    if (is_dir($folder)) {
        $images = array_diff(scandir($folder), array('..', '.'));
        echo json_encode(['exists' => true, 'images' => $images]);
    } else {
        echo json_encode(['exists' => false, 'images' => []]);
    }
} else {
    echo json_encode(['exists' => false, 'images' => []]);
}
?>