"""
Simple test script: download a single bird image and show a thumbnail.
"""
from fastdownload import download_url
from fastai.vision.all import *

# try to get search_images; if it's not available, we'll fall back to a fixed URL
try:
    from fastai.vision.all import search_images
except Exception:
    search_images = None

FALLBACK_URL = 'https://placekitten.com/800/600'

try:
    if search_images is None:
        print('search_images not available; using fallback URL')
        urls = [FALLBACK_URL]
    else:
        urls = search_images('bird photos', max_images=1)

    if not urls:
        print('No URLs available to download')
    else:
        dest = 'bird.jpg'
        try:
            download_url(urls[0], dest, show_progress=False)
        except Exception as e:
            print('download_url failed, trying requests fallback:', repr(e))
            try:
                import requests
                import certifi
                headers = {'User-Agent': 'python-requests/fastai-test'}
                try:
                    verify_path = certifi.where()
                except Exception:
                    verify_path = True

                r = requests.get(urls[0], headers=headers, verify=verify_path, timeout=15)
                r.raise_for_status()
                with open(dest, 'wb') as f:
                    f.write(r.content)
            except Exception as e2:
                print('requests fallback failed:', repr(e2))
                print('As a last resort, trying insecure download (verify=False)')
                try:
                    import requests
                    headers = {'User-Agent': 'python-requests/fastai-test'}
                    r = requests.get(urls[0], headers=headers, verify=False, timeout=15)
                    r.raise_for_status()
                    with open(dest, 'wb') as f:
                        f.write(r.content)
                except Exception as e3:
                    print('insecure fallback also failed:', repr(e3))
                    raise

        im = Image.open(dest)
        print('Downloaded image size:', im.size)
        thumb = im.copy()
        thumb.thumbnail((256,256))
        thumb.save('bird_thumb.jpg')
        print('Saved thumbnail to bird_thumb.jpg')
except Exception as e:
    print('Error running test script:', repr(e))
