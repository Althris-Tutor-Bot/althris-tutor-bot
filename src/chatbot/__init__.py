from nltk.stem.lancaster import LancasterStemmer
from nltk.stem.snowball import SnowballStemmer


class Chatbot:
    # def __init__(self, url="https://omvtjpr4t5etnbcajn76gkclzq.appsync-api.eu-west-1.amazonaws.com/graphql"):
    def __init__(self):
        # self.lancaster_stemmer = LancasterStemmer()
        self.snowball_stemmer = SnowballStemmer("english")
        self.dataset, self.wordbank, self.tags, self.training, self.output = [], [], [], [], []
        self.net, self.model = None, None
        # self.languages, self.languages_lower, self.categories = [], [], []
        # self.session = requests.Session()
        # self.session.auth = AWS4Auth(
        #     "AKIAQSQV6DKCDQZX7K73",
        #     "8aXACUDGdzE5iRJ2QpRxyb0xrn9Ol2rdv1tggXyT",
        #     "eu-west-1",
        #     "appsync"
        # )
        # self.endpoint = url
        self.load_data()
        self.load_model()

    # def api_query(self, query):
        """
        A simple one liner method that takes in a graphql query as a multiline string and returns the result,
        automatically dealing with the endpoint, the API key and the conversion from a Request object to json.
        """
    #     return self.session.request(url=self.endpoint, json={"query": query}, method="POST").json()

    from .load_data import load_data
    """
    imports load_data method into the class. The dot character signifies "import from the package that has been created 
    inside this directory using an __init__.py file. The first "load_data" (right after the dot) signifies that it Should
    import from load_data.py, and the last is the "load_data" method inside "load_data.py". The load_data.py method takes 
    in one argument (self) and modifies it, returning nothing. This is equivalent to having the method inside the class
    and having the whole package in one file (simply as a module), but the file would be very long.
    """
    from .load_models import load_model
    from .bag_of_words import bag_of_words
    from .get_response import get_response



