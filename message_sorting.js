const messageArray = {
    value: [
        {definition: { id: "error", priority: 2}},
        {definition: { id: "warning", priority: 1}},
        {definition: { id: "info", priority: 4}},
        {definition: { id: "warning", priority: 3}},
    ]
}

// sorting function based on priority
function sortByPriority(messages) {
    return messages.sort((a, b) => a.definition.priority - b.definition.priority)

}

function getMessagesByIdStartingWith(partialId) {
    const filteredMessages = messageArray.value.filter(entry => entry.definition.id.startsWith(partialId))

    return sortByPriority(filteredMessages)
}


// test the functions
const filteredAndSorted = getMessagesByIdStartingWith("warning")
filteredAndSorted.forEach(message => {
    console.log(`${message.definition.id} - ${message.definition.priority}`)
})
