#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Yuva :)"

if __name__ == "__main__":
    app.run()


# In[ ]:





# In[ ]:





# In[ ]:




