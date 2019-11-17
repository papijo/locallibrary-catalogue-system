var quotes = [
    'So many books, so little time.',
    'A room without books is like a body without a soul.',
    'The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.',
    'Good friends, good books, and a sleepy conscience: this is the ideal life.',
    'Fairy tales are more than true: not because they tell us that dragons exist, but because they tell us that dragons can be beaten.',
    'Outside of a dog, a book is man\'s best friend. Inside of a dog it\'s too dark to read.',
    'I have always imagined that Paradise will be a kind of library.',
    'If you only read the books that everyone else is reading, you can only think what everyone else is thinking.',
    'Never trust anyone who has not brought a book with them.',
    'You can never get a cup of tea large enough or a book long enough to suit me.',
]

function newQuote() {
    var randomNumber = Math.floor(Math.random() * (quotes.length));
    document.getElementById('quoteDisplay').innerHTML = quotes[randomNumber]
}


