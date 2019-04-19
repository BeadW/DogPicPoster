from GetImage import FetchImage
from UseImage import PostImage
import facebook

RetrieveImage = FetchImage("https://dog.ceo/api/breeds/image/random")
RetrieveImage.request()
RetrieveImage.store_link()
RetrieveImage.respond()
RetrieveImage.store_image()
SendImage = PostImage('')
SendImage.set_token()


fb = facebook.GraphAPI(access_token=SendImage.key)

fb.put_photo(image=open(RetrieveImage.filename, 'rb'),
            message=SendImage.content)