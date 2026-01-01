# tidal-readme :headphones:

Github README Tidal Integration
Show off your most listened to music on your GitHub profile!

## Usage

You MUST set your environmental variables to authenticate with Tidal for this to work.

- Run `python init_auth.py` and copy the printed link into a browser to authenticate with your Tidal account.
- Save the tokens into a `.env` file or your repository secrets on GitHub to use with GitHub Actions.
- Run `python app.py` using the GitHub Actions workflow or locally to render the README template.

Make sure you do not commit the tokens to your repository.
The GitHub Action workflow is configured to run on a push event or on the first of every month.
Don't forget to change your repository settings to allow Workflows read **and write** permissions!
*Found under Actions &rarr; General in repository settings on GitHub.*

Customize `template.md` to your heart's content and dig into [python-tidal](https://github.com/tamland/python-tidal) to pull some playlists of your own!

### Environmental Variables

Get these using `init_auth.py`:

- TOKEN_TYPE
- ACCESS_TOKEN
- REFRESH_TOKEN
- EXPIRY_TIME

## What I've been listening to

### Last month

![Last Month](https://images.tidal.com/0/EIsCGIsCIKABKKAB/CAEQBRokN2E1NDQwNmYvYTBjZi80MTZjLzhiYjAvMjgyZjFkOTU2Njg1IhBNeSBNb3N0IExpc3RlbmVkIghERUNFTUJFUioHI0E1RTNGRjAE?token=60cbcf401fa72516f626b040b28565154547d6c7)

| Track | Artist |
| :-: | :-: |
| When A Good Man Cries | CMAT |
| Cobra | Geese |
| Potion | Djo |
| Lonely Cosmos | King Gizzard & The Lizard Wizard |
| Avalanche | Snocaps |


### Last year

![Last Year](https://resources.tidal.com/images/rewind_icon_2025_267.jpg?rewind2025)

| Track | Artist |
| :-: | :-: |
| Add Up My Love | Clairo |
| Thinking About You | Faye Webster |
| Loretta | Ginger Root |
| Show Me How | Men I Trust |
| Good Grief | Dr. Dog |
