import cassiopeia as cass
from cassiopeia import Summoner


def print_rune_pages(summoner_name: str, region: str):
    summoner = Summoner(name=summoner_name, region=region)
    print("Name:", summoner.name)
    print("ID:", summoner.id)

    # pages = cass.get_rune_pages(summoner)
    pages = summoner.rune_pages
    for page in pages:
        print(page.name)

    page = pages[0]
    for rune, count in page.runes.items():
        print(rune.name, count)


if __name__ == "__main__":
    print_rune_pages("Kalturi", "NA")
