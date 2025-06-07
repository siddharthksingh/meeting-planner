# Meeting Planner

A minimal full-stack meeting scheduling app built with **FastAPI (backend)** and **React (frontend)**.

## Features

- Submit multiple users' busy schedules
- Suggest available common meeting slots based on given duration
- Book a slot and view updated calendars per user
- Show user's calendar (only accessible through Postman/docs)

## 🛠️ Tech Stack

| Layer       | Technology     |
|-------------|----------------|
| Backend     | FastAPI        |
| Frontend    | React          |

1. How exactly did you use AI while building this? List tools, prompts, successes, and failures.
\I devised the structure of the project and queried ChatGPT based on the required features. Didn't really face any failures as this was quite simple.

2. If given two more days, what would you refactor or add first, and why?
\The first thing I would do is Dockerize the whole project. That'll make it easier for anyone to be able to run the project on their machine. Another thing might be addition of a UI element to display user calendars. Currently it is only accessible through Postman/Docs.
