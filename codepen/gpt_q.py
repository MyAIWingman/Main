import requests
import os
import openai
import pd




openai.api_key = '[Enter API KEY]'
model_id = 'gpt-3.5-turbo'

def handler(pd: "pipedream"):
    kk = str( pd.steps["ocrspace_1"]["$return_value"]["ParsedResults"][0]["ParsedText"])
    ##kk = str("what is capital of nairobi")
    rr =  "Don't try too hard and don't be cheesy but Give me a slightly flirty and funny response to " + kk 
   

    completion = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages=[
        {"role": "user", "content": rr}
    ])
    final = completion.choices[0].message

    #json_obj = json.loads(final)

# Extract the "message" value from the "funnyResponse" object
   # message = json_obj["funnyresponse"]
    #flirtymessage = json_obj["flirtyresponse"]
    #questionmessage = json_obj["questionresponse"]
   
    
   
    #response = completion.choices[0].text.strip()
    

    

    #str_res = str(final)
    #data = json.loads(str_res)

    # extract the Flirty response
    #flirt_response = data['content'].split('Question response:')[0].split('Flirty response:')[1].strip()

   


    #json_dict = json.loads(str_res)
    #content = json_dict['content']
    #flirt_response = content.split('Flirty response: "')[1].split('"')[0]

# Extracting the flirt response
    

    #print(flirt_response)

    #json_obj = json.loads(final)

# Extract the "message" value from the "funnyResponse" object
   # message = json_obj["funnyresponse"]
    #flirtymessage = json_obj["flirtyresponse"]
    #questionmessage = json_obj["questionresponse"]
# Print the result
   # print(message)

# Print the results
 
    #return {"foo": {"funny":message,"flirty":flirtymessage,"question":questionmessage}}
    

    
   
    


    return final



    ##print(rr)
    ##initial_q = rr
 

 



  
