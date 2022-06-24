const messages = [
    {
        "id": "830d98ae-0a41-427b-8049-6e6d4aeb6ec1",
        "text": "Have you seen VueJS?",
        "time": "14:38",
        "sender": {
            "id": "012ffb9f-dbdd-45cb-8767-dbe349290a7d",
            "name": "Alice",
            "profilePicture": "https://randomuser.me/api/portraits/med/women/75.jpg"
        },
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
        "id": "7254c94a-ad6c-462d-8194-0453434cf173",
        "text": "Yeah, we started using it. I like it so far.",
        "time": "14:40",
        "sender": {
            "id": "4bd7ebd4-6ead-4ede-ac73-37d167ddae9d",
            "name": "Bob",
            "profilePicture": "https://randomuser.me/api/portraits/med/men/75.jpg"
        },
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
