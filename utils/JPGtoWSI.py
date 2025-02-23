import pyvips

# def convert_jpg_to_svs(input_jpg, output_svs):
#     image = pyvips.Image.new_from_file(input_jpg)
#     image.tiffsave(output_svs, tile=True, pyramid=True, compression="jpeg", bigtiff=True)
#     print(f"Converted {input_jpg} to {output_svs}")

def convert_jpg_to_tiff(input_jpg, output_tiff):
    # 使用 pyvips 读取 jpg 文件
    image = pyvips.Image.new_from_file(input_jpg)

    # 将其保存为 TIFF 格式
    image.write_to_file(output_tiff)

    print(f"Conversion complete: {input_jpg} -> {output_tiff}")

# 示例
convert_jpg_to_tiff("/home/input/3.jpg", "/home/input/3.tiff")
