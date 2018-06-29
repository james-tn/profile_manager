def draw_face(img):
    import requests
    from io import BytesIO
    from PIL import Image, ImageDraw
    #Convert width height to a point in a rectangle

    subscription_key = '7532d57c84d447a9adf222de78fe71a3'  # Replace with a valid subscription key (keeping the quotes in place).

    BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect'  # Replace with your regional Base URL
    headers = {
    # Request headers
    'Content-Type': 'application/octet-stream',   # this should be the content type
    'Ocp-Apim-Subscription-Key': subscription_key,
    }


 
    response = requests.post(BASE_URL,  headers=headers, data=img)
        
    faces = response.json()
    def getRectangle(faceDictionary):
        rect = faceDictionary['faceRectangle']
        left = rect['left']
        top = rect['top']
        bottom = left + rect['height']
        right = top + rect['width']
        return ((left, top), (bottom, right))


    output_image = Image.open(BytesIO(img))

    #For each face returned use the face rectangle and draw a red box.
    draw = ImageDraw.Draw(output_image)
    for face in faces:
        draw.rectangle(getRectangle(face), outline='red')

    return len(faces),output_image


#image_path = "path_to_image"

# Read the image into a byte array
#image_data = open(image_path, "rb").read()

#image = draw_face(image_data)
#image.show()


