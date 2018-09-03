# Find_wechat_photos

This little program helps you find all the photos in your WeChat chat history. 

## How to use it

1. Download or copy the file "findWechatPhotos.py" to your computer;
2. Connect your phone to your computer, find the folder "./Tencent/MicroMsg". Under this folder, you will find folder(s) named after a MD5 string that looks like "7484356f8cc3e1449c8a46df42f98ace"; find folder "/image2" under this folder and copy to your computer.
3. Open your Terminal or Command Prompt, change the directory to the folder you put this code file, e.g., - cd /Users/username/Desktop - ;
4. Run the program by typing - python findWechatPhotos.py -; the program will require you to type the path of the "/image2" folder on your computer. For example, if you put the "/image2" folder on your desktop, the path will be "/Users/username/Desktop/image2".
5. Press enter after you type the path, the program will create a folder called "/all_images" on your desktop that contains all photos in your WeChat history.

## Note

In "/all_images" folder, besides those photos, there will be another two folders. Folder "/th_images" contains thumbnails or WeChat photos you did not open. Photos whose size is smaller than 3000 bytes (30 KB) are in the folder "/th_images/abbr"; those are photos you cannot see clearly in general. Folder "previous_images" contains photos from the previous WeChat history you transfered from old phones.
