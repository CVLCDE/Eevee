from pokemontcgsdk import Set, Card

def get_all_cards_from_set(id: str) -> list[Card]:
    """
    Returns a list of all Card objects associated with a given set
    """
    return Card.where(q=f"set.id:{id}")


def get_prices_from_cards(card: Card) -> dict:
    tcgplayer_prices = card.tcgplayer.prices
    return {
        "normal": {
            "low": tcgplayer_prices.normal.low,
            "mid": tcgplayer_prices.normal.mid,
            "high": tcgplayer_prices.normal.high,
            "market": tcgplayer_prices.normal.market,
            "directLow": tcgplayer_prices.normal.directLow,
        }
    }


def organized_master_set() -> dict:
    """
    Returns a master dictionary of all pokemon card sets, ordered by id
    """
    master_set = {}
    for pkmn_set in Set.all()[::-1]:
        if pkmn_set.id not in master_set:
            master_set[pkmn_set.id] = {
                "set_name": pkmn_set.name,
                "set_logo": pkmn_set.images.logo,
                "set_symbol": pkmn_set.images.symbol,
                "set_count": pkmn_set.total,
                "set_cards": get_all_cards_from_set,
            }
    return master_set

def get_card_from_set(card_id) -> object:
    return Card.where(q=f"id:{card_id}")
