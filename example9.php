<!DOCTYPE html>
<html>
    <head>
        <title></title>
    </head>

    <body>
        
    </body>

    <script>
        async function getData() {
            try {
                const response = await fetch("https://newsapi.org/v2/everything?q=Apple&from=2023-01-28&sortBy=popularity&apiKey=7f86e5266e7a4f64812d0aede2e2c9de")
                const data = await response.json()

            } catch (error) {
                console.log("Error: " + error)
            }
        }

        getData()

    </script>
</html>