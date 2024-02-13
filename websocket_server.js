const WebSocket = require('ws')

const wss = new WebSocket.Server({ port: 8080 })

const subscriptions = {}

wss.on('connection', function connection(ws) {
  console.log('A new client connected')
  
  ws.on('message', function incoming(message) {
    console.log('received: %s', message)

    switch(message.type) {
        case 'subscribe':
            const topic = message.topic
            if(!subscriptions[topic]) {
                subscriptions[topic] = new Set()
            }
            subscriptions[topic].add(ws)
            break

        case 'publish':
            const subscribers = subscriptions[message.topic] || []
            subscribers.forEach(client => {
                if (client.readyState === WebSocket.OPEN){
                    client.send(JSON.stringify(message.data))
                }
            })
            break
        }
    })


    ws.on("close", () => {
        for(const topic in subscriptions) {
            subscriptions[topic].delete(ws)
        }
    })

  })
  
  // You can also send a message from the backend to the clients here
//   ws.send(JSON.stringify({ text: 'Hello from the backend!' }))


console.log('WebSocket server started on ws://localhost:8080')
