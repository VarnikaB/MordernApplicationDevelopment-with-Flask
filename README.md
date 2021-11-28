# MordernApplicationDevelopment-with-Flask
Description<br />
Flashcard Application is used as a memory training. In this application, knowledge based on how well you know a language is tested. In this, there is a user login which is followed by a well-defined user dashboard. In the dashboard, there are multiple decks which the user creates. Each deck has multiple cards. The user will select the card, and talk about the difficulty level of card.
<br /><br />
Technologies used<br />
  &nbsp;&nbsp;  •	Flask<br />
   &nbsp;&nbsp; •	sqlite3<br />
   &nbsp;&nbsp; •	sqlalchemy<br />
   &nbsp;&nbsp; •	jinja2<br />
  &nbsp;&nbsp;  •	HTML/CSS, JS, Bootstrap<br /><br />
DB Schema Design<br />
  &nbsp;&nbsp;•	User<br />
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;○	username<br />
   &nbsp;&nbsp;&nbsp;&nbsp; ○	password<br />
   &nbsp;&nbsp;&nbsp;&nbsp; ○	name<br />
 &nbsp;&nbsp; ●	Decks<br />
   &nbsp;&nbsp;&nbsp;&nbsp; o	id<br />
   &nbsp;&nbsp;&nbsp;&nbsp; o	name<br />
 &nbsp;&nbsp; ●	Cards<br />
  &nbsp;&nbsp;&nbsp;&nbsp;  o	id<br />
  &nbsp;&nbsp;&nbsp;&nbsp;  o	question<br />
  &nbsp;&nbsp;&nbsp;&nbsp;  o	answer<br />
 &nbsp;&nbsp; ●	UserDeck<br />
&nbsp;&nbsp;&nbsp;&nbsp;    ○	username<br />
  &nbsp;&nbsp;&nbsp;&nbsp;  ○	deck_id<br />
  &nbsp;&nbsp;●	Deck_cards<br />
  &nbsp;&nbsp;&nbsp;&nbsp;  o	deck_id<br />
  &nbsp;&nbsp;&nbsp;&nbsp;  o	card_id<br /><br />
Architecture and Features<br />
The pages with respect to each user has a header and a footer. Header consists of the username and Flash Card Application name. With respect to each operation there is a page. For the cards learning, adding a new card, there is a new page. There are modals constructed for renaming a deck and deleting a deck.
In templates folder all the respective HTML files are stored which are accessed by the main.py file. In the applications folder all the api, controllers, views and database is stored.<br /><br />

To visit go to: https://Mad1-Final-Project.0110varnika.repl.co<br />

