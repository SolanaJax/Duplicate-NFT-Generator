#------------------------------------------------------#
#    Duplicate NFT Generator - Made by Jax and Anton   #
#             https://twitter.com/SolanaJax            #
#                      MIT license                     #
#                        v0.0.3                        #
#                 Discord Tag Jax#3333                 #
#------------------------------------------------------#

# Donations are not necessary but always welcomed 3NEVEHsNgzgCGgdzNpxZrH8ws1eJaUV9AAbjDag9xxCq

# This generator follows the newest sugar version of the metadata standard https://docs.metaplex.com/developer-tools/sugar/guides/preparing-assets

# Modules
import shutil
import os

# Make sure to keep everything in the same folder asset folder and index.py should be within the same folder
# put your desired duplicated asset in the "asset" folder

# Don't change this unless you know what you're doing
nameCount = 1
imageCount = 0
fileCount = 0
uriCount = 0

# Amount of NFT Metadata that you want to generate
amountOfNfts = 10

# text field for metadata generation
name = "Write the name of the NFT"
symbol = "Write the symbol of the NFT"
description = "Write the description of the NFT"
traitType = "Write the trait type of the NFT"
trait = "Write the trait of the NFT"

# IMPORTANT write the same name as the gif assets you have in the asset folder
assetName = "example"
# IMPORTANT write the extension you asset is in (png, jpg, gif)
fileExtension = "gif"

path = "generatedAssets"

pathExist = os.path.exists(path)

# Check if the path exists and if it does not it creates a new directory
if pathExist == False:
    print("")
    print("Creating path for generated assets")
    print("")
    os.makedirs(path)
else:
    print("")
    print("Path does already exist. Overwriting existing files")
    print("")

print("")
print("Generating assets. . .")
print("")

# This is a loop that creates all the metadata files you need if you want to create duplicate gif NFTs
while fileCount < amountOfNfts:

    # Creates the duplicate gif files
    src_path = r"asset\%s.%s" % (assetName, fileExtension)
    dst_path = r"generatedAssets\%s.%s" % (fileCount, fileExtension)
    shutil.copy(src_path, dst_path)

    # Creates the metadata files
    file = open(r'generatedAssets\%s.json' % (fileCount), 'w')
    file.write('''{
  "name": "%s #%s",
  "symbol": "%s",
  "description": "%s",
  "image": "%s.%s",
  "attributes": [
    {
      "trait_type": "%s",
      "value": "%s"
    }
  ],
  "properties": {
    "files": [
      {
        "uri": "%s.%s",
        "type": "image/%s"
      }
    ]
  }
}
    ''' % (name, nameCount, symbol, description, imageCount, fileExtension, traitType, trait, uriCount, fileExtension, fileExtension))
    file.close()
    nameCount += 1
    fileCount += 1
    imageCount += 1
    uriCount += 1
    print("Asset-Pair:", fileCount, "has been generated")

print("")
print("All", fileCount, "Asset-Pairs has been successfully generated.")
print("")
