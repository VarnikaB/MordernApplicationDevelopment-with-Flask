# MordernApplicationDevelopment-with-Flask
Description
Flashcard Application is used as a memory training. In this application, knowledge based on how well you know a language is tested. In this, there is a user login which is followed by a well-defined user dashboard. In the dashboard, there are multiple decks which the user creates. Each deck has multiple cards. The user will select the card, and talk about the difficulty level of card.
Technologies used
•	Flask
•	sqlite3
•	sqlalchemy
•	jinja2
•	HTML/CSS, JS, Bootstrap
DB Schema Design
  •	User
    ○	username
    ○	password
    ○	name
  ●	Decks
    o	id
    o	name
  ●	Cards
    o	id
    o	question
    o	answer
  ●	UserDeck
    ○	username
    ○	deck_id
  ●	Deck_cards
    o	deck_id
    o	card_id
Architecture and Features
The pages with respect to each user has a header and a footer. Header consists of the username and Flash Card Application name. With respect to each operation there is a page. For the cards learning, adding a new card, there is a new page. There are modals constructed for renaming a deck and deleting a deck.
In templates folder all the respective HTML files are stored which are accessed by the main.py file. In the applications folder all the api, controllers, views and database is stored.

To visit go to: https://Mad1-Final-Project.0110varnika.repl.co

