import spacy
from app.services.nlp import SmNlpModel, MdNlpModel


def get_sm_nlp_model():
    return SmNlpModel(spacy.load("en_core_web_sm"))


def get_md_nlp_model():
    return MdNlpModel(spacy.load("en_core_web_md"))
