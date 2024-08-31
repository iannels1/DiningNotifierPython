import json

import requests

from Resources.variables import target_categories, locations, liked_foods, headers, base_URL

today_food = []

all_foods = []  # replace with a db at some point as this should be persistent


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
                            "section": section
                        }

                        if name not in all_foods:
                            all_foods.append(name)

                        today_food.append(food)


def notify():
    #TODO
    pass


def check_and_notify_if_liked_food_is_on_menu():
    for food in today_food:
        if food.get("name", "") in liked_foods:
            notify()

    today_food.clear()


def main():
    all_menus = []

    for location in locations:
        url = base_URL % location

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
