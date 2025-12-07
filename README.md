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

![Last Month](https://images.tidal.com/0/EIsCGIsCIKABKKAB/CAEQBRokMDEwNmExZTAvY2IwZC80ZThjL2JkMmMvN2ViMGVkNTNiOTZjIhBNeSBNb3N0IExpc3RlbmVkIghOT1ZFTUJFUioHI0E4RjdDMjAE?token=3fb9cafcdb64233b921e745d484ae67cafca863c)

| Track | Artist |
| :-: | :-: |
| Cherry Hard Candy | Snocaps |
| Avalanche | Snocaps |
| Heathcliff | Snocaps |
| Coast | Snocaps |
| You In Rehab | Snocaps |


### Last year

![Last Year](https://images.tidal.com/0/EIsCGIsCIKABKKAB/CAEQBBokNGQ3ZTVmZGIvZjNmMi80MmQwL2FkNGUvMzMwZDE4ZGFmNjRhGiQyODcxMTM0Mi83NDRiLzQ3MDUvYWMzNC9kN2MxNjVhNzVhMTUaJDNiZDYxOGJlLzZkMTIvNDA1ZS84MjBjLzNmNjQ4OTM3ZDk4MiIQTXkgTW9zdCBMaXN0ZW5lZCIEMjAyNCoHI0E1RTNGRjAD?token=c7fc1191a1c724151271c45e245942903bd523fa)

| Track | Artist |
| :-: | :-: |
| Angelica | Wet Leg |
| Expert In A Dying Field | The Beths |
| All I Do | Bully |
| Shotgun | Soccer Mommy |
| Add Up My Love | Clairo |
