import json

class Response_email:
    def __init__(self, not_phishing, phishing, message):
        self.not_phishing = not_phishing
        self.phishing = phishing
        self.message = message

    def check_percentage(self):
        if(self.phishing > 0.3 and self.phishing < 0.5):
            return "Suspect email be carefull"
        elif (self.phishing >= 0.5):
            return "Phishing email detected"
        else:
            return "Clear email"

    def to_string(self):
        print("Not Phishing {}%".format(self.not_phishing))
        print("Phishing {}%".format(self.phishing))
        print("Message {}%".format(self.message))

    def to_json(self):
        obj = {
            "not_phishing" : self.not_phishing,
            "phishing" : self.phishing,
            "message" : self.check_percentage(),
            }
        
        json_obj = json.dumps(obj)
        return json_obj

