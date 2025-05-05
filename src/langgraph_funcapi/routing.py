from langgraph.func import entrypoint , task
from litellm import completion
import random

API_KEY = "your_api_key_here"  # Replace with your actual API key
model = "gemini/gemini-2.0-flash-exp"

@task
def math_handle(query):
    """Task to perform the mathematical operations"""
    response = completion(
        model = model,
        api_key = API_KEY,
        messages = [{
            "role":"user",
            "content":f"You are an expert mathematician and solve the following question {query}"
        }]
    )
    result = response["choices"][0]["message"]["content"]
    return result

@task
def writer(query):
    """Task to write the adept essay"""
    response=completion(
        model = model,
        api_key = API_KEY,
        messages = [{
            "role":"user",
            "content":f"You are an expert writer and write an essay of 100 words on the following topic {query}"
        }]
    )
    result = response["choices"][0]["message"]["content"]
    return result

@task
def translator(query):
    """Task to perform the translation of the given query"""
    response = completion(
       model = model,
       api_key = API_KEY,
       messages =
        [{
            "role":"user",
            "content":f"You are an expert translator and translate the following sentence in german {query} give a one liner translated output of the query only"
        }]
    )
    result = response["choices"][0]["message"]["content"]
    return result

@task
def choice(query):
    operations = ["math","writer","translator"]
    result = random.choice(operations)
    return result

@entrypoint()
def router_call(input_data):
    category = choice(input_data).result()
    if category == "math":
        return math_handle(input_data["query"]).result()
    elif category == "writer":
        return writer(input_data["query"]).result()
    else :
        return translator(input_data["query"]).result()
    
    return {
        "query":input_data["query"],
        "category" : category,
        "response" : response
    }


def main():
    input_data = {"query":"I am Saim"}
    result = router_call.invoke(input_data)
    print("OUTPUT",result)
    