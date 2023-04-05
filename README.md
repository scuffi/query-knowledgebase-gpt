# query-knowledgebase-gpt

This repository allows for super simple querying of predefined data using GPT.

## Usage

The software requires environment variables defined before it can function (the docker-compose.yml expects a .env file in the same directory):
```env
PINECONE_API_KEY=
PINECONE_ENVIRONMENT=
PINECONE_INDEX=

OPENAI_KEY=

OPENAI_API_TYPE=
OPENAI_API_BASE=
OPENAI_API_DEPLOYMENT=
```
[Pinecone](https://www.pinecone.io/) is a Vector database used to store the context embeddings. To use the program you must create a pinecone account, along with an index where your context will be stored. (If you are using a different provider it is worth noting the database must support 384 dimension vectors to be stored). *Fields other than OPENAI_KEY are optional, only required if you are using Azure*

[OpenAI](https://platform.openai.com/docs/api-reference?lang=python) is the provider of the GPT models. Aswell as pinecone, you must provide an API key from OpenAI to use. Other fields allow for access through Azure, however if you are using the OpenAI API, the configuration is as follows:

The program can be automatically started using docker compose:
```bash
docker compose up --build
```

Then head to `http://localhost:7860` in your browser and start playing around.

## Database

[Pinecone](https://www.pinecone.io/) offers a generous free tier, which is more than adequate for testing. If you wanted to use your own database provider, exchange the logic in database.py to interact with your custom client.

The context will persist throughout restarts, so if you never clear the database, you will build up a large array of context in your database. You can clear the database through the frontend using the 'Clear Database' button - this will remove EVERYTHING in the specified index.

## License

[MIT](https://choosealicense.com/licenses/mit/)