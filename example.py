import requests


def video_download(video_id: str):
    cl = requests.session()

    print('Parsing video info...')
    v_info = cl.post('https://www.youtube.com/youtubei/v1/player',
                     params={
                         'key': 'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8'
                     },
                     json={
                         "context": {
                             "client": {
                                 "clientName": "WEB",
                                 "clientVersion": "2.20220311.01.00"
                             }
                         },
                         "videoId": video_id
                     })

    v_formats = v_info.json().get('streamingData').get('formats')

    print('Parsing video of first format...')
    v_content = cl.get(v_formats[0].get('url')).content

    print('Writing to file...')
    v_file = open(video_id + '.mp4', 'wb')
    v_file.write(v_content)
    v_file.close()


# Example
video_download('0eaBEs01heA') # from https://www.youtube.com/watch?v=0eaBEs01heA
