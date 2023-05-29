<div align="center">

![ClimaCast](https://github.com/Cocomango-GH/ClimaCast/assets/111953271/d24becd1-ac2e-4ca7-a376-c2ca6411bf5e)

 Built by:[Sasha Amah](https://www.linkedin.com/in/sashaamah) 

# ClimaCast

![](https://img.shields.io/badge/Maintained%3F-yes-green.svg)
![Askme](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)
![Trello](https://img.shields.io/badge/Trello-0052CC?style=for-the-badge&logo=trello&logoColor=white) ![Miro](https://img.shields.io/badge/Miro-050038?style=for-the-badge&logo=Miro&logoColor=white)
![Git](https://img.shields.io/badge/GIT-E44C30?style=for-the-badge&logo=git&logoColor=white) ![GITHUB](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white)
![HEROKU](https://img.shields.io/badge/Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white)
![PYTHON](http://ForTheBadge.com/images/badges/made-with-python.svg) ![HTML](https://img.shields.io/badge/HTML-239120?style=for-the-badge&logo=html5&logoColor=white) 
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![BOOTSTRAP](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)

**_Click the following link to be redirected to the live version of the code!_** 

[ClimaCast](https://climacast.herokuapp.com/)

### Description:
ClimaCast is a Django-based web app that provides real-time weather forecasts and climate data for global locations. Users can easily search for weather information for any location and view details such as temperature, precipitation, wind speed, humidity, and more. Additionally, ClimaCast features an alert system that notifies users of severe weather conditions in their area. Its user-friendly interface, comprehensive data analysis, and real-time updates make ClimaCast a valuable tool for individuals, businesses, and researchers alike.



## :link: Associated Links:

[Trello](https://trello.com/b/yNp7Ak8P/kanban-template) 
[ERD](https://miro.com/welcomeonboard/cGZaVWh6cjZ3VE5aM1FRY245NVRMZzlHWXF4YlNGM2VnbThJU0RQVVpsaGU5YzFZMlZBdk9UY3h2QkJEV2F2U3wzNDU4NzY0NTUzNjMyODM5MDIwfDI=?share_link_id=231814706823) 
[Wireframes](https://miro.com/welcomeonboard/a1UzVzdTTXhGMkpyY1EyVUpydHJobXZCU0xVSEtGTXdwWk9hMFdMRUF2WU5PQlhIeTAxZ296akVramZrN2FrTXwzNDU4NzY0NTUzNjMyODM5MDIwfDI=?share_link_id=939025752006)


</div>

### gif 
https://github.com/Cocomango-GH/ClimaCast/assets/111953271/291a6520-e149-488d-bafe-ac31920d5b53


## Auth Page
<img width="1726" alt="Screen Shot 2023-05-15 at 8 45 22 AM" src="https://github.com/Cocomango-GH/ClimaCast/assets/111953271/84cc34a6-1a98-480f-8466-d2e79e9440fd">






### Forecast Page
<img width="1726" alt="Screen Shot 2023-05-15 at 8 44 57 AM" src="https://github.com/Cocomango-GH/ClimaCast/assets/111953271/eee9281e-85bd-4024-ada1-534b5dc8e223">



<div align="center">
 <h2> Technologies Used </h2>
</div>

<div align="center">

![Trello](https://img.shields.io/badge/Trello-0052CC?style=for-the-badge&logo=trello&logoColor=white) ![Miro](https://img.shields.io/badge/Miro-050038?style=for-the-badge&logo=Miro&logoColor=white)
![Git](https://img.shields.io/badge/GIT-E44C30?style=for-the-badge&logo=git&logoColor=white) ![GITHUB](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white)
![HEROKU](https://img.shields.io/badge/Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white)
![PYTHON](http://ForTheBadge.com/images/badges/made-with-python.svg) ![HTML](https://img.shields.io/badge/HTML-239120?style=for-the-badge&logo=html5&logoColor=white) 
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![BOOTSTRAP](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)

</div>



<div align="center">
 <h2> The Code Behind The Program:</h2>
</div>

```
@login_required
def home(request):
    weather_data = {}
    if request.method == 'POST':
        location = request.POST.get('location')
        api_key = os.environ['API_KEY']
        url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&appid={api_key}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather_data['location'] = data['name']
            weather_data['description'] = data['weather'][0]['description']
            weather_data['temperature'] = data['main']['temp']
            weather_data['humidity'] = data['main']['humidity']
            weather_data['wind_speed'] = data['wind']['speed']
            print(weather_data)
            # Save the weather data to the Location model
            location = Location.objects.create(user=request.user, location=location, temperature=weather_data['temperature'], humidity=weather_data['humidity'], wind_speed=weather_data['wind_speed'], last_updated=datetime.now())
            # Redirect to the forecast page with location data in the URL
        else:
            weather_data['error'] = f'Error getting weather data for {location}. Please try again.'

    return render(request, 'home.html', {'weather_data': weather_data})

```

<div align="center">
 <h2>:chart_with_upwards_trend: Looking Forward (Roadmap) </h2>
</div>

- [x]Display daily forecast
- [] Display 5 day forecast 
- [] Add favorite locations
- [] Display date for the location 
- [] Add photoss of weather 
- [] I want to be able to set my preferred temperature unit to Celsius or Fahrenheit

