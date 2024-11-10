# tidal-readme

Github README Tidal Integration

## What I've been listening to

### Last month

| Track | Artist |
| :-: | :-: |
{% for track in last_month_tracks %}
| {{track.name}}| {{track.artist.name}}|
{% endfor %}

### Last year

| Track | Artist |
| :-: | :-: |
{% for track in last_year_tracks %}
| {{track.name}}| {{track.artist.name}}|
{% endfor %}
