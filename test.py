# Python program to read json
import json
  
# Opening JSON file
with open('data.json') as f:

   # returns JSON object as  a dictionary
   data = json.load(f)
   user_settings = data['user_settings']
   print(data, "\n")
   print(user_settings, "\n")
   print(user_settings['window_width'])
   print(user_settings['window_height'])
   print(user_settings['fps_cap'])
