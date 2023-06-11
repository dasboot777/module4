import  wikipedia

def get_article(article):
    wikipedia.set_lang("ru")
    try:
        response = wikipedia.summary(article)
    except wikipedia.WikipediaException:
        response = "Ничего не нашлось"
    return response