from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
app.static_folder = "static"


@app.route("/")
def scrape_function():
    # Fetch the webpage and parse it
    target_page = requests.get("https://www.boxingnews24.com/boxing-schedule/")
    soup = BeautifulSoup(target_page.text, "html.parser")

    content_divs = soup.find_all("div", class_="wprt-container")

    events_by_date = {}

    # For Loop that extracts fight data
    for card in content_divs:
        date = card.find("p").text.strip()

        p_tags = [p.text.strip() for p in card.find_all("p")]
        ul_tags = card.find_all("ul")

        event_lists = []

        for ul in ul_tags:
            event_list = [li.text.strip() for li in ul.find_all("li")]
            event_lists.append(event_list)

        events_by_date[date] = {"p": p_tags, "events": event_lists}

    # Pagination logic
    page = request.args.get("page", 1, type=int)
    per_page = 6
    total_fight_cards = sum(len(data["events"]) for data in events_by_date.values())
    start = (page - 1) * per_page
    end = start + per_page
    paginated_events = []

    for date, data in events_by_date.items():
        for event_list in data["events"]:
            paginated_events.append(
                {"date": date, "p": data["p"], "events": [event_list]}
            )

    paginated_events = paginated_events[start:end]

    # Render the index.html template with the paginated data
    return render_template(
        "index.html",
        events_by_date=paginated_events,
        page=page,
        per_page=per_page,
        total_fight_cards=total_fight_cards,
    )


@app.route("/mma")
def mma_scrape():
    # Fetch the webpage and parse it
    target_page = requests.get("https://www.mmafighting.com/schedule")
    soup = BeautifulSoup(target_page.text, "html.parser")

    content_divs = soup.find_all("div", class_="m-mmaf-pte-event-list")

    mma_events = {}

    for card in content_divs:
        title = card.find("h2").text.strip()
        date = card.find("h3").text.strip()
        streaming_info = card.find(
            "p", class_="m-mmaf-pte-event-list__tv-info"
        ).text.strip()
        mma_card = card.find_all("div", class_="m-mmaf-pte-event-list__split")

        mma_details = []

        for card_section in mma_card:
            mma_detail = [li.text.strip() for li in card_section.find_all("li")]
            mma_details.append(mma_detail)

        mma_events[date] = {
            "title": title,
            "date": date,
            "streaming_info": streaming_info,
            "mma_details": mma_details,
        }

    # Pagination logic
    page = request.args.get("page", 1, type=int)
    per_page = 6
    total_fight_cards = sum(
        len(mma_data["mma_details"]) for mma_data in mma_events.values()
    )
    start = (page - 1) * per_page
    end = start + per_page
    paginated_events = []

    for date, mma_data in mma_events.items():
        for mma_detail in mma_data["mma_details"]:
            paginated_events.append(
                {"date": date, "title": mma_data["title"], "mma_detail": mma_detail}
            )

    paginated_events = paginated_events[start:end]

    return render_template(
        "mma.html",
        mma_events=paginated_events,
        page=page,
        per_page=per_page,
        total_fight_cards=total_fight_cards,
    )


# Support Page
@app.route("/support")
def support():
    return render_template("support.html")


# 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)
