import sqlite3


def init():
    connection = sqlite3.connect('rest_api.db')
    
    sqllite_create_table_execute = '''
        CREATE TABLE IF NOT EXISTS quotes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            author TEXT NOT NULL,
            quote TEXT NOT NULL UNIQUE
        );
        '''

    cursor = connection.cursor()
    cursor.execute(sqllite_create_table_execute)
    connection.commit()
    connection.close()



    connection = sqlite3.connect('rest_api.db')
    cursor = connection.cursor()

    ai_quotes = [
        {
       "author": "Kevin Kelly",
       "quote": "The business plans of the next 10,000 startups are easy to forecast: " +
                "Take X and add AI."
    },
    {
        "author": "Stephen Hawking",
        "quote": "The development of full artificial intelligence could " +
                    "spell the end of the human race… " +
                    "It would take off on its own, and re-design " +
                    "itself at an ever increasing rate. " +
                    "Humans, who are limited by slow biological evolution, " +
                    "couldn't compete, and would be superseded."
    },
    {
        "author": "Claude Shannon",
        "quote": "I visualize a time when we will be to robots what " +
                    "dogs are to humans, " +
                    "and I’m rooting for the machines."
    },
        {
        "author": "Elon Musk",
        "quote": "The pace of progress in artificial intelligence " +
                    "(I’m not referring to narrow AI) " +
                    "is incredibly fast. Unless you have direct " +
                    "exposure to groups like Deepmind, " +
                    "you have no idea how fast — it is growing " +
                    "at a pace close to exponential. " +
                    "The risk of something seriously dangerous " +
                    "happening is in the five-year timeframe." +
                    "10 years at most."
    },
    {
        "author": "Geoffrey Hinton",
        "quote": "I have always been convinced that the only way " +
                    "to get artificial intelligence to work " +
                    "is to do the computation in a way similar to the human brain. " +
                    "That is the goal I have been pursuing. We are making progress, " +
                    "though we still have lots to learn about " +
                    "how the brain actually works."
    },
    {
        "author": "Pedro Domingos",
        "quote": "People worry that computers will " +
                    "get too smart and take over the world, " +
                    "but the real problem is that they're too stupid " +
                    "and they've already taken over the world."
    },
    {
        "author": "Alan Turing",
        "quote": "It seems probable that once the machine thinking " +
                    "method had started, it would not take long " +
                    "to outstrip our feeble powers… " +
                    "They would be able to converse " +
                    "with each other to sharpen their wits. " +
                    "At some stage therefore, we should " +
                    "have to expect the machines to take control."
    },
        {
        "author": "Ray Kurzweil",
        "quote": "Artificial intelligence will reach " +
                    "human levels by around 2029. " +
                    "Follow that out further to, say, 2045, " +
                    "we will have multiplied the intelligence, " +
                    "the human biological machine intelligence " +
                    "of our civilization a billion-fold."
    },
    {
        "author": "Sebastian Thrun",
        "quote": "Nobody phrases it this way, but I think " +
                    "that artificial intelligence " +
                    "is almost a humanities discipline. It's really an attempt " +
                    "to understand human intelligence and human cognition."
    },
    {
        "author": "Andrew Ng",
        "quote": "We're making this analogy that AI is the new electricity." +
                    "Electricity transformed industries: agriculture, " +
                    "transportation, communication, manufacturing."
    }
    ]




    for record in ai_quotes:
        cursor.execute("INSERT INTO quotes (author, quote) VALUES (?, ?)",
                       (record["author"], record["quote"]))


    connection.commit()
    connection.close()





def get_db_connection():
    conn = sqlite3.connect('rest_api.db', timeout=10)
    conn.row_factory = sqlite3.Row
    return conn

def get_quote(quote_id):
    conn = get_db_connection()
    quote = conn.execute('SELECT * FROM quotes WHERE id = ?', (quote_id,)).fetchone()
    conn.close()
    return quote

def limit():
    conn = get_db_connection()
    limit_number = conn.execute('SELECT COUNT(*) FROM quotes;').fetchone()[0]
    return int(limit_number)


def create(author, quote):
    conn = get_db_connection()
    index = conn.execute('INSERT INTO quotes (author, quote) VALUES (?, ?)',
        (author, quote)).lastrowid
    conn.commit()
    conn.close()
    return index


def update(quote_id, author, quote):
    conn = get_db_connection()
    conn.execute('UPDATE quotes SET author=?, quote=? WHERE id=?',
        (author, quote, quote_id))
    conn.commit()
    conn.close()
    return 202

def delete(quote_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM quotes WHERE id=?', (quote_id,))
    conn.commit()
    conn.close()
    return 200






