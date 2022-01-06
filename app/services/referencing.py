from app.schemas.referencing import TextInfoResponse
from collections import Counter


class Referencing:

    def __init__(self, text):
        self.text = text

    async def get_text_info(self):
        hot_word = await self.get_hot_word()
        text = self.text.your_text
        words_list = text.split(" ")
        return TextInfoResponse(
            symbols=len(list(text)),
            symbols_w_w=len(list(text.replace(" ", ""))),
            words_count=len(words_list),
            sentences_count=len(text.split(".")),
            hot_word=hot_word,
            hot_word_count=words_list.count(hot_word)
        )

    async def get_hot_word(self):
        counter_list = Counter(self.text.your_text.split(" "))
        return sorted(counter_list, key=counter_list.get, reverse=True)[0]




