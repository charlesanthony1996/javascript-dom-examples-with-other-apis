const WebSocket = require('ws')

const wss = new WebSocket.Server({ port: 8080 })

const subscriptions = {}
const users = {}


wss.on('connection', function connection(ws) {
  console.log('A new client connected')
  
  ws.on('message', function incoming(message) {
    // const parsedMessage = JSON.parse(data)
    console.log('Message received: ', message)

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

        case 'authenticate':
            const username = message.username
            users[username] = ws
            ws.username = username

            ws.send(JSON.stringify({ type: 'authenticated', username: username }))
            break

        case 'private_message':
            const recipient = message.recipient
            const sender = ws.username
            if(users[recipient] && users[recipient].readyState === WebSocket.OPEN) {
                users[recipient].send(JSON.stringify({
                    type: 'private_message',
                    from: sender,
                    text: message.text
                }))
            }

        }


    })


    ws.on("close", () => {
        if(ws.username) {
            delete users[ws.username]
        }

        for(const topic in subscriptions) {
            subscriptions[topic].delete(ws)
        }
    })

  })
  
  // You can also send a message from the backend to the clients here
//   ws.send(JSON.stringify({ text: 'Hello from the backend!' }))


console.log('WebSocket server started on ws://localhost:8080')
