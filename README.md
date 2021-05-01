description:
Using the Nutritionix natural language exercise API. Nutritionix allows you to input exercises using plain english and it returns a json structured version of your input, plus the estimated calories you burned.



useful documentation:
![Nutritionix API v2 Documentation](https://docs.google.com/document/d/1_q-K-ObMTZvO0qUEAxROrN3bwMujwAN25sLHwJzliK0/edit#heading=h.73n49tgew66c)

input:
```json
    post = {
        "query": "ran 5 kms, walked 2 km",
        "gender": "male",
        "weight_kg": 80.5,
        "height_cm": 173,
        "age": 40
    }
```

output:
```json
{
  "exercises": [
    {
      "tag_id": 317,
      "user_input": "ran",
      "duration_min": 31.08,
      "met": 9.8,
      "nf_calories": 408.65,
      "photo": {
        "highres": "https://d2xdmhkmkbyw75.cloudfront.net/exercise/317_highres.jpg",
        "thumb": "https://d2xdmhkmkbyw75.cloudfront.net/exercise/317_thumb.jpg",
        "is_user_uploaded": false
      },
      "compendium_code": 12050,
      "name": "running",
      "description": null,
      "benefits": null
    },
    {
      "tag_id": 100,
      "user_input": "walked",
      "duration_min": 24.85,
      "met": 3.5,
      "nf_calories": 116.69,
      "photo": {
        "highres": "https://d2xdmhkmkbyw75.cloudfront.net/exercise/100_highres.jpg",
        "thumb": "https://d2xdmhkmkbyw75.cloudfront.net/exercise/100_thumb.jpg",
        "is_user_uploaded": false
      },
      "compendium_code": 17190,
      "name": "walking",
      "description": null,
      "benefits": null
    }
  ]
}

```
