# tidal-readme

Github README Tidal Integration

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
