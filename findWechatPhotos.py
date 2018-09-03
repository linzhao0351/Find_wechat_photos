#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 10:30:54 2018

@author: linzhao
"""

import os
import shutil

class findWechatPhotos():
    
    def __init__(self):      

        self.srcDir = input('Please enter the image2 folder path: ').strip(' ')
        self.targetDir = os.path.join(os.path.expanduser("~"), "Desktop", "all_images")
        
        self.__makeDir(self.targetDir)
        self.__makeDir(os.path.join(self.targetDir, "th_images"))
        self.__makeDir(os.path.join(self.targetDir, "th_images", "abbr"))
        self.__makeDir(os.path.join(self.targetDir, "previous_images"))
        
        print("Search begins, please wait...")
         
    def __makeDir(self,path):
        isExist = os.path.exists(path)
        if isExist:
            pass
        else:
            os.mkdir(path)
        return path
        
    def traversefile(self, folder):
        count = 0
        for filename in os.listdir(folder):
            file = os.path.join(folder, filename)
            if os.path.isdir(file) == True:
                count += self.traversefile(file)
            
            if os.path.isdir(file) == False:
                if os.path.splitext(filename)[1] == ".jpg" or os.path.splitext(filename)[1] == ".png" or os.path.splitext(filename)[1] == ".gif":
                    targetFile = os.path.join(self.targetDir, filename)
                    shutil.copyfile(file, targetFile)
                    count += 1
                elif os.path.splitext(filename)[0][0:2] == "th":
                    if os.path.getsize(file) >= 30000:
                        targetFile = os.path.join(self.targetDir, "th_images", filename + ".jpg")          
                    else:
                        targetFile = os.path.join(self.targetDir, "th_images", "abbr", filename + ".jpg")
                    shutil.copyfile(file, targetFile)
                    count += 1
                else:
                    targetFile = os.path.join(self.targetDir, "previous_images", filename + ".jpg")  
                    shutil.copyfile(file, targetFile)
                    count += 1 
        return count
    
    def main(self):
        return self.traversefile(self.srcDir)


if __name__ == "__main__":  
    app = findWechatPhotos()
    num = app.main()
    print(str(num) + " wechat photos found.")  
        
        
        
        
