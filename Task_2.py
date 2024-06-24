from PIL import Image

def encrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = img.load()
    width, height = img.size
    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            # swapping red and blue channels
            encrypted_pixel = (b, g, r)
            pixels[i, j] = encrypted_pixel
    img.save(output_path)
    print("Image encrypted successfully!")

def decrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = img.load()
    width, height = img.size
    for i in range(width):
        for j in range(height):
            b, g, r = pixels[i, j]
            # swapping red and blue channels back
            decrypted_pixel = (r, g, b)
            pixels[i, j] = decrypted_pixel
    img.save(output_path)
    print("Image decrypted successfully!")

# Example usage
encrypt_image('C:\\Users\\91997\\Desktop\\Cyber Security\\Prodigy Internship\\input_image.png', 'C:\\Users\\91997\\Desktop\\Cyber Security\\Prodigy Internship\\encrypted_image.png', key=0)
decrypt_image('C:\\Users\\91997\\Desktop\\Cyber Security\\Prodigy Internship\\encrypted_image.png', 'C:\\Users\\91997\\Desktop\\Cyber Security\\Prodigy Internship\\decrypted_image.png', key=0)
