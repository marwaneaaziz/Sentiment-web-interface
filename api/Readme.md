This is a [Flask](https://flask.palletsprojects.com/en/2.0.x/)  Restful Api that loads [VaderSentimentAnalyzer](https://github.com/cjhutto/vaderSentiment)

## Getting Started

The Api is launched with the  'app.py' script, it is served Open [http://localhost:5000](http://localhost:5000) 

## Tests

### Unit tests

In order to test this script, you can execute unit tests by running :

```bash
pytest
```
This will launch 'tests/test_predict.py' you can change the input in 'samples/text.json'.

### Integration tests

In order to do integration tests you must first launch the Api with the script 

```bash
app.py
```

You can then do integration tests by using  [Postman](https://www.postman.com/), you can access the Api by sending a Post request,
to the port  [http://localhost:5000/predict](http://localhost:5000/predict), the body of the request must be of Json type and 
follows this format : 

```json
{ "text": "The text you want to analyse" }
```

## Learn More

To learn more about Flask, take a look at the following resources:

- [Flask Documentation](https://flask.palletsprojects.com/en/2.0.x/#user-s-guide) - learn about Flask features and API.

To learn more about Postman, take a look at the following resources : 

- [Learn Postman](https://learning.postman.com/docs/getting-started/introduction/) - learn about Postman.

