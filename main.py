import wikipedia

def get_wikipedia_summary(query):
    try:
        summary = wikipedia.summary(query, sentences=3)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Sorry, there are multiple topics related to '{query}'. Could you be more specific?"
    except wikipedia.exceptions.HTTPTimeoutError:
        return "There seems to be a network issue. Please try again later."
    except wikipedia.exceptions.RedirectError:
        return "The requested topic seems to have a redirect. Try rephrasing your question."
    except Exception as e:
        return "I couldn't find any information on that topic. Sorry!"

topic = input("Ask me something: ")
response = get_wikipedia_summary(topic)
print(response)
