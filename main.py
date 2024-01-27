import os
import shutil

def main():
    APP_DATA_PATH = os.getenv('LOCALAPPDATA')
    BASE_PATH = "Pal\Saved\SaveGames"
    SAVE_PATH = "\\".join([APP_DATA_PATH, BASE_PATH])

    DESKTOP_PATH = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    OUTPUT_PATH = "\\".join([DESKTOP_PATH, "palworld-save-export"])

    print(f"OUTPUT_PATH: {OUTPUT_PATH}.zip")
    print(f"SAVE_PATH: {SAVE_PATH}")

    shutil.make_archive(OUTPUT_PATH, "zip", SAVE_PATH)
    print('DONE! .zip file created at OUTPUT_PATH above.')

    input("Press enter to exit;")

if __name__ == '__main__':
    main()
