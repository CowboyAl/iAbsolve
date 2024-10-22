# getResponse.py
from openai import OpenAI;
import os;

def getResponse(name, denomination, type):

    client = OpenAI()
    OpenAI.api_key = os.environ["OPENAI_API_KEY"] ;
    
    outputType = "an absolution";
    if type == "blessing":
        outputType = "a blessing";
        
    #"content": "Write a blessing for someone who committed the sin of adultery and reply in the first person"

    
    role = "You are a " + denomination;
    content = "Write " + outputType + " for someone who committed the act of " + name + " and write the response in the first person";

    print("role - " +role);
    print("content - " + content);
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": role},
            {
                "role": "user",
                "content": content
            }
        ]
    )
    
    s = completion.choices[0].message.content
    #s = s.replace("\n", "<br>")

    return s