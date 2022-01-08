from app.schemas.referencing import TextInfoResponse, ReferencingResponse
from collections import Counter, ChainMap


class Referencing:

    def __init__(self, text):
        self.text = text
        self.alliances = ("in", "and", "on", "the", "a", "и", "или", "на", "в")

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

    async def referencing_text(self):
        text = self.text.your_text
        most_common_words = dict(ChainMap(*[{item[0]: item[1]} for item in Counter(text.split(" ")).most_common(5)
                                            if item[0] not in self.alliances]))
        words_list = text.split(" ")
        hot_word = await self.get_hot_word()
        res = []
        for item in text.split("."):
            appending = False
            for word in item.split(" "):
                if word in most_common_words.keys():
                    appending = True
            if appending:
                res.append(item)
        sentences_count = len(text.split("."))
        text_water = (len(res) / sentences_count) * 100
        return ReferencingResponse(
            symbols=len(list(text)),
            symbols_w_w=len(list(text.replace(" ", ""))),
            words_count=len(words_list),
            sentences_count=sentences_count,
            hot_word=hot_word,
            hot_word_count=words_list.count(hot_word),
            hot_words=most_common_words,
            text_water=f"{str(100 - text_water)}%",
            new_text=".".join(res)
        )
