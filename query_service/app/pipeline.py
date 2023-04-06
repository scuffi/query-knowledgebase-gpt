from loguru import logger as log

from datetime import datetime


from database import Database
from gpt import GPT
from vectoriser import Vectoriser
from prompt import Prompt

database = Database()
gpt = GPT()
vectoriser = Vectoriser()

def upload_context_pipeline(context: str):
    log.info(f"Uploading {context}")
    
    # Split into sentences
    sentences = vectoriser.sentencise_chunk(context)
    log.debug(f"Sentences: {sentences}")
    
    # Vectorise sentences
    vectorised_sentences = vectoriser.vectorise_sentences(sentences)
    log.debug(f"Vectors: {vectorised_sentences}")
    
    # Upload sentences to database
    log.info("Uploading vectors to database...")
    database.upload(vectorised_sentences)
    
def clear_database_pipeline():
    log.info("Clearing database...")
    database.clear()
    
def upload_question_pipeline(question: str):
    log.info(f"Answering {question}")
    
    # Vectorise question
    vectorised = vectoriser.vectorise_sentences([question])[0]
    log.debug(f"Vector: {vectorised}")
    
    # Query database for relating sentences
    relating_sentences = database.query(vectorised[1])
    log.debug(f"Related: {relating_sentences}")
    
    # If no relating context found, return error
    if not relating_sentences:
        return "[ERROR]: No knowledge found for this question!"
    
    # Create a prompt
    prompt = Prompt(
        "You are a fitness coach, tell me if this workout plan can be improved",
        context=' '.join(relating_sentences),
        workout_plan=question,
    )
    
    log.info(prompt.build())
    
    # Ask GPT question with found context
    output = gpt.query(prompt)
    log.debug(f"GPT Output: {output}")
    
    return output