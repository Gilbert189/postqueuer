# postqueuer
A simple post queuer bot for the TBGs.

Oh, would you look a that. A bot that's used to break rules has now transformed into a useful post queuer.

Uses [celery](https://github.com/celery/celery) to queue posts. You might need to read the repo.

Once run, postqueuer will use these environment variables:
```
TBGS_USERNAME: The bot's username
TBGS_PASSWORD: The bot's password
QUEUER_BROKER: The queuer's message broker (the place to send commands)
QUEUER_BACKEND: The queuer's backend (where the result of commands get sent in)
```