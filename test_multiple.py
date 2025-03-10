import os
import io
from PIL import Image
from pydantic_ai import Agent, BinaryContent


agent = Agent(
    "google-gla:gemini-2.0-flash-exp",
    result_type=str,
    system_prompt=(
        "Give a caption to the what you see in the pictures."
        "Give a short description of what you see in the pictures."
    )
)

img_binary_ls: list[bytes] = []
for dirpath, _, filenames in os.walk("./assets"):
    for filename in filenames:
        print(filename)
        with open(os.path.join(dirpath, filename), "rb") as img_file:
            image_bytes = img_file.read()
            img_binary_ls.append(image_bytes)


def test_multiple_individual():
    prepared_images_ls = [BinaryContent(img_binary, media_type="image/png") for img_binary in img_binary_ls]

    result = agent.run_sync(
        [
            "What do you see in this picture ?",
            *prepared_images_ls
        ]
    )

    print(result.data, end="\n")
    print(result.usage())


def test_multiple_single(cols=2, thumb_size=(500, 500)):
    images = [Image.open(io.BytesIO(byte_img)) for byte_img in img_binary_ls]
    for img in images:
        img.thumbnail((500, 500))

    # Determine grid size
    num_images = len(images)
    rows = (num_images + cols - 1) // cols  # Ceiling division
    collage_width = cols * thumb_size[0]
    collage_height = rows * thumb_size[1]
    
    # Create a new blank image for the collage
    collage = Image.new("RGB", (collage_width, collage_height))
    
    # Paste each image into the collage
    for index, img in enumerate(images):
        x = (index % cols) * thumb_size[0]
        y = (index // cols) * thumb_size[1]
        collage.paste(img, (x, y))
    
    # Save collage to bytes
    collage_buffer = io.BytesIO()
    collage.save(collage_buffer, format="PNG")
    collage_buffer.seek(0)
    return collage_buffer.read()


# Create the collage image bytes from all the images
collage_image_bytes = test_multiple_single()

# Prepare a single BinaryContent for the collage
prepared_collage = BinaryContent(collage_image_bytes, media_type="image/png")

# Pass the collage as a single input along with a prompt
result = agent.run_sync(
    [
        "What do you see in this picture?",
        prepared_collage,
    ]
)

print(result.data)
print(result.usage())
