from openai import OpenAI



def generate_logo_prompt():
    api_key = open(".env", mode="r").read()
    client = OpenAI(api_key=api_key)
    response = client.images.generate(
      model="dall-e-3",
      size="1024x1024",
      n = 1,
      prompt=("A cartoonish logo for 'GeoGenie'. "
              "The logo  featuring a small globe at the center,Along the diameter of the globe, have 'GeoGenie' written in a playful, stylized font. "
              "A friendly looking genie, with a big smile, who is wrapping her tail around the globe. "
              "The overall art style should be whimsical and fun, with vibrant colors. "
              "Use a color scheme of pink and blue, with a touch of white.")


    )
    image_url = response.data[0].url
    return image_url

#print(generate_logo_prompt())






