import abc
from pymkm.pymkm_helper import PyMkmHelper


class AbstractPriceCalculator(abc.ABC):
    @classmethod
    def calculate_price(cls, card_info: dict) -> float:
        raise NotImplementedError


class DefaultPriceCalculator(AbstractPriceCalculator):
    @classmethod
    def calculate_price(
        cls,
        is_foil: bool,
        is_playset: bool,
        condition: str,
        condition_discount: float,
        rounding_limit: float,
        card_info: dict,
        language_id: int,
        lang_increment: float,
    ) -> float:
        if not is_foil:
            trend_price = card_info["product"]["priceGuide"]["TREND"]
        else:
            trend_price = card_info["product"]["priceGuide"]["TRENDFOIL"]

        new_price = trend_price

        if new_price is None:
            raise ValueError("No price found!")
        else:
            if is_playset:
                new_price = 4 * new_price

            old_price = new_price
            # Apply condition discount
            if condition:
                new_price = new_price * condition_discount
            # Apply languge increment
            if language_id:
                new_price = new_price * lang_increment
            # Round
            new_price = PyMkmHelper.round_up_to_multiple_of_lower_limit(
                rounding_limit, new_price
            )

            return round(new_price, 2)
