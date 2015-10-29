<?php
    $db_connection = pg_pconnect("host=docker.postgres.local dbname=benchmark user=postgres password=root");

    header('Content-Type: application/json');
    $data = array();
    $method = $_SERVER['REQUEST_METHOD'];
    if ($meth == 'POST') {

    }
    else {
        $result = pg_query($db_connection, "SELECT * FROM urls");
        if (! $result) {
            echo "An error occurred.\n";
            exit;
        }

        while ($row = pg_fetch_row($result)) {
	        array_push($data, $data["long_url"] = $row[1]);
            array_push($data, $data["short_url"] = $row[2]);
        }
    }

    echo json_encode($data);
?>