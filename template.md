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

Customize `template.md` to your heart's content and dig into [python-tidal](https://github.com/tamland/python-tidal) to pull some playlists of your own!

### Environmental Variables

Get these using `init_auth.py`:

- TOKEN_TYPE
- ACCESS_TOKEN
- REFRESH_TOKEN
- EXPIRY_TIME

## What I've been listening to

### Last month

![Last Month]({{last_month_img}})

| Track | Artist |
| :-: | :-: |
{% for track in last_month_tracks -%}
| {{track.name}} | {{track.artist.name}} |
{% endfor %}

### Last year

![Last Year]({{last_year_img}})

| Track | Artist |
| :-: | :-: |
{% for track in last_year_tracks -%}
| {{track.name}} | {{track.artist.name}} |
{% endfor %}
