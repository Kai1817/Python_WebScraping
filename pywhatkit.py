#(1) the google search using keyword with 'pywhatkit' module
"""
You can perform a Google search using the following simple command. 
It opens your browser and searches for the topic you have given in your code
"""
import pywhatkit
try:
    pywhatkit.search('facts about AI')
    print('done searching')
except:
    print('error in searching')


#(2)play videos on youtube 
""" 
If you pass the topic name as parameter, it plays the random video on that topic. 
On passing the URL of the video as the parameter, it open that exact video.
"""
import pywhatkit
try:
    pywhatkit.playonyt('python programming') #passing parameter which plays random video
    print('searching done')
except:
    print('error in searching')

#----

import pywhatkit
try:
    pywhatkit.playonyt('https://www.youtube.com/watch?v=H35cMgmlkcw&ab_channel=REALCRICKET') 
    print('searching done') #passing the url which plays the exact video
except:
    print('error in searching')

#(3) Get information on  particular topic

"""
We can get brief information on a particular topic. 
We can also limit the number of lines to be printed. 
Also, make sure that you are searching for the topics that are available on Wikipedia.
"""

import pywhatkit
try:
    pywhatkit.info("Data Science",lines = 7) 
    print('searching done') 
except:
    print('error in searching')