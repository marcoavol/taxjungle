# TaxJungle
## Project

Taxjungle was the final project three fellow students and I built during the last two-and-a-half weeks of the full-stack developer bootcamp at Propulsion Academy, Zurich.

The project opportunity was provided by Keen Innovation AG, a company located in Basel, Switzerland, that provides forward-thinking digital solutions for unsolved customer problems in the local and global FinTech ecosystem. With Taxjungle (www.taxjungle.ch) Keen Innovation AG wants to help the roughly 40k foreigners moving to Switzlerand every year to choose their place of living by offering super intuitive tools and thereby build a relationship with the users that eventually leads to them becoming customers of BKB or Bank Cler.

Our goal was to rebuild the existing functionality from scratch (except the API providing the swiss taxation data) while improving it wherever possible and adding a new social component to it that allows for interaction with the users and providing informative content on various finance-related topics. For the interactive map we decided to do it purely with D3 (instead of using tools like datawrapper) to create as little dependencies as possible and allow for greater customization and future inclusion of additional data layers (for example average renting prices).

## Features

* Interactive map of Switzerland that allows for calculation (based on individual configuration) and comparison of expected taxation rates between cantons and municipalities

* Blog component that allows for creating, commenting and sharing articles for different finance related categories/topics (including a search functionality)

* User authentication and profiles

## Tech-Stack

* Javascript, React, Redux, D3 (Frontend)

* Python, Django (Backend)

* Postgres (Database)

* Digital Ocean, Docker, Nginx (Deployment)

* Gitlab, Gitlab-Runner (CI/CD)

## Screenshots
![map](/screenshots/map2.png?raw=true)
![map](/screenshots/map1.png?raw=true)
![map](/screenshots/map3.png?raw=true)
![map](/screenshots/map4.png?raw=true)
![map](/screenshots/authentication.png?raw=true)
![map](/screenshots/blog1.png?raw=true)
![map](/screenshots/blog2.png?raw=true)
![map](/screenshots/blog3.png?raw=true)
![map](/screenshots/profile.png?raw=true)

## Credits

This project was developed in collaboration between Propulsion Academy AG (https://propulsion.academy) and Keen Innovation AG (https://keen-innovation.ch).

The geological map data is provided by Swisstopo (https://www.swisstopo.admin.ch/) and the conversion to TopoJSON format was done with Swiss Maps Generator (https://swiss-maps.vercel.app) by Interactive Things (https://www.interactivethings.com).
