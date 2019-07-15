class VideoApp:
    participants_online=0
    action=['speaking','silent']

    def __init__(self,user_name,company):
        self.user_name=user_name
        self.company=company

    @classmethod
    def show_participants_online(cls):
        return(print(f"participants are attending the meeting {cls.participants_online}"))

    @classmethod
    def go_online(cls):
        cls.participants_online=cls.participants_online+1
        return cls.participants_online

    @classmethod
    def go_offline(cls):
        cls.new_participants_online=cls.participants_online-1
        return cls.new_participants_online

    def status(self,action):
        if action in VideoApp.action:
            return print(f'{self.user_name} is in action')
        else:
            raise ValueError("speaking or silent")
            #return f'{self.username}'


class Message:

    def __init__(self, user_name, message):
        self.username = user_name
        self.message = message

    def __status(self):
        print(f'{self.user_name} sent the message: {self.message}')



class ChatApp(VideoApp,Message):

    def __init__(self,user_name,message,company):
        VideoApp.__init__(self,user_name,company)
        Message.__init__(self,user_name,message)
        #print("i am init of chatapp")




c1 = ChatApp('keerthana', 'welcome', 'integrify')
print(c1.go_online())
c1.show_participants_online()
print(c1.go_offline())
c1.status('silent')
c1._Message__status()  #to call the __status explicilty you have to write like this



