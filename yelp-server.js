// server.js

const express = require("express")
// const fetch = require("node-fetch")

const app = express()
const port = 4000

const cors = require('cors');
app.use(cors());

const apikey = "HupqS1suMvvTiIKD3P52WCLQyRJUOEwOhGIghMaUoOejbYSyCREATi1Fgi1fw13j_I_Rbs4AOukCU14ZUZQPQFjwaX6wrt-zVhZ84slCpHIq9knmib4nkNTG7MGVZXYx"
app.use(express.json())

app.get("/search", async(req, res) => {
    const { term, location, radius } = req.query

    try {
        const fetch = (await import('node-fetch')).default
        const url = `https://api.yelp.com/v3/businesses/search?term=${term}&location=${location}&radius=${radius}`
        // if (radius) {
        //     url += `&radius=${radius}`;
        // }
        console.log(`Term: ${term}, Location: ${location}, Radius: ${radius}`);

        const yelpresponse = await fetch(url, {
            headers: {
                'Authorization': `Bearer ${apikey}`
            }
        })
        console.log(`Term: ${term}, Location: ${location}, Radius: ${radius}`);


        const data = await yelpresponse.json()
        res.json(data)
    } catch (error) {
        res.status(500).json({ error: error.message })

    }
})




app.listen(port, () => {
    console.log(`server running on http://localhost:${port}`)
})