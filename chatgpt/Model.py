import os
from pyChatGPT import ChatGPT


class Model():
    def __init__(self, model_uri=""):
        self.loaded = False
        self.model_uri = model_uri

    def load(self):
        session_token = os.getenv("CHATGPT_TOKEN", default = None)
        try:
            self.model = ChatGPT(session_token)  # auth with session token
            self.loaded = True
        except:
            print("session_token error, please check your session_token.")
        

    def predict(self, X, feature_names = None, meta = None):
        if not self.loaded:
            self.load()
        print("Question: {}".format(X[0]))
        if self.loaded:
            resp = self.model.send_message(X[0])
            print("Answer: {}".format(resp['message']))
            return resp['message']
        else:
            return "ERROR"
