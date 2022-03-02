from ..config.db import mongo
from ..tools.ptcg_sdk import get_card_from_set

db = mongo.db


class OwnedCardsModel:
    def get_all_cards(self) -> list:
        """
        Returns all documents found within the database's owned_cards collection
        """
        print(f"Getting all owned cards.")
        return [document for document in db["owned_cards"].find({})]

    def get_card(self, card_id) -> object:
        """
        Returns the document specified at 'card_id' in the database's owned_cards collection
        """
        if db["owned_cards"].find_one({"card_id": card_id}):
            print(f"Card: {card_id} found!")
            return db["owned_cards"].find_one({"card_id": card_id})
        else:
            print(f"Card: {card_id} not found")
            return None

    def add_card(self, card_id):
        """
        Adds a new card to the database's owned_cards collection
        """
        if self.get_card(card_id) is None:
            card_obj = get_card_from_set(card_id)
            formatted_card_obj = {
                "card_id": card_obj[0].id,
                "card_name": card_obj[0].name,
                "card_image": card_obj[0].images.small,
                "prices": self.get_price_data(card_obj[0])
            }
            db["owned_cards"].insert_one(formatted_card_obj)
            print(f"Added {card_id} to owned_cards database.")
        else:
            print(f"Cannot add to owned_cards database: {card_id} already exists.")

    def remove_card(self, card_id):
        """
        Removes a card from the database's owned_cards collection
        """
        if self.get_card(card_id) is not None:
            print(f"Removing {card_id} from owned_cards database.")
            db["owned_cards"].delete_one({"card_id": card_id})
        else:
            print(
                f"Cannot remove card from owned_cards database: {card_id} does not exist."
            )

    def get_price_data(self, card_obj):
        prices = {
            "normal": card_obj.tcgplayer.prices.normal,
            "holofoil": card_obj.tcgplayer.prices.holofoil,
            "reverseHolofoil": card_obj.tcgplayer.prices.reverseHolofoil,
            "firstEditionHolofoil": card_obj.tcgplayer.prices.firstEditionHolofoil,
            "firstEditionNormal":card_obj.tcgplayer.prices.firstEditionNormal
        }
        relevant_prices = {}

        for card_type, price in prices.items():
            if price is not None:
                relevant_prices[card_type] = price.market
        
        return relevant_prices

