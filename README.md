
# Comments 
Get youtube comments with Python. 

## Setup 

1. Install required dependencies with `pipenv install`.

2. Create a file called `key.py` that has your Youtube Data API KEY. You can make one online at https://developers.google.com/youtube/v3/getting-started.  
`echo 'KEY = "YOUR_API_KEY"' > key.py` 

3. Create an alias for easier access. In short "comments" would equate to us cding into the folder and running comments.py within the pipenv context. Save this alias inside shell rc file.  
`alias comments='cd ~/dev/comments/ && pipenv run py comments.py'`. 

4. `comments my_video_id` // to get root comments to stdout. 

5. You can pipe the comments to less or save to a file. You have to wait for the sync requests. 
`comments my_video_id | less`
