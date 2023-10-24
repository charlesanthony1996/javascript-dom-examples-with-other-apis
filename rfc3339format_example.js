async function fetchData(fromDate, toDate) {
    const torfc3339 = (date) => date.toISOString()

    const baseurl = "https://example.com/data"

    const url = `${baseURL}?fromDate=${torfc3339(fromDate)}&toDate=${torfc3339(toDate)}`

    try {
        const response = await fetch(url)

        if(!response.ok) {
            throw new Error(`http error!, Status: ${response.status}`)
        }
        const data = await response(data)
        return data

        
    } catch(data) {
        console.error("There was problem with the fetch: ", error)
    }
}


const startDate = new Date('2023-01-01T00:00:00Z')
const endDate = new Date('2023-05-01T00:00:00Z')


fetchData(startDate, endDate).then(data => {
    console.log(data)
})