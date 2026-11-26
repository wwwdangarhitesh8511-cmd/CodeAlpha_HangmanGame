import os
import shutil

def organize_images():
    source_folder = input("જે ફોલ્ડરમાંથી ફાઇલો ખસેડવી છે તેનો પાથ લખો: ")
    destination_folder = input("જે નવા ફોલ્ડરમાં ફાઇલો મૂકવી છે તેનો પાથ લખો: ")

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
        print(f"નવું ફોલ્ડર બનાવ્યું: {destination_folder}")

    files = os.listdir(source_folder)
    jpg_count = 0

    for file in files:
        if file.lower().endswith('.jpg'):
            src_path = os.path.join(source_folder, file)
            dest_path = os.path.join(destination_folder, file)
            shutil.move(src_path, dest_path)
            print(f"ખસેડવામાં આવી: {file}")
            jpg_count += 1

    print(f"\nકામ પૂરું થયું! કુલ {jpg_count} .jpg ફાઇલો ખસેડવામાં આવી.")

if __name__ == "__main__":
    organize_images()
