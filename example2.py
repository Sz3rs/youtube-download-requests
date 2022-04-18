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
    v_file = open(video_id + '.mp4', 'wb')

    v_url = v_formats[0].get('url')
    # v_content = cl.get(v_formats[0].get('url')).content
    size = int(requests.head(v_url) \
               .headers.get('Content-Length'))

    print('Video Size:', round(size / 1024 / 1024), 'mb')
    # print(r.headers)
    # print(r.text)
    print('Parsing video...')
    with requests.get(v_url, stream=True) as request:
        request.raise_for_status()
        i = 0
        for chunk in request.iter_content(chunk_size=8192):
            if chunk:
                v_file.write(chunk)
                print("%.1f" % (i * 100 / (size / 8192)), '/ 100')
                i += 1

    print('Success!')
    v_file.close()


# Example with %'s
video_download('0eaBEs01heA') # from https://www.youtube.com/watch?v=0eaBEs01heA
