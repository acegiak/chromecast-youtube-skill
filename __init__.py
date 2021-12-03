from mycroft import MycroftSkill, intent_file_handler


class ChromecastYoutube(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('youtube.chromecast.intent')
    def handle_youtube_chromecast(self, message):
        self.speak_dialog('youtube.chromecast')


def create_skill():
    return ChromecastYoutube()

