import os
from dotenv import load_dotenv
from google import genai
import argparse
from google.genai import types
from prompts import system_prompt

# Unecessary code:
# from functions.get_files_info import schema_get_files_info
# from functions.get_file_content import schema_get_files_content
# from functions.run_python_file import schema_run_python_file
# from functions.write_file_content import schema_write_file

from call_function import available_functions, call_function

def main():
    # print("Hello from ai-agent-in-python-project!")
    # load_dotenv()
    # api_key = os.environ.get("GEMINI_API_KEY")
    # client = genai.Client(api_key=api_key)

    # parser = argparse.ArgumentParser(description="Chatbot")
    # parser.add_argument("user_prompt", type=str, help="User prompt")
    # parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    # args = parser.parse_args()

    # # Create a new list of types.Content, and set the user's prompt as the only message (for now):
    # messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

# # Now we can access `args.prompt`
#     response = client.models.generate_content(
#         # model='gemini-2.0-flash-001'  # --> This model offers a generous free-tier
#         model='gemini-2.5-flash',       # This specific model was required to pass the test case on boot.dev
#         # contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.",
#         # contents=args.prompt
#         contents=messages,
#         config=types.GenerateContentConfig(system_instruction=system_prompt),
#     )

    # print(response.text)

    # if response.usage_metadata is None:
    #     raise RuntimeError("No usage metadata received")

    # # print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    # # print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    # if args.verbose:
    #     print("User prompt:", args.user_prompt)
    #     print("Prompt tokens:", response.usage_metadata.prompt_token_count)
    #     print("Response tokens:" ,response.usage_metadata.candidates_token_count)

    # print("Hello from ai-agent-in-python-project!")
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    # Create a new list of types.Content, and set the user's prompt as the only message (for now):
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    
    generate_content(client, messages, args.verbose)

def generate_content(client, messages, verbose):
    
    for _ in range(20):  # up to 20 iterations
        try:
            response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=messages,
            # config=types.GenerateContentConfig(system_instruction=system_prompt),
            config=types.GenerateContentConfig(
                tools=[available_functions], system_instruction=system_prompt
            )
        )

        # 1) Add candidates to messages
            if response.candidates:
                for candidate in response.candidates:
                    messages.append(candidate.content)

            # 2) If there are NO function calls, maybe we’re done
            if not response.function_calls:
                if response.text:
                    print("Final response:")
                    print(response.text)
                    break
                # no tools and no text, just let the loop continue
                continue

            # 3) There AR  E function calls: run them and collect results
            function_responses = []

            for function_call_part in response.function_calls:
                # this is the same helper from the previous lesson
                function_call_result = call_function(function_call_part, verbose)

                if (
                    not function_call_result.parts
                    or not function_call_result.parts[0].function_response
                ):
                    raise Exception("empty function call result")

                if verbose:
                    print(f"-> {function_call_result.parts[0].function_response.response}")

                # collect the Part so we can send it back to the model
                function_responses.append(function_call_result.parts[0])

            if not function_responses:
                raise Exception("no function responses generated, exiting.")

            # 4) Convert list of tool results into a single user Content and append
            messages.append(types.Content(role="user", parts=function_responses))

            # loop continues, model will see tool outputs next iteration

        except Exception as e:
            print("Error:", e)
            break

# ----------

        #     any_tool_calls = False
        #     # 1.3 After you have the responses from each function call, use the types.Content constructor to convert the list of responses into a message with a role of user, and append it to your messages.
        #     tool_results = []   # each result is something like a text or JSON string


        #     # 1.2 After calling client's generate_content method, check the .candidates property of the response. It's a list of response variations (usually just one). It contains the equivalent of "I want to call get_files_info," so we need to add it to our conversation. Iterate over each candidate and add its .content to your messages list.
        #     for candidate in response.candidates:
        #         messages.append(candidate.content)
        #         if candidate.content.parts 
        #             any_tool_calls = True

        #             tool_results.append(tool_output)


        #     tool_results_message = types.Content(
        #         role="user",
        #         parts=[
        #             types.Part.from_text(result)
        #             for result in tool_results
        #         ],
        #     )

        #     messages.append(tool_results_message)
        #     pass
        # except Exception as e:
        #     print("Error:", e)
        #     break


    

    # ... (rest of the function)

    # print(response.text)
    # if not response.function_calls:
    #     print("Response:")
    #     print(response.text)
    #     return
        
    #     # for response_function_call in response.function_calls:
    #         # print(f"Calling function: {response_function_call.name}({response_function_call.args})")
            
    #     # ----------------------------------

    # function_responses = []

    # for function_call_part in response.function_calls:
    #     function_call_result = call_function(function_call_part, verbose)

    #     if (
    #         not function_call_result.parts
    #         or not function_call_result.parts[0].function_response
    #     ):
    #         raise Exception("empty function call result")

    #     if verbose:
    #         print(f"-> {function_call_result.parts[0].function_response.response}")

    #     function_responses.append(function_call_result.parts[0])

    # if not function_responses:
    #     raise Exception("no function responses generated, exiting.")
        
    # # ---------------------

        
    # if response.usage_metadata is None:
    #     raise RuntimeError("No usage metadata received")

    # # print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    # # print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    # if verbose:
    #     print("User prompt:", messages[0].parts[0].text)
    #     print("Response tokens:" ,response.usage_metadata.candidates_token_count)

if __name__ == "__main__":
    main()



