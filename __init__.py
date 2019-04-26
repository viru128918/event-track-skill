from mycroft import MycroftSkill, intent_file_handler


class EventTrack(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('track.event.intent')
    def handle_track_event(self, message):
        self.speak_dialog('track.event')


def create_skill():
    return EventTrack()

