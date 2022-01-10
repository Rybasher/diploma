from typing import List, Dict, Any

import spacy
import numpy as np
from spacy import displacy
import textacy.extract

from app.schemas.nlp import NlpEntitiesResponse, UpdatePattern


class NlpBase:

    def __init__(self, nlp):
        self.nlp = nlp

    async def get_doc(self, text: str):
        return self.nlp(text)

    async def get_text_with_entities(self, text: str) -> NlpEntitiesResponse:
        doc = await self.get_doc(text)
        return NlpEntitiesResponse(
            text=await self.get_text_entities(doc=doc),
            ent_proc=await self.get_entities_perc(doc=doc)
        )

    @staticmethod
    async def get_text_entities(doc):
        return " ".join([f"{token.text}({token.ent_type_})" if token.ent_type_ else f"{token.text}"
                         for token in doc])

    @staticmethod
    async def get_entities_perc(doc):
        return f"{(len(doc.ents) / len(doc)) * 100}%"

    async def get_text_entities_with_updated_pattern(self, text: str, pattern: UpdatePattern):
        ruler = self.nlp.add_pipe("entity_ruler", before="ner")
        ruler.add_patterns([pattern.dict()])
        doc = self.nlp(text)
        return NlpEntitiesResponse(
            text=await self.get_text_entities(doc=doc),
            ent_proc=await self.get_entities_perc(doc=doc)
        )

    async def get_fact(self, text: str, word: str):
        doc = self.nlp(text)
        uniqueStatements = set()
        for cue in ["is", "has"]:
            statements = textacy.extract.semistructured_statements(doc, entity=word, cue=cue)
            for st in statements:
                uniqueStatements.add(st)

        result = []
        for statement in uniqueStatements:
            subject, verb, fact = statement
            result.append(fact)
        breakpoint()
        return result


class SmNlpModel(NlpBase):
    ...


class MdNlpModel(NlpBase):
    ...
