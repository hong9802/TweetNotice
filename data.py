import datetime

class Data:
    def __init__(self):
        temp = str(datetime.datetime.now(datetime.timezone.utc))
        temp = temp[:temp.find(".")]
        self.alert_time = datetime.datetime.strptime(temp, "%Y-%m-%d %H:%M:%S")

    def get_time(self, created_at):
        result = datetime.datetime.strptime(created_at, "%a %b %d %H:%M:%S +0000 %Y")
        return result

    def update_time(self, new_time):
        self.alert_time = new_time

    def get_alert_time(self):
        return self.alert_time