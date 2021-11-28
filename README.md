# MordernApplicationDevelopment-with-Flask
Description<br />
Flashcard Application is used as a memory training. In this application, knowledge based on how well you know a language is tested. In this, there is a user login which is followed by a well-defined user dashboard. In the dashboard, there are multiple decks which the user creates. Each deck has multiple cards. The user will select the card, and talk about the difficulty level of card.
<br /><br />
Technologies used<br />
  •	Flask<br />
  •	sqlite3<br />
  •	sqlalchemy<br />
  •	jinja2<br />
  •	HTML/CSS, JS, Bootstrap<br /><br />
DB Schema Design<br />
  •	User<br />
    ○	username<br />
    ○	password<br />
    ○	name<br />
  ●	Decks<br />
    o	id<br />
    o	name<br />
  ●	Cards<br />
    o	id<br />
    o	question<br />
    o	answer<br />
  ●	UserDeck<br />
    ○	username<br />
    ○	deck_id<br />
  ●	Deck_cards<br />
    o	deck_id<br />
    o	card_id<br /><br />
Architecture and Features<br />
The pages with respect to each user has a header and a footer. Header consists of the username and Flash Card Application name. With respect to each operation there is a page. For the cards learning, adding a new card, there is a new page. There are modals constructed for renaming a deck and deleting a deck.
In templates folder all the respective HTML files are stored which are accessed by the main.py file. In the applications folder all the api, controllers, views and database is stored.<br /><br />

To visit go to: https://Mad1-Final-Project.0110varnika.repl.co<br />

