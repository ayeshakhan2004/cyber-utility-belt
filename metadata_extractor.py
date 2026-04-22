import argparse
import sys
from PIL import Image
from PIL.ExifTags import TAGS

def get_arguments():
    parser = argparse.ArgumentParser(description="🦇 Cyber Utility Belt - Image Metadata Extractor")
    parser.add_argument("-i", "--image", dest="image", required=True, help="Path to the image file")
    
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
        
    return parser.parse_args()

def extract_metadata(image_path):
    try:
        image = Image.open(image_path)
        exif_data = image._getexif()
        metadata = {}
        
        if exif_data:
            for tag_id, value in exif_data.items():
                tag_name = TAGS.get(tag_id, tag_id)
                # Skip massive binary data like MakerNote or PrintImageMatching
                if isinstance(value, bytes):
                    continue
                metadata[tag_name] = value
        return metadata
        
    except FileNotFoundError:
        print(f"\n[!] Error: The file '{image_path}' was not found.")
        sys.exit(1)
    except Exception as e:
        print(f"\n[!] An error occurred: {e}")
        sys.exit(1)

def print_results(metadata):
    print("\n🦇 Cyber Utility Belt - Image Metadata")
    print("-" * 55)
    
    if not metadata:
        print("[-] No EXIF metadata found. The image might have been scrubbed.")
        print("-" * 55)
        return

    for key, value in metadata.items():
        print(f"{str(key):<25}: {str(value)}")
    print("-" * 55)

if __name__ == "__main__":
    options = get_arguments()
    print(f"[*] Analyzing {options.image}...")
    extracted_data = extract_metadata(options.image)
    print_results(extracted_data)