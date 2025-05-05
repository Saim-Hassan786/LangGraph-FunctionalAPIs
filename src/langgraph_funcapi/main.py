from dotenv import load_dotenv , find_dotenv
from langgraph.func import task, entrypoint
from langchain_google_genai import ChatGoogleGenerativeAI
from litellm import completion


# _:bool = load_dotenv(find_dotenv())

API_KEY = "your_api_key_here"  # Replace with your actual API key


@task
def generate_random_city(country:str)->str:
    """Generate a random city Using the LLM Call"""

    response = completion(
        model="gemini/gemini-2.0-flash-exp",
        api_key=API_KEY,
        messages=[
            {"role":"user","content":f"Return the name of a City name from {country}"}
        ]
    )
    random_city = response["choices"][0]["message"]["content"]
    return random_city


@task
def generate_fun_fact(city:str)->str:
    """Generate a fun fact about the given city using LLM call"""

    response = completion(
    model="gemini/gemini-2.0-flash-exp",
    api_key=API_KEY,
    messages=[
        {"role":"user","content":f"Return a fun fact of a {city}"}
        ]
    )
    fun_fact = response["choices"][0]["message"]["content"]
    return fun_fact


@entrypoint()
def run_workflow(country:str)->dict:
    """Main WorkFlow That Generates a random city and fetch a fun fact about it"""
    city = generate_random_city(country).result()
    fun_fact = generate_fun_fact(city).result()
    
    print({"Country":{country},"City":{city},"Fun_Fact":{fun_fact}})
    return {"Country":{country},"City":{city},"Fun_Fact":{fun_fact}}



# To Run The Above Flow

def flow():
    run_workflow.invoke("Indonesia")



def flow_stream():
    for events in run_workflow.stream("Zambia"):
        print(events)