
def bot_response(message):
    if message == "hello":
        return "Hello there humanbeing!"
    elif message == "goodbye":
        return "Short circuit executed!"
    elif message == "Gimme image":
        import random
        image_url = "https://picsum.photos/200/300/?id=" + str(random.randint(1, 1000))
        return f'<img src="{image_url}">'
    elif message == 'help':
        return "1. To get a random image type 'Gimme image'.""2. To search for something in wikipedia type 'Tell me about....'""3. To find the weater in your location type 'weather in....'."    
    my_list = message.split(' ')
    if len(my_list) >= 4:
        search = my_list[3]
        if message == f'Tell me about {search}':
            reply = f"<a href='https://en.wikipedia.org/wiki/{search}'>https://en.wikipedia.org/wiki/{search}</a>"
            return reply
    elif len(my_list) < 4:
        import requests    
        city = my_list[2]
        if message == f'Weather in {city}':
            response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=59cbfb7e1ab794582f5c92629bbfc890&units=metric")
            if response.status_code == 200:
                data = response.json()
                temp = round(data['main']['temp'])
                reply = f'The tempereture in {city} is {temp}C'   
                return reply