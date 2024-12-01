from PIL import Image
import os

def convert_image_to_gray_and_binary(input_path):
    # Verificar se o arquivo existe
    if not os.path.exists(input_path):
        print(f"Erro: O arquivo '{input_path}' não existe.")
        return None, None

    # Abrir a imagem colorida
    try:
        img_color = Image.open(input_path)
    except Exception as e:
        print(f"Erro ao abrir a imagem: {e}")
        return None, None

    # Converter para níveis de cinza
    img_gray = img_color.convert('L')

    # Calcular o limiar como a média dos valores de intensidade
    histogram = img_gray.histogram()
    total_pixels = sum(histogram)
    cumulative_intensity = sum(i * histogram[i] for i in range(256))
    mean_intensity = cumulative_intensity / total_pixels
    threshold = int(mean_intensity)

    # Usar a função 'point' para aplicar o limiar binário em toda a imagem
    img_binary = img_gray.point(lambda p: 255 if p >= threshold else 0)

    # Salvar as imagens resultantes
    output_dir = os.path.splitext(input_path)[0] + '_converted'
    os.makedirs(output_dir, exist_ok=True)

    img_gray.save(os.path.join(output_dir, 'Lenna_cinza.png'))
    img_binary.save(os.path.join(output_dir, 'Lenna_binaria.png'))

    print(f"Imagens convertidas e salvas em: {output_dir}")

    return img_gray, img_binary

# Exemplo de uso
input_path = 'Lenna.png'
convert_image_to_gray_and_binary(input_path)
