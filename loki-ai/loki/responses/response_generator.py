import requests  

class ResponseGenerator:
    def __init__(self, memory_manager, real_time_data):
        self.memory_manager = memory_manager
        self.real_time_data = real_time_data  
        self.groq_api_key = "your_api_key_here"  

    def generate_response(self, query):
        query = query.lower()

        # Handle greetings
        if "good morning" in query:
            return "Good morning! How can I assist you today?"
        elif "good afternoon" in query:
            return "Good afternoon! How can I help you?"
        elif "good evening" in query:
            return "Good evening! What can I do for you?"
        elif "hello" in query or "hi" in query:
            return "Hello! How can I assist you?"

        # Check memory for relevant information
        memory_response = self.memory_manager.retrieve_information(query)
        if memory_response:
            return memory_response

        # Query Groq API directly
        groq_response = self.query_groq(query)
        if groq_response:
            return groq_response

        # Default response if no information is found
        return "I'm sorry, I don't have an answer for that."

    def query_groq(self, query):
        try:
            url = "your_endpoint_url_here"  
            headers = {
                "Authorization": f"Bearer {self.groq_api_key}",
                "Content-Type": "application/json"
            }
            payload = {
                "model": "meta-llama/llama-4-scout-17b-16e-instruct",  
                "messages": [      
                    {"role": "user", "content": query}
                ]
            }
            response = requests.post(url, json=payload, headers=headers)
            
            if response.status_code == 200:
                data = response.json()
                return data.get("choices", [{}])[0].get("message", {}).get("content", "No response from Groq.")
            else:
                return f"Groq API error: {response.status_code} - {response.text}"
        except Exception as e:
            return f"Error fetching response from Groq: {e}"