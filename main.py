randomuser_data = {
    "results": [
        {
        "gender": "male",
        "name": {
            "title": "Mr",
            "first": "Atilla",
            "last": "Bennink"
        },
        "location": {
            "street": {
                "number": 7541,
                "name": "Hoveniersdreef"
            },
            "city": "Aalsmeerderbrug",
            "state": "Flevoland",
            "country": "Netherlands",
            "postcode": "3436 TI",
            "coordinates": {
                "latitude": "36.7507",
                "longitude": "-169.1103"
            },
            "timezone": {
                "offset": "+3:30",
                "description": "Tehran"}}}]} 
users = randomuser_data['results']
gender_count = {}
for user in randomuser_data['results']:
    gender = user['gender']
    gender_count[gender] = gender_count.get(gender, 0) + 1
print(gender_count)