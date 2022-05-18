import requests
URL="https://opentdb.com/api.php"
parameters={
    "amount":10,
    "category":18,
    "type":"boolean"
}

response=requests.get(url=URL,params=parameters)
response.raise_for_status()
question_data=response.json()["results"]
print(question_data)
#print(question_data)

# question_data = [
#     {"category": "Science: Computers",
#      "type": "boolean", "difficulty": "medium",
#      "question": "The HTML5 standard was published in 2014.",
#      "correct_answer": "True",
#      "incorrect_answers": ["False"]},
#     {"category": "Science: Computers", "type": "boolean", "difficulty": "medium",
#      "question": "The very first recorded computer &quot;bug&quot; was a moth found inside a Harvard Mark II computer.",
#      "correct_answer": "True", "incorrect_answers": ["False"]},
#     {"category": "Science: Computers", "type": "boolean", "difficulty": "medium",
#      "question": "All program codes have to be compiled into an executable file in order to be run. This file can then be executed on any machine.",
#      "correct_answer": "False", "incorrect_answers": ["True"]},
#     {"category": "Science: Computers", "type": "boolean", "difficulty": "medium",
#      "question": "&quot;Windows NT&quot; is a monolithic kernel.",
#      "correct_answer": "False", "incorrect_answers": ["True"]},
#     {"category": "Science: Computers", "type": "boolean", "difficulty": "medium",
#      "question": "To bypass US Munitions Export Laws, the creator of the PGP published all the source code in book form. ",
#      "correct_answer": "True", "incorrect_answers": ["False"]},
#     {"category": "Science: Computers", "type": "boolean", "difficulty": "medium",
#      "question": "The open source program Redis is a relational database server.",
#      "correct_answer": "False", "incorrect_answers": ["True"]},
#     {"category": "Science: Computers", "type": "boolean", "difficulty": "medium",
#      "question": "AMD created the first consumer 64-bit processor.",
#      "correct_answer": "True", "incorrect_answers": ["False"]},
#     {"category": "Science: Computers", "type": "boolean", "difficulty": "medium",
#      "question": "Early RAM was directly seated onto the motherboard and could not be easily removed.",
#      "correct_answer": "True", "incorrect_answers": ["False"]},
#     {"category": "Science: Computers", "type": "boolean", "difficulty": "medium",
#      "question": "The last Windows operating system to be based on the Windows 9x kernel was Windows 98.",
#      "correct_answer": "False", "incorrect_answers": ["True"]},
#     {"category": "Science: Computers", "type": "boolean", "difficulty": "medium",
#      "question": "Android versions are named in alphabetical order.",
#      "correct_answer": "True", "incorrect_answers": ["False"]}
# ]
