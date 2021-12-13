# Sentiment-web-interface

This repo has two parts : Front & Back.
Each part has it's own readme.md that gives a small introduction.

### How to run the app ? 

Start by pulling the project to your own local machine;

Launch docker with Linux containers being up;

In a CLI, `cd` to the directory of this project where you'll find the `docker-compose.yml` file;

Then type the following command : 

```bash
docker-compose up -d
```

Afterwards the image will be up.

## How to test/use the app ?

In a CLI, type `ipconfig` then  get your `IPv4 address` of your wireless wifi network card;
As mentionned in the `docker-compose.yml` file, the web app's port is set to 3000, so connect to the address and try out our sentiment application ! 

HAVE FUN :) 
