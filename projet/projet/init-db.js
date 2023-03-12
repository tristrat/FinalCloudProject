db = db.getSiblingDB('scores')
db.score.drop()
db.createCollection('scores')

db.scores.insertMany([
    { name: 'Alice', score: 10 },
    { name: 'Bob', score: 20 },
    { name: 'Charlie', score: 30 }
])