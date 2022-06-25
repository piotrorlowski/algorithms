const reactions = [
    {
        "reactions": [
            {
                "id": "2",
                "content": "👍"
            },
            {
                "id": "4",
                "content": "🍷",
                "deleted": true
            },
            {
                "id": "3",
                "content": "❓"
            },
            {
                "id": "2",
                "content": "👍"
            },
            {
                "id": "3",
                "content": "❓"
            },
            {
                "id": "2",
                "content": "👍"
            },
            {
                "id": "5",
                "content": "👀",
                "deleted": true
            }
        ]
    },
    {
        "reactions": [
            {
                "id": "1",
                "content": "🔥"
            },
            {
                "id": "1",
                "content": "🔥"
            },
            {
                "id": "1",
                "content": "🔥"
            },
            {
                "id": "1",
                "content": "🔥"
            },
            {
                "id": "6",
                "content": "🧀",
                "deleted": true
            }
        ]
    }
];
  
function getResponsesWithCount(messages) {
    return messages.map(message => {
        return message.reactions.reduce((acc, reaction) => {
            if (acc[reaction.id]) {
                acc[reaction.id].count++;
            } else {
                acc[reaction.id] = { ...reaction, count: 1 };
            }
            return acc;
        }, {})
    })
};

console.log(getResponsesWithCount(messages));
