

base_URL = "https://dining.iastate.edu/wp-json/dining/menu-hours/get-single-location/?slug=%s&time="
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}
locations = ["seasons-marketplace-2-2",
             "conversations-2",
             "union-drive-marketplace-2-2",
             "friley-windows-2-2"]

liked_foods = ["Smoked Brisket"]

target_categories = ["Entree",
                     "Pasta Bar",
                     "Sides",
                     "Soups",
                     "Pizza"]

smpt_server = "smtp.gmail.com:587"
