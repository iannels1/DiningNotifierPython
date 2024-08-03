import json

import requests

baseURL = "https://dining.iastate.edu/wp-json/dining/menu-hours/get-single-location/?slug=%s&time="
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}
locations = ["seasons-marketplace-2-2",
             "conversations-2",
             "union-drive-marketplace-2-2",
             "friley-windows-2-2"]

todays_food = []
liked_foods = ["Cheese Pizza",
               "Pepperoni Pizza"]

all_foods = []  # replace with a db at some point as this should be persistent

breakfast = []
brunch = []  # not sure what place has brunch
lunch = []
dinner = []
late_night = []

meals = [
    breakfast,
    brunch,
    lunch,
    dinner,
    late_night
]


def get_foods_from_menus(all_data):
    menus = all_data.get("menus")
    location = all_data.get("slug")

    if not menus or not location:
        return

    if location is locations[0]:  # seasons
        # breakfast, lunch, dinner
        pass

    if location is locations[1]:  # convos
        # lunch, dinner, late night
        pass

    if location is locations[2]:  # udcc - I only know these mappings atp
        # breakfast, lunch, dinner

        for menu in menus:

            section = menu.get("section", "")
            menuDisplays = menu.get("menuDisplays", [])

            for menuDisplay in menuDisplays:
                pass



        pass

    if location is locations[3]:  # windows
        # lunch, dinner, late night
        pass

    # if menu.get("section", "") is "breakfast":
    #     menu.get("menuDisplays", [])
    # if menu.get("section", "") is "brunch":
    #     pass
    # if menu.get("section", "") is "lunch":
    #     pass
    # if menu.get("section", "") is "dinner":
    #     pass
    # if menu.get("section", "") is "late_night":
    #     pass


def notify():
    pass


def check_and_notify_if_liked_food_is_on_menu():
    for food in todays_food:
        if food in liked_foods:
            notify()


def main():
    all_menus = []

    for location in locations:
        url = baseURL % location

        response = requests.get(url, headers=headers)
        response.raise_for_status()
        all_data = response.json()

        if not all_data:
            continue

        get_foods_from_menus(all_data)

        all_menus.append(all_data)

    check_and_notify_if_liked_food_is_on_menu()


if __name__ == '__main__':
    main()
