import os
from dotenv import load_dotenv
import tidalapi
from datetime import date, timedelta
import jinja2



load_dotenv()

token_type = os.getenv("TOKEN_TYPE")
access_token = os.getenv("ACCESS_TOKEN")
refresh_token = os.getenv("REFRESH_TOKEN")
expiry_time = os.getenv("EXPIRY_TIME")

session = tidalapi.Session()
session.load_oauth_session(token_type,access_token,refresh_token,expiry_time)

home = session.home()


prev = date.today().replace(day=1) - timedelta(days=1)
year = str(prev.year - 1)
month = prev.strftime('%B %Y')


for category in home.categories:
    if category.title == "Your listening history":
        for item in category.items:
            if item.title == year:
                print(item.title)
                last_year = item.get()
                last_year_thumbnail_url = last_year.image()
                tracks = last_year.items()
                last_year_tracks = []
                for i in range(0, 5):
                    last_year_tracks.append(tracks[i]._get(tracks[i].id))            
            elif item.title == month:
                print(item.title)
                last_month = item.get()
                last_month_thumbnail_url = last_month.image()
                tracks = last_month.items()
                last_month_tracks = []
                for i in range(0, 5):
                    last_month_tracks.append(tracks[i]._get(tracks[i].id))


environment = jinja2.Environment(loader=jinja2.FileSystemLoader("./"))
output_file = "README.md"
readme_template = environment.get_template("template.md")
context = {
    "last_month_tracks": last_month_tracks,
    "last_year_tracks": last_year_tracks,
    "last_month_img": last_month_thumbnail_url,
    "last_year_img": last_year_thumbnail_url
}
with open(output_file, mode="w") as output:
    output.write(readme_template.render(context))

