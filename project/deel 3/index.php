<!DOCTYPE html>
<html>
    <head>
        <title>World</title>
    </head>
    <body>
        <p><strong>get info for country's</strong></p>
        <form method="post" id="form" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">
            <input type="text" placeholder="country Code" name="Code">
            <input type="submit" name="submit" value="submt">
        </form>
        <p><strong>get info for country's</strong></p>
        <?php
            $request = file_get_contents("http://localhost:8000/countrys/");
            $requestArray = json_decode($request, true);
            foreach($requestArray as $request)
            {
                $requestcity = file_get_contents("http://localhost:8000/citys/". $request["Captital"] . "/");
                $request2 = json_decode($requestcity, true);
                $requestlanguage = file_get_contents("http://localhost:8000/countrylanguages/". $request["Code"] . "/");
                $request3 = json_decode($requestlanguage, true);
                // echo "country naam test " .$request . "<br><br>";
                // echo "hoofdstad naam test " .$requestcity . "<br><br>";
                echo "<div class=''>";
                echo "The country " . $request["Name"] . " ";
                echo "has the country code: " . $request["Code"] . "<br>";
                echo "it is on the continent: " . $request["Continent"] . " ";
                echo "and in the region: " . $request["Region"] . "<br>";
                echo "the surfaceArea of " . $request["Name"] . " is " . $request["SurfaceArea"] . " <br>";
                echo "and it has a population of " . $request["Population"] . " residents <br>";
                echo "the name of the capital is " .$request2["name"] . " ";
                echo "its id is: " .$request2["ID"] . " <br>";
                echo "it has " .$request2["Population"] . " residents. <br>";
                echo "in the country " . $request["Name"] . " about ".$request3["Percentage"]. " % speaks " . $request3["Language"]. "  <br><br>";
                echo "</div>"; 
            }
        ?>
    </body>
</html>