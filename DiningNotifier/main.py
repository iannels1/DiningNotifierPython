import os
import time

import requests

from emailHelper import send_email
from variables import target_categories, locations, liked_foods, headers, base_URL

today_food = []

all_foods = []  # replace with a db at some point as this should be persistent

location_hours = []


# This works, but I have the striking suspicion that this can be more efficient
# and not create 1000 of essentially the same thing
def get_foods_from_menus(all_data):
    menus = all_data[0].get("menus")
    location = all_data[0].get("slug")

    if not menus or not location:
        return

    for menu in menus:

        section = menu.get("section", "")
        menu_displays = menu.get("menuDisplays", [])

        for menuDisplay in menu_displays:
            categories = menuDisplay.get("categories", [])

            for category in categories:

                if category.get("category", "") in target_categories:

                    for menu_item in category.get("menuItems", []):

                        name = menu_item.get("name", "")
                        food = {
                            "name": name,
                            "location": location,
                            "meal": section
                        }

                        if name not in all_foods:
                            all_foods.append(name)

                        today_food.append(food)


def notify(food: dict):
    food_name = food.get("name", "")
    location = food.get("location", "")
    meal = food.get("meal", "")
    start_time = ""
    end_time = ""

    for location_day in location_hours:
        for location_meal in location_day.get("hours"):
            if meal == location_meal.get("name") and location == location_day.get("location"):
                start_time = location_meal.get("start_time", "")
                end_time = location_meal.get("end_time", "")

    body = f"{food_name} at {location} for {meal} from {start_time} to {end_time}"

    send_email(os.environ["receiver"], body)
    print(f"email sent, body: {body}")


def check_and_notify_if_liked_food_is_on_menu():
    for food in today_food:
        if food.get("name", "") in liked_foods:
            notify(food)


def clear_all():
    today_food.clear()
    all_foods.clear()
    location_hours.clear()



def main():
    send_email(os.environ["receiver"], "program started")
    while True:
        all_menus = []

        for location in locations:
            url = base_URL % location

            response = requests.get(url, headers=headers)
            response.raise_for_status()
            all_data = response.json()

            location_hours.append({"location": location,
                                   "hours": all_data[0].get("todaysHours", "")
                                   })

            get_foods_from_menus(all_data)

            all_menus.append(all_data)

        check_and_notify_if_liked_food_is_on_menu()

        clear_all()

        print("day finished")

        time.sleep(86400)


if __name__ == '__main__':
    main()
