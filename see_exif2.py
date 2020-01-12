from PIL import Image
from PIL.ExifTags import TAGS

def get_exif_data(imagefile):
	img = Image.open(imagefile)
	exif_data = img._getexif()
	return exif_data

def convert_exif_data(exif_data):
	return {TAGS.get(k):v for (k,v) in exif_data.items()}

def get_exif_orientation(imagefile):
	exifdata = get_exif_data(imagefile)
	return convert_exif_data(exifdata)["Orientation"]

print(get_exif_orientation("testimage.jpg"))