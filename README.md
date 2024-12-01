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

![Last Month](https://images.tidal.com/0/EIsCGIsCIKABKKAB/CAEQBRokZTJlODJjNTMvZDVmOC80ODU2L2E3ZTMvZTY5MjNhYWViZTNlIhBNeSBNb3N0IExpc3RlbmVkIghOT1ZFTUJFUioHI0ZDQUVEODAE?token=dd317d021fd917cda03b8382badcf10e092e0d0c)

| Track | Artist |
| :-: | :-: |
| Add Up My Love | Clairo |
| Red Wine Supernova | Chappell Roan |
| Thinking About You | Faye Webster |
| Hot Rod | Dayglow |
| From The Start | Laufey |


### Last year

![Last Year](https://images.tidal.com/0/EIsCGIsCIKABKKAB/CAEQBBokNjU1OWEzMjkvYmE0Ny80MDczLzljNTYvMjdhMDM4NDIyZDU2GiQ5MDA4ZjJkNS9kMDM0LzRjYTkvODM2ZC83Yzg2NjQwNjkwZDUaJDhjZWVkYTI1LzZkYjcvNDI5Ny9hZjZiLzhkZDEyMjNjNWYwYiIQTXkgTW9zdCBMaXN0ZW5lZCIEMjAyMyoHI0Y5QTE5MjAD?token=913aec29605d10ed168e3e4547cee76595f16406)

| Track | Artist |
| :-: | :-: |
| Sarah | Alex G |
| Impossible Germany | Wilco |
| Write A List of Things To Look Forward To | Courtney Barnett |
| After The Earthquake | Alvvays |
| Watching Strangers Smile | Parquet Courts |
