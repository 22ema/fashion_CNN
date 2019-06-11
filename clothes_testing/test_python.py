import argparse
parser = argparse.ArgumentParser()
parser.add_argument("image", type=str,help="image_read")

args = parser.parse_args()
print(args.image) 
print("hello")
