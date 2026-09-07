## Weekly project
# list of questions

questions= [ 

("question": (("What is the capital city of Kenya?",))
"choices":
 ("A": "Mombasa","B": "Nairobi","C": "Kisumu","D": "Nakuru"  ,
 "Answer": "B" ),

"question": ("What is the capital city of Tanzania?"),
"choices":
 ("A": "Dodoma","B": "Mwanza","C": "Arusha","D": "Mzuzu" ,
 "Answer": "A"),

 ("question": "What colour is the sky?",
 "choices": ("A": "Blue","B": "Red","C": "Yellow","D": "Black" ,
 "Answer": "A",)

("question": "how many days are there  in a week?",
" choices": ("A", "5", "B", "6", "C", "7", "D", "8" }
"Answer": "C") 
]

input:(( "question": "What is the capital city of Kenya?",
"choices":
 {"A": "Mombasa","B": "Nairobi","C": "Kisumu","D": "Nakuru" },
 "Answer": "B")),
if input == "B":
 print ( int(10) "Correct!") 
else:
 print(int(0) "Incorrect!"),

input: ("question": "What is the capital city of Tanzania?",
"choices":
 {"A": "Dodoma","B": "Mwanza","C": "Arusha","D": "Mzuzu" },
 "Answer": "A",)
 if input == "A":
 print (int(10) "Correct!")
else:
 print (int(0) "Incorrect!"),

input: ("question": "What colour is the sky?",
 "choices": ("A": "Blue","B": "Red","C": "Yellow","D": "Black" ,
"Answer": "A")
if input == "A":
 print (int(10) "correct!")
else:
 print (int(0) "Incorrect!"),

input: ("question": "how many days are there  in a wee?",
" choices": ("A": "5","B": "6","C": "7","D": "8" ),
"Answer": "C")
if input == "C":
 print(int(10) "correct!")
else:
 print(int(0) "Incorrect!"),

input: ("question": "how many days are there  in a week?"),
" choices": ("A": "5","B": "6","C": "7","D": "8" ,
"Answer": "C")
if input == "C":
 print(int(10) "correct!")
else:   
 print(int(0) "Incorrect!")


